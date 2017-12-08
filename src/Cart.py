# System

# Third-party

# Internal
from src.Item import Item

class Cart(object):
    """ Simple class for implementing shopping cart functionality """
    def __init__(self, product_data):
        self.items = []
        self.discounts = {
            "BOGO":None,
            "APPL":None,
            "CHMK":1,
            "APOM":1
        }
        self.product_data = product_data

    def apply_discounts(self):
        """ Apply discounts to cart contents """
        for item in self.items:
            # if "BOGO" in self.discounts and item['product_code'] == "CF1" and item['quantity'] >= 2:
            #     # Discount every other Coffee
            #     # if item['quantity'] % 2 == 0:
            #     #     item['discount'] = item['price'] / 2
            #     item['coupon'] = "BOGO"
            if "APPL" in self.discounts and item.product_code == "AP1" and self.quantify("AP1") >= 3:
                item.discounts.append(1.50)
                item.coupons.append("APPL")
            if self.discounts["CHMK"] and item.product_code == "MK1" and self.exists("CH1"):
                item.discounts.append(item.price)
                item.coupons.append("CHMK")
                self.discounts["CHMK"] = None
            if self.discounts["APOM"] and item.product_code == "AP1" and self.exists("OM1"):
                item.discounts.append((item.price / 2))
                item.coupons.append("APOM")
                self.discounts["APOM"] = None

    def contents(self):
        """ Return cart contents """
        return self.items

    def exists(self, product_code):
        if any(item.product_code == product_code for item in self.items):
            return True

    def quantify(self, product_code):
        matches = (item.product_code == product_code for item in self.items)
        return list(matches).count(True)

    def total(self):
        """ Calculate cost of cart contents """
        print("Calculating total cart cost")
        self.apply_discounts()
        total = 0
        for item in self.items:
            if len(item.discounts) > 0:
                final = item.price - sum(item.discounts)
            else:
                final = item.price
            total += final
            print(f"{item.product_code} ${item.price} = {item.price}\nDiscount {sum(item.discounts)}\nFinal {final}")
        print(f"Total:{total}")
        return total

    def add(self, product_code, quantity=1):
        """ Add item to cart """
        print(f"Adding {quantity} {product_code} to cart")
        for number in range(quantity):
            price = self.product_data[product_code]['price']
            item = Item(product_code, float(price))
            self.items.append(item)

    def remove(self, product_code, quantity):
        """ Remove item from cart """
        print(f"Removing {quantity} {product_code} from cart")
        delete_indices = []
        removed = 0
        for index, item in enumerate(self.items):
            if item.product_code == product_code and removed < quantity:
                delete_indices.append(index)
                removed += 1
        for i in sorted(delete_indices, reverse=True):
            deleted = self.items.pop(i)
            print(f"Deleted {deleted.product_code} id: {deleted.id}")
