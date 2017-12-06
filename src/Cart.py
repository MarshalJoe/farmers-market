

class Cart(object):
    """ Simple class for implementing shopping cart functionality """
    def __init__(self):
        self.items = []
        self.discounts = []

    def contents(self):
        """ Show cart contents """
        return self.items

    def add(self, item, quantity):
        """ Add item to cart """
        print(f"Adding {quantity} {item} to cart")
        
        if any(item_obj['product_code'] == item for item_obj in self.items):
            for entry in self.items:
                if entry['product_code'] == item:
                    entry['quantity'] += quantity
        else:
            record = {'product_code':item, 'quantity': quantity}
            self.items.append(record)
