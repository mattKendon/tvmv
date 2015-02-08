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
    m.find_sources()
    with click.progressbar(m.files) as files:
        for file in files:
            m.move_file(file)
    click.echo("Moved {0} files. Ignored {1} files.".format(m.moved, m.ignored))


@tvmv.command()
@click.argument('source', type=click.Path(exists=True))
def ls(source):
    m = Mover(source, source)
    m.find_sources()
    for file in m.files:
        click.echo(file.filename)