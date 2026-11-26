import json
import os
import re
from re import match
from datetime import datetime as dt

from dotenv import load_dotenv
from openai import OpenAI

from consts import *
from server import *
from git_utils import *


def get_edited(text: str, model: str):
    if text is None: return None

    if CLOUD_TESTING: load_dotenv()
    client = OpenAI(base_url=f"http://localhost:{SERVER_PORT}/v1" if not CLOUD_TESTING else TEST_ENDPOINT,
                    api_key="unnecessary" if not CLOUD_TESTING else os.getenv(TEST_KEY_NAME))
    model = model if not CLOUD_TESTING else TEST_MODEL
    response = client.chat.completions.create(model=model, messages=[
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": text}])
    return str(response.choices[0].message.content)  # reasoning already in diff field


def process_vault(vault: str, model: str):
    changed = changed_files(vault)
    old = get_text(vault)
    if vault[len(vault) - 1] is not "/": vault = vault + "/"
    # dont move before or else it breaks git diff
    make_commit(vault, COMMIT_STR + ": before edits at " + dt.now().strftime("%Y-%m-%d"), changed)
    reviews = {}
    for file in old:
        new = get_edited(old[file], model)
        with open(vault + file, "w") as f:
            f.write(new)
        # no need for context reset, llama is stateless and manages memory itself
        reviews = populate_review(file, new, reviews)
    with open(vault + REVIEW_FILE, "w") as f:
        json.dump(reviews, f)
    make_commit(vault, COMMIT_STR + ": after edits at " + dt.now().strftime("%Y-%m-%d"), changed)


def process_all(model: str):
    if not CLOUD_TESTING: start_server(model)
    for vault in VAULTS:
        process_vault(VAULTS[vault], model)
    end_server()


def process_indiv(vault: str, model: str):
    if not CLOUD_TESTING: start_server(model)
    process_vault(vault, model)
    end_server()


def write_back(vault:str, new: dict):
    if vault[len(vault) - 1] is not "/": vault = vault + "/"
    for file in new:
        with open(vault + file, "w") as f:
            f.write(new[file])

def get_notes(text: str):
    lines = text.split("\n")
    result = ""
    found = False
    for l in lines:
        if match(r">\s*\[!caution\]", l):
            found = True
            continue
        if found:
            if l.startswith("> "):
                result += l[2:]
            else:
                break

    if not found:
        return None
    else:
        return result

def populate_review(file:str, text: str, reviews: dict):
    n = get_notes(text)
    if n is not None:
        reviews[file] = n
    return reviews