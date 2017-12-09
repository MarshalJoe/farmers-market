# System

# Third-party
import click

# Internal
from src.Cart import Cart
from src.util import print_menu

@click.command()
def run():
    cart = Cart()
    cart.add("CH1")
    cart.add("AP1")
    cart.add("CF1")
    cart.add('MK1')
    click.echo(cart.print())

if __name__ == '__main__':
    run()