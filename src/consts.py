import yaml
from pathlib import Path
# for quick changes
oai = ("gpt-6-luna", "https://api.openai.com/v1")
ds = ("deepseek-flash", "https://api.deepseek.com")
gem = ("gemini-3.5-flash-lite", "https://generativelanguage.googleapis.com/v1beta/openai")  # or gemini-3.8-flash

CLOUD_TESTING = False
TEST_MODEL = gem[0]
TEST_ENDPOINT = gem[1]
TEST_KEY_NAME = "GEMINI_KEY"


MAIN_GIT_BRANCH = "main"
COMMIT_STR = "MDnight"
VAULTS = {}

PROJECT_DIR = Path(__file__).resolve().parent.parent
VAULTS_FILE = PROJECT_DIR / "src" / "vaults.yaml"
MODELS_FILE = PROJECT_DIR / "src" / "models.yaml"
PROMPT_FILE = PROJECT_DIR / "src"/ "sysprompt.txt"
REVIEW_FILE = "notes.json"

SERVER_PORT = 9931

DEFAULT_MODEL = "qwen9b"
WEIGHTS_BASE_PATH = "/Users/davidzjx/.cache/huggingface/hub/"
# note for configs, use full option names (the ones with --)
SERVER_CONFIGS = {
    "port": str(SERVER_PORT)
}
with open(VAULTS_FILE, "r") as f:
    temp = yaml.safe_load(f.read())
    for v in temp:
        VAULTS[v]["path"] = Path(temp[v])
with open(MODELS_FILE, "r") as f:
    MODEL_CONFIGS = yaml.safe_load(f.read())
with open(PROMPT_FILE, "r") as f:
    PROMPT = f.read()