from abc import ABC, abstractmethod


# Fly Behavior classes

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flying with wings")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("No way to fly")


# Quack Behavior classes

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class Mute(QuackBehavior):
    def quack(self):
        print("...")


# Duck classes


class Duck:
    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def swim(self):
        print("Swimming ...")

    def display(self):
        pass


class RedheadDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())
        
    def display(self):
        print("REDHEAD")


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("MALLARD")


class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Squeak())

    def display(self):
        print("RUBBER")


class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Mute())

    def display(self):
        print("DECOY")


if __name__ == '__main__':
    ducks = []
    ducks.append(MallardDuck())
    ducks.append(RedheadDuck())
    ducks.append(RubberDuck())
    ducks.append(DecoyDuck())

    for duck in ducks:
        duck.display()
        duck.quack_behavior.quack()
        duck.fly_behavior.fly()
