# System
import configparser

# Third-party
import click
from terminaltables import AsciiTable

# Internal
from src.Cart import Cart

product_map = configparser.ConfigParser()
product_map.read('config.ini')
product_codes = product_map.sections()

def print_menu():
    table_data = []
    tables_headers = ['Product Code', 'Name', 'Price']
    table_data.append(tables_headers)
    for code in product_codes:
        row = [code, product_map[code]['name'], "$" + product_map[code]['price']]
        table_data.append(row)
    table = AsciiTable(table_data)
    print("Welcome to Farmer Joe's Farmer's Market!")
    print("We have the following products for sale today:")
    print(table.table)

def print_cart():
    print(cart.contents())

cart = Cart()
cart.add("AP1", 1)
cart.add("AP1", 2)
cart.add("AP1", 5)
cart.add("MK1", 1)
print_cart()
print_menu()

# print(product_codes)
# print(products['CH1']['NAME'])

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
# def run(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)