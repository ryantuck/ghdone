# ghdone

Find out what you've done recently on github.

Fetch high-level detail about PRs for a given user.

## installation

Clone, and symlink.

```
$ git clone https://github.com/ryantuck/ghdone.git ~/src/ghdone
$ ln -s ~/src/ghdone/ghdone /usr/local/bin/ghdone
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

TODO: add outputs here.
