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
    """ Add item to cart """
    item = get_code(item)
    click.echo(f"{quantity} {item}")

@cart.command()
@click.option('--quantity', default=1, help='Number of items to remove from your cart (defaults to 1)')
@click.argument('item')
def remove(quantity, item):
    """ Remove item from cart """
    click.echo(f"{quantity} {item}")

@cart.command()
def print():
    """ Print cart contents """
    cart = load_cart()
    click.echo(cart.print())

@cart.command()
def clear():
    """ Empty cart """
    click.echo("Emptied Cart")

@cart.command()
def deals():
    """ Show deals """
    click.echo("BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)")
    click.echo("APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.")
    click.echo("CHMK -- Purchase a box of Chai and get milk free. (Limit 1)")
    click.echo("APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples")

@cart.command()
def products():
    """ Show products and prices """
    click.echo(print_menu())

# @click.command()
# def run():
#     # cart = Cart()
#     # cart.add("CH1")
#     # cart.add("AP1")
#     # cart.add("CF1")
#     # cart.add('MK1')
#     # pickle.dump( cart, open("cart.p", "wb" ))
#     cart = load_cart()
#     cart.add('MK1')
#     save_cart(cart)
#     click.echo(cart.print())

if __name__ == '__main__':
    cart()