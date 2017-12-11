# System

# Third-party

# Internal
from src.Item import Item

class TestItem(object):
    """ Class for testing Item """
    def __init__(self):
        pass
        
    def test_creation(self):
        item = Item("CF1")
        assert item.name == "Coffee"

    def test_coupons(self):
        coupon = "CHMK"
        item = Item("CF1")
        item.coupons.append(coupon)
        assert coupon in item.coupons
