import click
from tvmv.mover import Mover


@click.group()
def tvmv():
    pass


@tvmv.command()
@click.argument('source', type=click.Path(exists=True))
@click.argument('destination', type=click.Path(exists=True))
def move(source, destination):
    m = Mover(source, destination)
    m.move()


@tvmv.command()
@click.argument('source', type=click.Path(exists=True))
def ls(source):
    m = Mover(source, source)
    m.find_sources()
    for file in m.files:
        click.echo(file.filename)