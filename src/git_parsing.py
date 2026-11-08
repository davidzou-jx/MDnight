from git import Repo
from consts import *

def changed_files(vault):
    repo = Repo(vault)
    commits = repo.iter_commits(MAIN_BRANCH)
    for commit in commits:
        if COMMIT_STR in str(commit.message):
            latest = commit
            break
    if not latest: print("No commit found, manually create one containing" + COMMIT_STR)
    return repo.head.commit.diff(latest)