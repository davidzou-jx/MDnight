import yaml
# for quick changes
oai = ("gpt-6-luna", "https://api.openai.com/v1")
ds = ("deepseek-flash", "https://api.deepseek.com")
gem = ("gemini-3.5-flash-lite", "https://generativelanguage.googleapis.com/v1beta/openai")  # or gemini-3.8-flash

CLOUD_TESTING = False
TEST_MODEL = gem[0]
TEST_ENDPOINT = gem[1]
TEST_KEY_NAME = "GEMINI_KEY"

MAIN_BRANCH = "main"
VAULTS = ["test_vault/"] # preferably with trailing slash
COMMIT_STR = "MDnight"

SERVER_PORT = 9931

DEFAULT_MODEL = "qwen9b"
WEIGHTS_BASE_PATH = "/Users/davidzjx/.cache/huggingface/hub/"
# note for configs, use full option names (the ones with --)
SERVER_CONFIGS = {
    "port": str(SERVER_PORT)
}
with open("models.yaml", "r") as f:
    MODEL_CONFIGS = yaml.safe_load(f.read())
with open("sysprompt.txt", "r") as f:
    PROMPT = f.read()