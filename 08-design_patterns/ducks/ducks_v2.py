from abc import ABC, abstractmethod


class Duck:
    def swim(self):
        print("Swimming ...")

    def display(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Quackable(ABC):
    @abstractmethod
    def quack(self):
        pass


class RedheadDuck(Duck, Flyable, Quackable):
    def display(self):
        print("REDHEAD")

    def fly(self):
        print("Redhead flying")

    def quack(self):
        print("Readhead says Quack")


class MallardDuck(Duck, Flyable, Quackable):
    def display(self):
        print("MALLARD")

    def fly(self):
        print("Mallard flying")

    def quack(self):
        print("Mallard says Quack")


class RubberDuck(Duck, Quackable):
    def display(self):
        print("RUBBER")

    def quack(self):
        print("Rubber says Squeak")


class DecoyDuck(Duck):
    def display(self):
        print("DECOY")

    def quack(self):
        pass


if __name__ == '__main__':
    ducks = []
    ducks.append(RedheadDuck())
    ducks.append(MallardDuck())
    ducks.append(RubberDuck())
    ducks.append(DecoyDuck())

    for duck in ducks:
        duck.display()
        duck.quack()
        duck.fly()


