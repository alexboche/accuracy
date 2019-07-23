import click

from accuracy import app


@click.group()
def cli():
    "Console tools for voice accuracy."
    pass


@cli.command()
@click.argument("dictated_file", type=click.File())
@click.argument("correct_file", type=click.File())
def measure(dictated_file, correct_file):
    """Report accuracy statistics for dictated file."""
    result = app.compute_file_accuracy(dictated_file, correct_file)
    click.echo(round(result, 2))


if __name__ == "__main__":
    cli()
