# ghdone

Find out what you've done recently on github.

Fetch high-level detail about PRs for a given user.

## installation

Clone, and `pip install`:

```
$ git clone https://github.com/ryantuck/ghdone.git ~/src/ghdone
$ pip install -e ~/src/ghdone
```

Create a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) for github and set some `ENV` vars:

```
$ export GITHUB_USERNAME="ryantuck"
$ export GITHUB_TOKEN="abcd12345"
```

## usage

```
$ ghdone --help
Usage: ghdone [OPTIONS] USERNAME

Options:
  -r, --repo TEXT     Repo of interest. Repeat flag for multiple repos.
  --since TEXT        Pull from given date. Defaults to seven days ago.
  --output [json|md]  Output as json or as markdown list with links.
  --help              Show this message and exit.
```

## sample outputs

```
$ ghdone ryantuck --repo "ryantuck/ghdone"
ryantuck/ghdone 1 ryantuck 2018-07-31 open   add output samples to readme
$ ghdone ryantuck --repo "ryantuck/ghdone" --output json
[{'created': '2018-07-31',
  'num': 1,
  'repo': 'ryantuck/ghdone',
  'status': 'open',
  'title': 'add output samples to readme',
  'url': 'https://api.github.com/repos/ryantuck/ghdone/pulls/1',
  'user': 'ryantuck'}]
$ ghdone ryantuck --repo "ryantuck/ghdone" --output md
- [ryantuck/ghdone #1 add output samples to readme](https://api.github.com/repos/ryantuck/ghdone/pulls/1)
```
