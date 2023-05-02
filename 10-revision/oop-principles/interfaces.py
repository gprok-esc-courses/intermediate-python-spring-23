from abc import ABC, abstractmethod


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Airplane(Flyable):
    def fly(self):
        print("Fly like an airplane")


class Bird(Flyable):
    def fly(self):
        print("Fly like a bird")


class Kite(Flyable):
    def fly(self):
        print("Fly like a kite")


class Simulation:
    def __init__(self):
        self.items = []

    def add_flying_item(self, s: Flyable):
        self.items.append(s)


if __name__ == '__main__':
    sim = Simulation()
    sim.add_flying_item(Bird())
    sim.add_flying_item(Airplane())
    sim.add_flying_item(Kite())

    for f in sim.items:
        f.fly()
