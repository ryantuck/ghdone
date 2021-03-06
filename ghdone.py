#!/usr/bin/env python3
from collections import namedtuple
import os
import pprint

import arrow
import click
import requests


BASE_URL = 'https://api.github.com'
SEVEN_DAYS_AGO = arrow.utcnow().replace(days=-7).date()


SimplePr = namedtuple('PR', [
    'repo',
    'num',
    'user',
    'created',
    'status',
    'title',
    'url',
])


def _auth():
    return (
        os.environ.get('GITHUB_USERNAME'),
        os.environ.get('GITHUB_TOKEN'),
    )


def _get_prs(repo, page=1):
    r = requests.get(
        url=f'{BASE_URL}/repos/{repo}/pulls',
        params={
            'state': 'all',
            'page': page,
        },
        auth=_auth(),
    )

    return r.json()


def prs_opened_for_user(repo, username, since_date=SEVEN_DAYS_AGO):
    page = 1
    results = []
    while True:
        batch = _get_prs(repo, page=page)
        tmp_results = [
            pr for pr in batch
            if arrow.get(pr['created_at']).date() >= since_date
            and pr['user']['login'] == username
        ]

        if tmp_results == []:
            break
        results += tmp_results
        page += 1

    return results


def simple_pr(pr_json):
    status = 'open'
    if pr_json['merged_at']:
        status = 'merged'
    if pr_json['closed_at']:
        status = 'closed'
    return SimplePr(
        repo=pr_json['head']['repo']['full_name'],
        num=pr_json['number'],
        user=pr_json['user']['login'],
        created=arrow.get(pr_json['created_at']).date().isoformat(),
        status=status,
        title=pr_json['title'],
        url=pr_json['html_url'],
    )


@click.command()
@click.argument('username')
@click.option('--repo', '-r',
    multiple=True,
    help='Repo of interest. Repeat flag for multiple repos.'
)
@click.option('--since',
    required=False,
    default=SEVEN_DAYS_AGO,
    help='Pull from given date. Defaults to seven days ago.',
    )
@click.option('--output',
    required=False,
    type=click.Choice(['json', 'md']),
    help='Output as json or as markdown list with links.',
)
def cli(username, repo, since, output):
    prs = []
    for r in repo:
        prs_json = prs_opened_for_user(r, username, arrow.get(since).date())
        prs += [simple_pr(pr) for pr in prs_json]

    if output == 'json':
        pprint.pprint([dict(pr._asdict()) for pr in prs])
    elif output == 'md':
        for pr in prs:
            print(f'- [{pr.repo} #{pr.num} {pr.title}]({pr.url})')
    else:
        for pr in prs:
            print(
                f'{pr.repo} {pr.num} {pr.user} '
                f'{pr.created} {pr.status: <6} {pr.title}'
            )


if __name__ == '__main__':
    cli(obj={})
