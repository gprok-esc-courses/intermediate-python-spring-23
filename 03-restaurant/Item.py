

class Item:
    def __init__(self, name, item_type, price):
        self.name = name
        self.type = item_type
        self.price = price

    def __str__(self):
        return self.name + " (" + self.type + ") price: " + str(self.price)


if __name__ == '__main__':
    item = Item("Arrabiata", "PASTA", 12.5)
    print(item)