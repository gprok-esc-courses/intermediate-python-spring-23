from Client import Client
from Item import Item
from Order import Order
from datetime import datetime


class Restaurant:
    def __init__(self):
        self.clients = {}
        self.items = {}
        self.orders = []

    def add_client(self, name, address, phone):
        # Check if phone is already in use
        if phone in self.clients:
            print("Phone is already in the system")
        else:
            client = Client(name, address, phone)
            self.clients[phone] = client
            print(client, " added.")

    def add_item(self, name, item_type, price):
        if name in self.items:
            print("Item already exists")
        else:
            item = Item(name, item_type, price)
            self.items[name] = item
            print(item, " added.")

    def add_order(self, phone):
        if phone not in self.clients:
            print("Customer does not exist")
        else:
            client = self.clients[phone]
            order = Order(client, datetime.now())
            while True:
                name = input("Item (- to exit): ")
                if name == '-':
                    break
                else:
                    if name in self.items:
                        q = int(input("Quantity: "))
                        order.add_item(self.items[name], q)
                    else:
                        print("Item", name, "not found")
            self.orders.append(order)

    def item_revenue(self, name):
        revenue = 0
        for o in self.orders:
            items = o.items
            for i in items:
                if i.name == name:
                    revenue = revenue + (i.price * items[i])
        return revenue

    def customer_payments(self, phone):
        payments = 0
        for o in self.orders:
            if o.client.phone == phone:
                payments = payments + o.total_price()
        return payments

    def display_catalog(self):
        print("CATALOG")
        for i in self.items:
            print(self.items[i])
        print("==================")


if __name__ == '__main__':
    r = Restaurant()
    r.add_client("aaa", "bbb", "1111")
    r.add_client("zzz", "ddd", "1111")

