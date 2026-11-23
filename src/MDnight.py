import typer
import processing as p

app = typer.Typer()


@app.command()
def process_all() -> None:
    p.process()

@app.command()
def process(vault: str) -> None:
    p.process_indiv(vault)

# TODO: add review command, change prompt to more parsable and make a list for latest edit

if __name__ == "__main__":
    app()
