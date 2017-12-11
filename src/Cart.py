# System

# Third-party
from terminaltables import AsciiTable

# Internal
from src.Item import Item

class Cart(object):
    """ Simple class for implementing shopping cart functionality """
    def __init__(self):
        self.items = []

    def apply_discounts(self):
        """ Apply discounts to cart contents """
        discounts = {
            "BOGO":None,
            "APPL":None,
            "CHMK":1,
            "APOM":1
        }

        if self.quantify("CF1") >= 2:
            for coffee in self.matching("CF1")[1::2]:
                if coffee.coupon != "BOGO":
                    coffee.discount = coffee.price
                    coffee.coupon = "BOGO"

        for item in self.items:
            if "APPL" in discounts and item.product_code == "AP1" and self.quantify("AP1") >= 3 and item.coupon != "APPL":
                item.discount = 1.50
                item.coupon = "APPL"
            if discounts["CHMK"] and item.product_code == "MK1" and self.exists("CH1") and item.coupon != "CHMK":
                item.discount = item.price
                item.coupon = "CHMK"
                discounts["CHMK"] = None
            if discounts["APOM"] and item.product_code == "AP1" and self.exists("OM1") and item.coupon != "APOM":
                item.discount = (item.price / 2)
                item.coupon = "APOM"
                discounts["APOM"] = None

    def contents(self):
        """ Return cart contents """
        self.apply_discounts()
        return self.items

    def print(self):
        """ Print cart contents """
        table_data = []
        tables_headers = ['Item', '            ', 'Price']
        border_row = ["----", "", "-----"]
        table_data.append(tables_headers)
        table_data.append(border_row)
        msg = ""
        for item in self.contents():
            row = [item.product_code, "", "{0:.2f}".format(item.price)]
            table_data.append(row)
            if item.discount:
                discount_row = ["", item.coupon, f"-{item.discount}"]
                table_data.append(discount_row)
        total_row = ["", "", "{0:.2f}".format(self.total())]
        table_data.append(total_row)
        table = AsciiTable(table_data=table_data)
        table.inner_column_border = False
        table.outer_border = False
        table.inner_heading_row_border = False
        table.inner_footing_row_border = True
        table.justify_columns[1] = 'center' # Justify coupons center
        table.justify_columns[2] = 'right' # Justify prices right
        msg += table.table
        return msg

    def exists(self, product_code):
        """ Check it item exists in cart """
        if any(item.product_code == product_code for item in self.items):
            return True

    def matching(self, product_code):
        """ Count the number of a given item in the cart """
        return [item for item in self.items if item.product_code == product_code]

    def quantify(self, product_code):
        """ Count the number of a given item type in the cart """
        return len(self.matching(product_code))

    def total(self):
        """ Calculate cost of cart contents """
        total = 0
        for item in self.contents():
            if item.discount:
                final = item.price - item.discount
            else:
                final = item.price
            total += final
        return total

    def add(self, product_code, quantity=1):
        """ Add item to cart """
        for number in range(quantity):
            item = Item(product_code)
            self.items.append(item)

    def remove(self, product_code, quantity=1):
        """ Remove item from cart """
        delete_indices = []
        removed = 0
        for index, item in enumerate(self.items):
            if item.product_code == product_code and removed < quantity:
                delete_indices.append(index)
                removed += 1
        for i in sorted(delete_indices, reverse=True):
            deleted = self.items.pop(i)
