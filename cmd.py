# System

# Third-party
import click

# Internal
from src.Cart import Cart
from src.utils import print_menu, save_cart, load_cart, get_code

@click.group()
def cart():
    """ Farmer's Market Help Page """
    pass

@cart.command()
@click.option('--quantity', default=1, help='Number of items to add to your cart (defaults to 1)')
@click.argument('item')
def add(quantity, item):
    """ Add item(s) to cart """
    cart = load_cart()
    cart.add(item, quantity)
    save_cart(cart)
    click.echo(f"Added {quantity} {item} to your cart.")

@cart.command()
@click.option('--quantity', default=1, help='Number of items to remove from your cart (defaults to 1)')
@click.argument('item')
def remove(quantity, item):
    """ Remove item(s) from cart """
    cart = load_cart()
    cart.remove(item, quantity)
    save_cart(cart)
    click.echo(f"Removed {quantity} {item} to your cart.")

@cart.command()
def print():
    """ Print cart contents """
    cart = load_cart()
    if len(cart.items) != 0:
        click.echo(cart.print())
    else:
        click.echo("Your cart is empty! Try adding an item.")

@cart.command()
def empty():
    """ Empty cart """
    cart = Cart()
    save_cart(cart)
    click.echo("Emptied Cart")

@cart.command()
def deals():
    """ Show deals """
    click.echo("BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)")
    click.echo("APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.")
    click.echo("CHMK -- Purchase a box of Chai and get milk free. (Limit 1)")
    click.echo("APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples")

@cart.command()
def shop():
    """ Show products and prices """
    click.echo(print_menu())

if __name__ == '__main__':
    cart()