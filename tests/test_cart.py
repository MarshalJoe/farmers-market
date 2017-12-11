# System

# Third-party

# Internal
from src.Cart import Cart

class TestCart(object):
    """ Class for testing Cart """
    def __init__(self):
        self.cart = Cart()

    def test_total_1(self):
        """ Test first sample total """
        self.cart.add("CH1")
        self.cart.add("AP1")
        self.cart.add("CF1")
        self.cart.add('MK1')
        assert self.cart.total() == 20.34

    def test_total_2(self):
        """ Test second sample total """
        self.cart.add("AP1")
        self.cart.add('MK1')
        assert self.cart.total() == 10.75

    def test_total_3(self):
        """ Test third sample total """
        self.cart = Cart()
        self.cart.add("CF1", 2)
        assert self.cart.total() == 11.23

    def test_total_4(self):
        """ Test fourth sample total """
        self.cart = Cart()
        self.cart.add("AP1", 3)
        self.cart.add("CH1")
        assert self.cart.total() == 16.61

    def test_empty(self):
        """ Test that new cart is empty of items """
        assert len(self.cart.contents()) == 0

    def test_add(self):
        """ Test adding item """
        self.cart.add("AP1")
        assert len(self.cart.contents()) == 1

    def test_multiple_add(self):
        """ Test adding multiple items """
        self.cart.add("CH1")
        self.cart.add("AP1")
        self.cart.add("CF1")
        self.cart.add('MK1')
        total_1 = self.cart.total()
        self.cart.add("CF1")
        self.cart.add('MK1')
        self.cart.remove("CF1")
        self.cart.remove('MK1')
        total_2 = self.cart.total()
        total_3 = self.cart.total()
        assert total_1 == total_2 == total_3

    def test_remove(self):
        """ Test removing item """
        self.cart.add("AP1")
        self.cart.remove("AP1")
        assert len(self.cart.contents()) == 0

    def test_exists(self):
        """ Test item exist check """
        self.cart.add("AP1")
        number = self.cart.quantify("AP1")
        assert number == 1
        