import configparser
from terminaltables import AsciiTable

def generate_product_map(product_file):
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
    product_data = generate_product_map('product.ini')
    table_data = []
    tables_headers = ['Product Code', 'Name', 'Price']
    table_data.append(tables_headers)
    for code in product_data.keys():
        row = [code, product_data[code]['name'], "$" + product_data[code]['price']]
        table_data.append(row)
    table = AsciiTable(table_data=table_data, title="Farmer Joe's Farmer's Market")
    msg = "Welcome to Farmer Joe's Farmer's Market!\nWe have the following products for sale today:\n"
    msg += table.table
    return msg