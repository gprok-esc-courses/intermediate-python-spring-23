

class Duck:
    def quack(self):
        print("Quack")

    def swim(self):
        print("Swimming ...")

    def fly(self):
        print("Flying ...")

    def display(self):
        pass


class RedheadDuck(Duck):
    def display(self):
        print("REDHEAD")


class MallardDuck(Duck):
    def display(self):
        print("MALLARD")


class RubberDuck(Duck):
    def quack(self):
        print("Squeak")

    def fly(self):
        pass

    def display(self):
        print("RUBBER")


class DecoyDuck(Duck):
    def quack(self):
        pass

    def fly(self):
        pass

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
        duck.quack()
        duck.fly()
