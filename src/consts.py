TESTING = True

MAIN_BRANCH = "main"
VAULTS = ["/Users/davidzjx/Documents/Purdue Vault"]
COMMIT_STR = "MDnight"

DEFAULT_MODEL = "qwen27b"
WEIGHTS_BASE_PATH = "/Users/davidzjx/.cache/huggingface/hub/"
SERVER_CONFIGS = {
    "port": "9931",
}
MODEL_CONFIGS = {
    "qwen27b":{
        "weights": WEIGHTS_BASE_PATH+"models--ISTA-DASLab--Qwen3.8-27B-GSQ-RCO-GGUF/snapshots/d562806dbafae37109975e970aae91b43e73b440/Qwen3.8-27B-GSQ-RCO-IQ3_S.gguf",
        "llama_options": {
            "ctx-size": "16384",
            "parallel": "1",
            "flash-attn": "on",
            "cache-type-k": "q8_0",
            "cache-type-v": "q8_0",
        }
    },
    "qwen9b":{
        "weights": WEIGHTS_BASE_PATH+"models--unsloth--Qwen3.5-9B-GGUF/snapshots/3885219b6810b007914f3a7950a8d1b469d598a5/Qwen3.5-9B-UD-Q4_K_XL.gguf",
        "llama_options": {
            "ctx-size": "65536",
            "parallel": "1",
            "flash-attn": "on",
            "cache-type-k": "q8_0",
            "cache-type-v": "q8_0",
        }
    },
    "qwen2b":{
        "weights": WEIGHTS_BASE_PATH+"models--unsloth--Qwen3.5-2B-GGUF/snapshots/f6d5376be1edb4d416d56da11e5397a961aca8ae/Qwen3.5-2B-UD-Q8_K_XL.gguf",
        "llama_options": {
            "ctx-size": "131072",
            "parallel": "1",
            "flash-attn": "on",
            "cache-type-k": "q8_0",
            "cache-type-v": "q8_0",
        }
    }
}