# System

# Third-party

# Internal
from src.Item import Item

class TestItem(object):
    """ Class for testing Item """
    def __init__(self):
        self.item = Item("CF1")
        
    def test_creation(self):
        assert self.item.name == "Coffee"

    def test_coupons(self):
        coupon = "CHMK"
        self.item.coupons.append(coupon)
        assert coupon in self.item.coupons
