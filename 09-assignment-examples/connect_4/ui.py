from tkinter import Tk, Frame, Button


class Connect4UI:
    def __init__(self):
        self.buttons = []
        self.window = Tk()
        self.frame = Frame(self.window)
        for row in range(6):
            for col in range(7):
                b = Button(self.frame, text='-', command=lambda c=col: self.btn_clicked(c))
                self.buttons.append(b)
                b.grid(row=row, column=col)
        self.frame.grid(row=0, column=0)

    def start(self):
        self.window.mainloop()

    def btn_clicked(self, col):
        print(str(col) + " clicked")


if __name__ == '__main__':
    app = Connect4UI()
    app.start()
