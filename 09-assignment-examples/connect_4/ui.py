from tkinter import Tk, Frame, Button


class Model:
    def __init__(self):
        self.board = [['-']*7 for i in range(6)]
        self.player = 'R'

    def play(self, col):
        for r in range(5, -1, -1):
            if self.board[r][col] == '-':
                self.board[r][col] = self.player
                p = self.player
                self.player = 'Y' if self.player == 'R' else 'R'
                return r, col, p
        return -1, col, self.player


class Connect4UI:
    def __init__(self):
        self.model = Model()
        self.window = Tk()
        self.buttons = []
        self.frame = Frame(self.window)
        for row in range(6):
            buttons_row = []
            for col in range(7):
                b = Button(self.frame, text='-', command=lambda c=col: self.btn_clicked(c))
                buttons_row.append(b)
                b.grid(row=row, column=col)
            self.buttons.append(buttons_row)

        self.frame.grid(row=0, column=0)

    def start(self):
        self.window.mainloop()

    def btn_clicked(self, col):
        print("clicked", col)
        row, col, player = self.model.play(col)
        if row != -1:
            self.buttons[row][col].config(text=player)


if __name__ == '__main__':
    app = Connect4UI()
    app.start()
