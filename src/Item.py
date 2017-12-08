# System
import uuid

# Third-party

# Internal
from src.util import generate_product_map

class Item(object):
    """ Simple class for tracking item information """
    def __init__(self, product_code):
        self.product_code = product_code
        self.product_data = generate_product_map("product.ini")
        self.price = float(self.product_data[product_code]['price'])
        self.name = self.product_data[product_code]['name']
        self.discounts = []
        self.coupons = []
        self.id = uuid.uuid4()
        