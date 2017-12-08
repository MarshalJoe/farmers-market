# System

# Third-party

# Internal
from src.Cart import Cart
from src.util import generate_product_map

product_data = generate_product_map('product.ini')

def test_total_1():
    cart = Cart(product_data)
    cart.add("CH1", 1)
    cart.add("AP1", 1)
    cart.add("CF1", 1)
    cart.add('MK1', 1)
    assert cart.total() == 20.34

def test_total_2():
    cart = Cart(product_data)
    cart.add("AP1", 1)
    cart.add('MK1', 1)
    assert cart.total() == 10.75

def test_total_3():
    cart = Cart(product_data)
    cart.add("CF1", 2)
    assert cart.total() == 11.23

def test_total_4():
    cart = Cart(product_data)
    cart.add("AP1", 3)
    cart.add("CH1", 1)
    assert cart.total() == 16.61