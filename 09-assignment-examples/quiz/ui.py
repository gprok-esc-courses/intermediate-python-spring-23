from tkinter import Tk, Radiobutton, Frame, IntVar


class QuizUI:
    def __init__(self):
        self.window = Tk()
        self.frame = Frame(self.window)
        self.var = IntVar()
        self.selected = 0
        self.r1 = Radiobutton(self.frame, text='-', variable=self.var,
                              value=0, command=self.radio_action)
        self.r2 = Radiobutton(self.frame, text='-', variable=self.var,
                              value=1, command=self.radio_action)
        self.r3 = Radiobutton(self.frame, text='-', variable=self.var,
                              value=2, command=self.radio_action)
        self.r4 = Radiobutton(self.frame, text='-', variable=self.var,
                              value=3, command=self.radio_action)
        self.r1.grid(row=0, column=0)
        self.r2.grid(row=1, column=0)
        self.r3.grid(row=2, column=0)
        self.r4.grid(row=3, column=0)
        self.frame.grid(row=0, column=0)

    def start(self):
        self.window.mainloop()

    def radio_action(self):
        self.selected = self.var.get()
        print(self.var.get())


if __name__ == '__main__':
    app = QuizUI()
    app.start()