

class Cart(object):
    """ Simple class for implementing shopping cart functionality """
    def __init__(self, product_data):
        self.items = []
        self.discounts = {
            "BOGO":None, 
            "APPL":None, 
            "CHMK":1, 
            "APOM":None
        }
        self.product_data = product_data

    def apply_discounts(self):
        """ Apply discounts to cart contents """
        for item in self.items:
            if "BOGO" in self.discounts and item['product_code'] == "CF1" and item['quantity'] >= 2:
                # Discount every other Coffee
                # if item['quantity'] % 2 == 0:
                #     item['discount'] = item['price'] / 2
                item['coupon'] = "BOGO"
            if "APPL" in self.discounts and item['product_code'] == "AP1" and item['quantity'] >= 3:
                item['discount'] = 1.50
                item['coupon'] = "APPL"
            if "CHMK" in self.discounts and item['product_code'] == "MK1" and any(item_obj['product_code'] == "CH1" for item_obj in self.items):
                item['discount'] = item['price']
                item['coupon'] = "CHMK"
            if "APOM" in self.discounts and item['product_code'] == "OM1" and any(item_obj['product_code'] == "AP1" for item_obj in self.items):
                print("OATMEAL!")

    def contents(self):
        """ Show cart contents """
        return self.items

    def total(self):
        """ Calculate cost of cart contents """
        print("Calculating total cart cost")
        
        self.apply_discounts()
        total = 0
        for item in self.items:
            print(item)
            price = item['price']
            quantity = item['quantity']
            discount = item['discount']
            cost = price * quantity
            if discount:
                final = cost - (float(discount) * quantity)
            else:
                final = cost
            total += final
            print(f"{item['product_code']} {quantity} X {price} = {cost}\nDiscount {discount}\nNew {final}")

        return total

    def add(self, item, quantity):
        """ Add item to cart """
        print(f"Adding {quantity} {item} to cart")
        
        if any(item_obj['product_code'] == item for item_obj in self.items):
            for entry in self.items:
                if entry['product_code'] == item:
                    entry['quantity'] += quantity
        else:
            price = self.product_data[item]['price']
            record = {'product_code':item, 'quantity': quantity, 'price': float(price), 'discount': None, 'coupon': None}
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
