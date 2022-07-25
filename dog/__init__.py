#1 /usr/bin/env python3
import typer
import rich
app = typer.Typer()

@app.command()
def dog(file: str):
    with open(file) as f:
        rich.print(f.read())
