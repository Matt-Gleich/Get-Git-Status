# Get-Git-Status ![PyPI](https://img.shields.io/pypi/v/gitStatus)

[![Actions Status](https://github.com/Matt-Gleich/Get-Git-Status/workflows/Python-Versions/badge.svg)](https://github.com/Matt-Gleich/Get-Git-Status/actions) [![Actions Status](https://github.com/Matt-Gleich/Get-Git-Status/workflows/Python-Cron/badge.svg)](https://github.com/Matt-Gleich/Python-Cron/actions)

![PyPI - Format](https://img.shields.io/pypi/format/gitStatus) ![PyPI - Status](https://img.shields.io/pypi/status/gitStatus)

Get-Git-Status is a PyPi package that allows you to get the git status of any repo. Look down below to see the documentation that will explain this more.

## Install

gitStatus is confirmed to work with the following versions:

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gitStatus)

One you have one of the supported versions make sure you have pip installed and install gitStatus with the following commands:

```bash
pip3 install gitStatus
```

## Documentation

Before you use gitStatus you need to make a object for the repo. You create this object using `gitStatus.gitStatus("PATH TO REPO")`. Below is an example:

```py
from gitStatus import gitStatus

repo = gitStatus("/Users/matthewgleich/Documents/Github/Personal/Get-Git-Status")
```

### `untrackedFiles()`

Get a list of the untracked files for a repo. Below is an example where the file `test.txt` was created under the `src` folder creating one untracked file:

```py
from gitStatus import gitStatus
repo = gitStatus("/Users/matthewgleich/Documents/Github/Personal/Get-Git-Status")
untrackedFiles = repo.untrackedFiles()
print(untrackedFiles) # Prints ["src/test.txt"]
```

### `unstagedFiles()`

Get a list of all the unstaged files and the status of that file (deleted or modified). Below is an example with the following changes not staged:

1. Deleted `src/main.py`
2. Modified `requirements.txt`

```py
from gitStatus import gitStatus
repo = gitStatus("/Users/matthewgleich/Documents/Github/Personal/Get-Git-Status")
unstagedFiles = repo.unstagedFiles()
print(unstagedFiles) # Prints {"src/main.py": "deleted", "requirements.txt": "modified"}
```

### `stagedFiles()`

Get a list of all the staged files and the status of that file (deleted, modified, or new file). Below is an example with the following changes staged:

1. Deleted `README.md`
2. Modified `src/main.py`
3. Created New File `src/actions.py`

```py
from gitStatus import gitStatus
repo = gitStatus("/Users/matthewgleich/Documents/Github/Personal/Get-Git-Status")
unstagedFiles = repo.unstagedFiles()
print(unstagedFiles) # Prints {"README.md": "deleted", "src/main.py": "modified", "src/actions.py": "new file"}
```
