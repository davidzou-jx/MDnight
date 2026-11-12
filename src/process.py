import os

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
    new = {}
    for file in old:
        new[file] = get_edited(old[file])
        # no need for context reset, llama is stateless and manages memory itself
    return new


def process():
    if not TESTING: start_server()
    edited = {}
    for vault in VAULTS:
        edited[vault] = process_vault(vault)
    end_server()
    # TODO: something for writing back into vaults
