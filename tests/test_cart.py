# System

# Third-party

# Internal
from src.Cart import Cart
from src.util import generate_product_map

def test_total_1():
    product_data = generate_product_map('product.ini')
    cart = Cart(product_data)
    cart.add("CH1", 1)
    cart.add("AP1", 1)
    cart.add("CF1", 1)
    cart.add('MK1', 1)
    assert cart.total() == 20.34

def test_total_2():
    product_data = generate_product_map('product.ini')
    cart = Cart(product_data)
    cart.add("AP1", 1)
    cart.add('MK1', 1)
    assert cart.total() == 10.75