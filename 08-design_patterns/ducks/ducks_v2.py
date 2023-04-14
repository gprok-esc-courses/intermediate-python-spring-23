

class Duck:
    def swim(self):
        print("Swimming ...")

    def display(self):
        pass


class Flyable:
    def fly(self):
        pass


class Quackable:
    def quack(self):
        pass


class RedheadDuck(Duck, Flyable, Quackable):
    def display(self):
        print("REDHEAD")

    def fly(self):
        print("Flying ...")

    def quack(self):
        print("Quack")


class MallardDuck(Duck, Flyable, Quackable):
    def display(self):
        print("MALLARD")

    def fly(self):
        print("Flying ...")

    def quack(self):
        print("Quack")


class RubberDuck(Duck, Quackable):
    def quack(self):
        print("Squeak")

    def display(self):
        print("RUBBER")


class DecoyDuck(Duck):
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
        if not isinstance(duck, DecoyDuck):
            duck.quack()
        if isinstance(duck, MallardDuck) or isinstance(duck, RedheadDuck):
            duck.fly()
