import subprocess
from consts import *

global server


def construct_command(model=DEFAULT_MODEL):
    cmd = ["llama", "serve"]
    for opt in SERVER_CONFIGS:
        cmd.append("--" + opt)
        cmd.append(SERVER_CONFIGS[opt])
    for opt in MODEL_CONFIGS[model]["llama_options"]:
        cmd.append("--" + opt)
        cmd.append(MODEL_CONFIGS[model]["llama_options"][opt])
    return cmd


def start_server(model=DEFAULT_MODEL):
    cmd = construct_command(model)
    global server
    server = subprocess.Popen(cmd)


def end_server():
    server.terminate()
