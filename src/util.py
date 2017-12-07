import configparser

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