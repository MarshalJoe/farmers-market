# System
import pickle

# Third-party
import click

# Internal
from src.Cart import Cart
from src.util import print_menu

@click.command()
@click.option('--cart_file', default='cart.p', help='Path to saved cart (pickle file)')
def run(cart_file):
    # cart = Cart()
    # cart.add("CH1")
    # cart.add("AP1")
    # cart.add("CF1")
    # cart.add('MK1')
    # pickle.dump( cart, open("cart.p", "wb" ))
    cart = pickle.load(open(cart_file, "rb" ))
    cart.add('MK1')
    pickle.dump( cart, open(cart_file, "wb" ))
    click.echo(cart.print())

if __name__ == '__main__':
    run()