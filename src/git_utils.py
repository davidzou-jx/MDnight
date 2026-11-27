from pathlib import Path

from git import Repo
from consts import *


# gets list of add/mod files since last run
def changed_files(vault: Path):
    repo = Repo(vault)
    commits = repo.iter_commits(MAIN_GIT_BRANCH)
    latest = None
    for commit in commits:
        if COMMIT_STR in str(commit.message):
            latest = commit
            break
    if latest is None: print("No commit found, manually create one containing " + COMMIT_STR)
    diffs = latest.diff(None, diff_filter="AMR")  # compares last run with current state
    out = []
    for diff in diffs:
        p = diff.b_path
        if p.endswith(".md"):
            out.append(p)
    return out


# gets a dict of file paths mapped to the text content
def get_text(vault: Path):
    files = changed_files(vault)
    text = {}
    for file in files:
        with open(vault / file) as f:
            text[file] = f.read()
    return text


def make_commit(vault: Path, message: str, files: list):
    repo = Repo(vault)
    for file in files:
        repo.index.add(file)
    repo.index.commit(message)
