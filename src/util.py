# System
import configparser
import pickle

# Third-party
from terminaltables import AsciiTable

# Internal

def generate_product_map(product_file):
    """ Format product information """
    raw_product_data = configparser.ConfigParser()
    raw_product_data.read(product_file)
    product_codes = raw_product_data.sections()
    product_data = {}
    for code in product_codes:
        product_data[code] = { 
            'name':raw_product_data[code]['name'],
            'price': raw_product_data[code]['price']
        }
    return product_data

def print_menu():
    """ Print Menu information """
    product_data = generate_product_map('product.ini')
    table_data = []
    tables_headers = ['Product Code', 'Name', 'Price']
    table_data.append(tables_headers)
    for code in product_data.keys():
        row = [code, product_data[code]['name'], "$" + product_data[code]['price']]
        table_data.append(row)
    table = AsciiTable(table_data=table_data)
    table.justify_columns[0] = 'center' # Justify codes center
    table.justify_columns[1] = 'left' # Justify coupons center
    table.justify_columns[2] = 'right'  # Justify prices right
    msg = "Welcome to Farmer Joe's Farmer's Market!\nWe have the following products for sale today:\n"
    msg += table.table
    return msg

def get_code(item):
    return "CODE"

def save_cart(cart):
    """ Save cart to Pickle """
    pickle.dump(cart, open("cart.p", "wb" ))

def load_cart():
    """ Load cart from Pickle """
    return pickle.load(open("cart.p", "rb" ))
