import typer
from consts import *
import processing as p

app = typer.Typer()

# TODO: more options

@app.command()
def process_all() -> None:
    p.process_all(DEFAULT_MODEL)

@app.command()
def process(vault: str) -> None:
    p.process_indiv(vault, DEFAULT_MODEL)

# TODO: add review command, change prompt to more parsable and make a list for latest edit

if __name__ == "__main__":
    app()
