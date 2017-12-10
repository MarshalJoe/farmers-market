# System

# Third-party

# Internal
from src.Cart import Cart
from src.utils import generate_product_map

product_data = generate_product_map('product.ini')

def test_total_1():
    cart = Cart()
    cart.add("CH1")
    cart.add("AP1")
    cart.add("CF1")
    cart.add('MK1')
    assert cart.total() == 20.34

def test_total_2():
    cart = Cart()
    cart.add("AP1")
    cart.add('MK1')
    assert cart.total() == 10.75

def test_total_3():
    cart = Cart()
    cart.add("CF1", 2)
    assert cart.total() == 11.23

def test_total_4():
    cart = Cart()
    cart.add("AP1", 3)
    cart.add("CH1")
    assert cart.total() == 16.61

def test_empty():
    cart = Cart()
    assert len(cart.contents()) == 0

def test_add():
    cart = Cart()
    cart.add("AP1")
    assert len(cart.contents()) == 1

def test_multiple_add():
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

def test_remove():
    cart = Cart()
    cart.add("AP1")
    cart.remove("AP1")
    assert len(cart.contents()) == 0

def test_exists():
    cart = Cart()
    cart.add("AP1")
    number = cart.quantify("AP1")
    assert number == 1