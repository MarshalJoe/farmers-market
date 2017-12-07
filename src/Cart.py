

class Cart(object):
    """ Simple class for implementing shopping cart functionality """
    def __init__(self, product_data):
        self.items = []
        self.discounts = []
        self.product_data = product_data

    def contents(self):
        """ Show cart contents """
        return self.items

    def total(self):
        """ Calculate cost of cart contents """
        print("Calculating total cart cost")
        
        total = 0
        for item in self.items:
            price = self.product_data[item['product_code']]['price']
            quantity = item['quantity']
            total += float(price) * quantity
        return total

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

    def remove(self, item, quantity):
        """ Remove item from cart """
        print(f"Removing {quantity} {item} from cart")
        
        if any(item_obj['product_code'] == item for item_obj in self.items):
            for index, entry in enumerate(self.items):
                if entry['product_code'] == item:
                    new_quantity = entry['quantity'] - quantity 
                    entry['quantity'] = new_quantity if new_quantity > 0 else self.items.pop(index)
        else:
            print("Item not found")
