from sys import path

import typer
from consts import *
import processing as p

app = typer.Typer()

@app.command()
def process_all(model: str = typer.Option(DEFAULT_MODEL, "--model", "-m")) -> None:
    if model not in MODEL_CONFIGS:
        print(model+" is not a configured model. Use another one.")
        return
    p.process_all(model)

@app.command()
def process(vault: str, model: str = typer.Option(DEFAULT_MODEL, "--model", "-m")) -> None:
    if model not in MODEL_CONFIGS:
        print(model+" is not a configured model. Use another one.")
        return
    p.process_indiv(vault, model)

@app.command()
def list_models() -> None:
    for model in MODEL_CONFIGS:
        print(f"{model}: {MODEL_CONFIGS[model]["llama-options"]["ctx-size"]}tk context")

@app.command()
def list_vaults() -> None:
    for v in VAULTS:
        print(f"{v}: {VAULTS[v]}")

@app.command()
def add_vault(name: str, path: str) -> None:
    VAULTS[name] = path
    with open("vaults.yaml", "w") as f:
        f.write(yaml.dump(VAULTS))

# TODO: add review command, change prompt to more parsable and make a list for latest edit

if __name__ == "__main__":
    app()
