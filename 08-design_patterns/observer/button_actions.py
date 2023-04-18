from abc import ABC, abstractmethod
from tkinter import Tk, Button, Text, END


class ButtonObserver(ABC):
    @abstractmethod
    def act(self):
        pass


class DBAction(ButtonObserver):
    def act(self):
        print("Saving to database")


class EmailAction(ButtonObserver):
    def act(self):
        print("Sending email")


class PrintAction(ButtonObserver):
    def act(self):
        print("Printing")


class LogAction(ButtonObserver):
    def act(self):
        print("Updating log file")


class Window:
    def __init__(self):
        self.observers = []
        self.window = Tk()
        self.field = Text(self.window)
        self.button = Button(self.window, text="Click", command=self.action)
        self.field.grid(row=0, column=0)
        self.button.grid(row=1, column=0)

    def add_observer(self, observer):
        if isinstance(observer, ButtonObserver):
            self.observers.append(observer)
        else:
            print("Not added, this is not a ButtonObserver")

    def start(self):
        self.window.mainloop()

    def action(self):
        text = self.field.get("1.0", END)
        for observer in self.observers:
            observer.act()


class Cat:
    def act(self):
        print("Mieow")


if __name__ == '__main__':
    window = Window()
    window.add_observer(DBAction())
    window.add_observer(EmailAction())
    window.add_observer(PrintAction())
    window.add_observer(LogAction())
    window.add_observer(Cat())
    window.start()

