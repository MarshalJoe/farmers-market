# System

# Third-party
import click

# Internal
from src.Cart import Cart
from src.util import generate_product_map, print_menu

print_menu()

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
# def run(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)