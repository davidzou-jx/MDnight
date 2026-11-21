# for quick changes
oai = ("gpt-6-luna", "https://api.openai.com/v1/responses")
ds = ("deepseek-flash", "https://api.deepseek.com")
gem = ("gemini-3.5-flash-lite", "https://generativelanguage.googleapis.com")  # gemini-3.8-flash

TESTING = True
TEST_MODEL = gem[0]
TEST_ENDPOINT = gem[1]
TEST_KEY_NAME = "GEMINI_KEY"

MAIN_BRANCH = "main"
VAULTS = ["/Users/davidzjx/Documents/Purdue Vault/"] # preferably with trailing slash
COMMIT_STR = "MDnight"

SERVER_PORT = 9931

DEFAULT_MODEL = "qwen27b"
WEIGHTS_BASE_PATH = "/Users/davidzjx/.cache/huggingface/hub/"
SERVER_CONFIGS = {
    "port": str(SERVER_PORT)
}
MODEL_CONFIGS = {
    "qwen27b": {
        "weights": WEIGHTS_BASE_PATH + "models--ISTA-DASLab--Qwen3.8-27B-GSQ-RCO-GGUF/snapshots/d562806dbafae37109975e970aae91b43e73b440/Qwen3.8-27B-GSQ-RCO-IQ3_S.gguf",
        "llama_options": {
            "ctx-size": "16384",
            "parallel": "1",
            "flash-attn": "on",
            "cache-type-k": "q8_0",
            "cache-type-v": "q8_0",
        }
    },
    "qwen9b": {
        "weights": WEIGHTS_BASE_PATH + "models--unsloth--Qwen3.5-9B-GGUF/snapshots/3885219b6810b007914f3a7950a8d1b469d598a5/Qwen3.5-9B-UD-Q4_K_XL.gguf",
        "llama_options": {
            "ctx-size": "65536",
            "parallel": "1",
            "flash-attn": "on",
            "cache-type-k": "q8_0",
            "cache-type-v": "q8_0",
        }
    },
    "qwen2b": {
        "weights": WEIGHTS_BASE_PATH + "models--unsloth--Qwen3.5-2B-GGUF/snapshots/f6d5376be1edb4d416d56da11e5397a961aca8ae/Qwen3.5-2B-UD-Q8_K_XL.gguf",
        "llama_options": {
            "ctx-size": "131072",
            "parallel": "1",
            "flash-attn": "on",
            "cache-type-k": "q8_0",
            "cache-type-v": "q8_0",
        }
    }
}

PROMPT = """This is a note written in Obsidian-flavored markdown. Assume all relevant markdown features are available.
It is written quickly, and is likely full of abbreviations, shorthands, and grammar, and structural mistakes.
Your task is to edit this text to be more pleasant to read.

You **should**:
- Capitalize appropriately. This should be done all over the note, even if otherwise instructed to retain the original
- Expand obvious shorthands and abbreviations, unless they are commonly used in abbreviate form, or there is no obvious replacement. For example:
    - "bc" should become"because"
    - "tday" should become "today"
    - "u" should become "you"
    - Keep "etc.", "et al.", or "nov" as they are
- Fix grammar and capitalization mistakes. However, do not expand sentence fragments into full sentences
    - Insert apostrophes into "howd", "youre", "didnt", etc.
    - Reword sentences to be grammatically correct.
        - Keep the text to a similar length and structure, but fix grammatical mistakes if they make reading awkward
- Correct typos and spelling mistakes. Do not correct anything with a capital letter, as it is likely a name or specific term
- Update the document structure. If certain sections obviously belong under another, edit the heading to conform to the hierarchy
    
You **should not**:
- Make factual corrections to any apparently incorrect information
- Add or remove content or knowledge from the note
 
Outside the reasoning block, the output should only contain the edited text.
"""
