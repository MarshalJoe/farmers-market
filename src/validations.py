from click import BadParameter
from src.utils import generate_product_map

def validate_quantity(quantity):
    """ Ensure quantity is a positive integer """
    if quantity <= 0:
        raise BadParameter("Number of items must be an integer greater than zero")
    else:
        return quantity

def validate_item(item):
    """ Ensure item is a valid product name or code """
    product_data = generate_product_map('product.ini')
    product_codes = product_data.keys()
    product_names = []
    for code in product_codes:
        product_names.append(product_data[code]['name'])
    if item not in product_codes and item not in product_names:
        raise BadParameter(f"Item '{item}' not a valid product name or code")
    else:
        return item