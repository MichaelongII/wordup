import click
import clipboard
from db_utils import *
from utils import *

@click.command()
@click.argument('name')
def add(name):
    click.echo('Adds password ' + name)

@click.command()
@click.argument('name')
def get(name):
    clipboard.copy("abc")
    click.echo('Puts password into clipboard')

@click.command()
@click.argument('name')
def delete(name):
    click.echo('Deletes a pw from db')

@click.command()
@click.argument('name', default="")
def gen(name):
    click.echo('Generates a pw for name')

@click.command()
def clear():
    clipboard.copy("")
    click.echo('Clears the clipboard')

@click.group()
def cli():
    pass


cli.add_command(add)
cli.add_command(get)
cli.add_command(delete)
cli.add_command(gen)
cli.add_command(clear)

if __name__ == '__main__':
    cli()
