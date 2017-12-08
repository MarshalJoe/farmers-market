# System
import uuid

# Third-party

# Internal

class Item(object):
    """ Simple class for tracking item information """
    def __init__(self, product_code, price):
        self.product_code = product_code
        self.price = price
        self.discounts = []
        self.coupons = []
        self.id = uuid.uuid4()
        