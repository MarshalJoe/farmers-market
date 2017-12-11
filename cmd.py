# System
import configparser
import logging
from pathlib import Path

# Third-party
import click

# Internal
from src.Cart import Cart
from src.utils import print_menu, save_cart, load_cart, get_code
from src.validations import validate_quantity, validate_item

pickle_file = Path("cart.p")
if not pickle_file.is_file():
    print("Pickle 'cart.p' file does not exist! Creating one")
    file = open("cart.p","w+")
    cart = Cart()
    save_cart(cart)

config_file = Path("config.ini")
if not config_file.is_file():
    raise Exception("No config file detected! Please add a 'config.ini' ")

config = configparser.ConfigParser()
config.read("config.ini")

logging.basicConfig(filename=config['LOGGER']['PATH'], format='%(asctime)s %(message)s', level=logging.DEBUG)

@click.group()
def cart():
    """ Farmer's Market Help Page """
    pass

@cart.command()
@click.option('--quantity', default=1, help='Number of items to add to your cart (defaults to 1)')
@click.argument('item')
def add(quantity, item):
    """ Add item(s) to cart """
    logging.debug(f"Adding {quantity} {item} to your cart.")
    product_code = get_code(validate_item(item))
    cart = load_cart()
    cart.add(product_code, validate_quantity(quantity))
    save_cart(cart)
    click.echo(f"Added {quantity} {item} to your cart.")

@cart.command()
@click.option('--quantity', default=1, help='Number of items to remove from your cart (defaults to 1)')
@click.argument('item')
def remove(quantity, item):
    """ Remove item(s) from cart """
    logging.debug(f"Removing {quantity} {item} to your cart.")
    product_code = get_code(validate_item(item))
    cart = load_cart()
    cart.remove(product_code, validate_quantity(quantity))
    save_cart(cart)
    click.echo(f"Removed {quantity} {item} to your cart.")

@cart.command()
def print():
    """ Print cart contents """
    logging.debug(f"Printing cart contents.")
    cart = load_cart()
    if len(cart.items) != 0:
        click.echo(cart.print())
    else:
        click.echo("Your cart is empty! Try adding an item.")

@cart.command()
def empty():
    """ Empty cart """
    logging.debug("Emptying cart.")
    cart = Cart()
    save_cart(cart)
    click.echo("Emptied Cart")

@cart.command()
def deals():
    """ Show deals """
    logging.debug("Showing deals")
    click.echo("BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)")
    click.echo("APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.")
    click.echo("CHMK -- Purchase a box of Chai and get milk free. (Limit 1)")
    click.echo("APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples")

@cart.command()
def shop():
    """ Show products and prices """
    logging.debug("Showing menu / products")
    click.echo(print_menu())

if __name__ == '__main__':
    cart()