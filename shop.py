# System
import configparser

# Third-party
import click
from terminaltables import AsciiTable

# Internal
from src.Cart import Cart

def generate_product_map():
    raw_product_data = configparser.ConfigParser()
    raw_product_data.read('product.ini')
    product_codes = raw_product_data.sections()
    product_data = {}
    for code in product_codes:
        product_data[code] = { 
            'name':raw_product_data[code]['name'],
            'price': raw_product_data[code]['price']
        }
    return product_data

def print_menu(product_data):
    table_data = []
    tables_headers = ['Product Code', 'Name', 'Price']
    table_data.append(tables_headers)
    for code in product_data.keys():
        row = [code, product_data[code]['name'], "$" + product_data[code]['price']]
        table_data.append(row)
    table = AsciiTable(table_data)
    print("Welcome to Farmer Joe's Farmer's Market!\nWe have the following products for sale today:")
    print(table.table)

product_data = generate_product_map()
# print_menu(product_data)

# def print_cart():
#     print(cart.contents())

cart = Cart(product_data)
cart.add("AP1", 1)
cart.add("AP1", 2)
cart.add("AP1", 5)
cart.remove("AP1", 5)
cart.add("MK1", 1)
print(cart.total())

# print(product_codes)
# print(products['CH1']['NAME'])

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
# def run(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)