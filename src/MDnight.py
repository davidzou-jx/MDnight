import typer
from consts import *
import processing as p

app = typer.Typer()

# TODO: more options

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

# TODO: add review command, change prompt to more parsable and make a list for latest edit

if __name__ == "__main__":
    app()
