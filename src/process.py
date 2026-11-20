import os
from datetime import datetime as dt

from dotenv import load_dotenv
from openai import OpenAI

from consts import *
from server import *
from git_utils import *


def get_edited(text=None):
    if text is None: return None

    if TESTING: load_dotenv()
    client = OpenAI(base_url=f"http://localhost:{SERVER_PORT}/v1" if not TESTING else TEST_ENDPOINT,
                    api_key="" if not TESTING else os.getenv(TEST_KEY_NAME))
    model = client.models[0] if not TESTING else TEST_MODEL
    response = client.chat.completions.create(model=model, messages=[
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": text}])
    return str(response.choices[0].message.content)


def process_vault(vault, model="qwen9b"):
    old = get_text(vault)
    if vault[len(vault) - 1] is not "/": vault = vault + "/"
    # dont move before or else it breaks git diff
    make_commit(vault, COMMIT_STR + " before edits at " + dt.now().strftime("%Y-%m-%d"))
    for file in old:
        new = get_edited(old[file])
        with open(vault+file, "w") as f:
            f.write(new[file])
        # no need for context reset, llama is stateless and manages memory itself
    make_commit(vault, COMMIT_STR + " after edits at " + dt.now().strftime("%Y-%m-%d"))

def process():
    if not TESTING: start_server()
    for vault in VAULTS:
        process_vault(vault)
    end_server()

def write_back(vault, new):
    if vault[len(vault)-1] is not "/": vault = vault + "/"
    for file in new:
        with open(vault+file, "w") as f:
            f.write(new[file])