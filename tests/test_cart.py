# System

# Third-party

# Internal
from src.Cart import Cart

class TestCart(object):
    """ Class for testing Cart """
    def __init__(self):
        pass

    def test_total_1(self):
        """ Test first sample total """
        cart = Cart()
        cart.add("CH1")
        cart.add("AP1")
        cart.add("CF1")
        cart.add('MK1')
        assert cart.total() == 20.34

    def test_total_2(self):
        """ Test second sample total """
        cart = Cart()
        cart.add("AP1")
        cart.add('MK1')
        assert cart.total() == 10.75

    def test_total_3(self):
        """ Test third sample total """
        cart = Cart()
        cart.add("CF1", 2)
        assert cart.total() == 11.23

    def test_total_4(self):
        """ Test fourth sample total """
        cart = Cart()
        cart.add("AP1", 3)
        cart.add("CH1")
        assert cart.total() == 16.61

    def test_empty(self):
        """ Test that new cart is empty of items """
        cart = Cart()
        assert len(cart.contents()) == 0

    def test_add(self):
        """ Test adding item """
        cart = Cart()
        cart.add("AP1")
        assert len(cart.contents()) == 1

    def test_multiple_add(self):
        """ Test adding multiple items """
        cart = Cart()
        cart.add("CH1")
        cart.add("AP1")
        cart.add("CF1")
        cart.add('MK1')
        total_1 = cart.total()
        cart.add("CF1")
        cart.add('MK1')
        cart.remove("CF1")
        cart.remove('MK1')
        total_2 = cart.total()
        total_3 = cart.total()
        assert total_1 == total_2 == total_3

    def test_remove(self):
        """ Test removing item """
        cart = Cart()
        cart.add("AP1")
        cart.remove("AP1")
        assert len(cart.contents()) == 0

    def test_exists(self):
        """ Test item exist check """
        cart = Cart()
        cart.add("AP1")
        number = cart.quantify("AP1")
        assert number == 1
        