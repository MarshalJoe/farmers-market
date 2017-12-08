# System

# Third-party
import click

# Internal
from src.Cart import Cart
from src.util import print_menu, print_cart

cart = Cart()
cart.add("CH1")
cart.add("AP1")
cart.add("CF1")
cart.add('MK1')

# print_menu()
print_cart(cart)

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
# def run(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)