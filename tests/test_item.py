# System

# Third-party

# Internal
from src.Item import Item

class TestItem(object):
    """ Class for testing Item """
    def __init__(self):
        self.item = Item("CF1")
        
    def test_creation(self):
        assert type(self.item.name).__name__ == "str"

    def test_coupons(self):
        coupon = "CHMK"
        self.item.coupon = coupon
        assert coupon == self.item.coupon

    def test_price(self):
        assert type(self.item.price).__name__ == "float"
