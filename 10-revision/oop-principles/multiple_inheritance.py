# Be careful with multiple inheritance


class Animal:
    def eat(self):
        print("Animal is eating")


class Bird:
    def eat(self):
        print("Bird is eating")


class Penguin(Animal, Bird):
    def __init__(self):
        self.type = "Penguin"


class SouthPolePenguin(Penguin, Bird):
    pass


if __name__ == '__main__':
    p = SouthPolePenguin()
    p.eat()
