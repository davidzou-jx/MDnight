from git import Repo
from consts import *

# gets list of add/mod files since last run
def changed_files(vault):
    repo = Repo(vault)
    commits = repo.iter_commits(MAIN_BRANCH)
    latest = None
    for commit in commits:
        if COMMIT_STR in str(commit.message):
            latest = commit
            break
    if latest is None: print("No commit found, manually create one containing" + COMMIT_STR)
    diffs =  latest.diff(None, diff_filter="AM") # compares last run with current state
    out = []
    for diff in diffs: out.append(diff.b_path)
    return out

# gets a dict of file paths mapped to the text content
def get_text(vault):
    if vault[len(vault)-1] is not "/": vault = vault + "/"
    files = changed_files(vault)
    text = {}
    for file in files:
        with open(vault+file) as f:
            text[file] = f.read()
    return text