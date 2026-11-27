import subprocess
from consts import *

global server


def construct_command(model: str) -> list[str]:
    cmd = ["llama", "serve"]
    cmd.append("-m")
    cmd.append(MODEL_CONFIGS[model]["weights"])
    for opt in SERVER_CONFIGS:
        cmd.append("--" + opt)
        cmd.append(SERVER_CONFIGS[opt])
    for opt in MODEL_CONFIGS[model]["llama-options"]:
        cmd.append("--" + opt)
        cmd.append(MODEL_CONFIGS[model]["llama-options"][opt])
    return cmd


def start_server(model: str):
    cmd = construct_command(model)
    global server
    server = subprocess.Popen(cmd)


def end_server():
    global server
    server.terminate()
