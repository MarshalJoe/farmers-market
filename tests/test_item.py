# System

# Third-party

# Internal
from src.Item import Item

def test_creation():
    item = Item("CF1")
    assert item.name == "Coffee"
