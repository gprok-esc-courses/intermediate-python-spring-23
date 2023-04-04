from abc import ABC, abstractmethod


class Duck:
    def quack(self):
        print("Quack")

    def swim(self):
        print("Swimming ...")

    def display(self):
        pass

    def fly(self):
        print("Flying ...")


class RedheadDuck(Duck):
    def display(self):
        print("REDHEAD")


class MallardDuck(Duck):
    def display(self):
        print("MALLARD")


class RubberDuck(Duck):
    def display(self):
        print("RUBBER")

    def fly(self):
        pass

    def quack(self):
        print("Squeak")


class DecoyDuck(Duck):
    def display(self):
        print("DECOY")

    def fly(self):
        pass

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


