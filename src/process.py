import os

from dotenv import load_dotenv
from openai import OpenAI

from consts import *


def process_text(text=None):
    if text is None: return None

    if TESTING: load_dotenv()
    client = OpenAI(base_url=f"http://localhost:{SERVER_PORT}/v1" if not TESTING else TEST_ENDPOINT,
                    api_key="" if not TESTING else os.getenv(TEST_KEY_NAME))
    model = client.models[0] if not TESTING else TEST_MODEL
    response = client.chat.completions.create(model=model, messages=[
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": text}])
    return str(response.choices[0].message.content)
