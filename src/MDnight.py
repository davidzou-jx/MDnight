import sys
from pathlib import Path
from sys import path

import json
import yaml
import typer
from consts import *
import processing as p

app = typer.Typer()

@app.command()
def process_all(model: str = typer.Option(DEFAULT_MODEL, "--model", "-m")) -> None:
    if model not in MODEL_CONFIGS:
        print(model+" is not a configured model. Use another one or add it in models.yaml.")
        sys.exit(1)
    p.process_all(model)

@app.command()
def process(vault: str, model: str = typer.Option(DEFAULT_MODEL, "--model", "-m")) -> None:
    if model not in MODEL_CONFIGS:
        print(model+" is not a configured model. Use another one or add it in models.yaml.")
        sys.exit(1)
    p.process_indiv(Path(vault), model)

@app.command()
def review(vault: str) -> None:
    vault = Path(vault)
    print("Vault: " + str(vault) + "\n")
    with open(vault / REVIEW_FILE, "r") as f:
        reviews = json.load(f)
    for r in reviews:
        print(r + ": ")
        print("\t" + reviews[r])


@app.command()
def list_models() -> None:
    for model in MODEL_CONFIGS:
        print(f"{model}: {MODEL_CONFIGS[model]["llama-options"]["ctx-size"]}tk context")

@app.command()
def list_vaults() -> None:
    for v in VAULTS:
        print(f"{v}: {str(VAULTS[v]["path"])}")

@app.command()
def add_vault(name: str, path: str) -> None:
    VAULTS[name]["path"] = Path(path)
    temp = {}
    for v in VAULTS:
        temp[v]["path"] = str(VAULTS[v]["path"])
        if "exclude" in VAULTS[v]:
            temp[v]["exclude"] = VAULTS[v]["exclude"]
    with open(VAULTS_FILE, "w") as f:
        f.write(yaml.dump(temp))

# TODO: add review command, change prompt to more parsable and make a list for latest edit

if __name__ == "__main__":
    app()
