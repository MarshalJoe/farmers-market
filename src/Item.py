
class Item(object):
    """ Simple class for tracking item information """
    def __init__(self, product_code, price):
        self.product_code = product_code
        self.price = price
        self.discount = None
        self.coupon = None
        self.id = 1

        