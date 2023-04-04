from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flying with wings")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("Not able to fly")


class FlyAsDrone(FlyBehavior):
    def fly(self):
        print("Flying as drone")


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


class Duck:
    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def swim(self):
        print("Swimming ...")

    def display(self):
        pass

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()



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
    r = RubberDuck()
    r.fly_behavior = FlyAsDrone()
    r.quack_behavior = Mute()
    ducks.append(RedheadDuck())
    ducks.append(MallardDuck())
    ducks.append(r)
    ducks.append(DecoyDuck())

    for duck in ducks:
        duck.display()
        duck.quack()
        duck.fly()


