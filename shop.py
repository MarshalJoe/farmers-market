# System

# Third-party
import click

# Internal
from src.Cart import Cart
from src.util import print_menu, print_cart

@click.command()
def run():
    click.echo(print_menu())

if __name__ == '__main__':
    run()