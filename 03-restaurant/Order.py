
class Order:
    def __init__(self, client, date_time):
        self.client = client
        self.date_time = date_time
        self.items = {}

    def add_item(self, item, quantity):
        self.items[item] = quantity

    def total_price(self):
        price = 0
        for item in self.items:
            price = price + (item.price * self.items[item])
        return price


