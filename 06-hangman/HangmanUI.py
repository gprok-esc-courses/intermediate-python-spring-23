from tkinter import Tk, Label, Text, Button, END, Canvas
from HangmanModel import HangmanModel


class HangmanUI(Tk):
    def __init__(self):
        super().__init__()
        self.model = HangmanModel()
        self.canvas = Canvas(self, bg="white", width=400, height=400)
        self.canvas.grid(row=0, column=0)
        self.secret_label = Label(self, text="")
        self.secret_label.grid(row=1, column=0)
        self.user_input = Text(self, width=5, height=1)
        self.user_input.grid(row=2, column=0)
        self.play_button = Button(self, text="Guess", command=self.check)
        self.play_button.grid(row=3, column=0)
        # EXERCISE: Add label to display win or lose
        self.message = Label(self, text="")
        self.message.grid(row=4, column=0)
        # EXERCISE: Add  button to PLAY AGAIN
        self.play_again_button = Button(self, text="PLAY AGAIN", command=self.play_again)
        self.play_again_button.grid(row=5, column=0)

    def new_game(self):
        self.model.get_word()
        self.secret_label.configure(text=self.model.get_secret())

    def check(self):
        letter = self.user_input.get("1.0")
        print(letter)
        self.user_input.delete("1.0", END)
        self.model.play(letter)
        self.secret_label.configure(text=self.model.get_secret())
        self.draw_hangman()
        # EXERCISE: Check Win or Lose and display in appropriate label
        if self.model.win():
            self.message.configure(text="Congratulations! You found the word!")
            self.play_button["state"] = "disabled"
        if self.model.lost():
            self.message.configure(text="Sorry, you are hanged ...")
            self.play_button["state"] = "disabled"

    def play_again(self):
        self.play_button["state"] = "normal"
        self.model.reset()
        self.secret_label.configure(text=self.model.get_secret())
        self.message.configure(text="")
        self.canvas.delete("all")

    def draw_hangman(self):
        wrong = self.model.wrong_guesses()
        if wrong >= 1:
            # head
            self.canvas.create_oval(180, 80, 220, 120)
        if wrong >= 2:
            # body
            self.canvas.create_line(200, 120, 200, 200)
        if wrong >= 3:
            # leg left
            self.canvas.create_line(200, 200, 140, 260)
        if wrong >= 4:
            # leg right
            self.canvas.create_line(200, 200, 260, 260)
        if wrong >= 5:
            # hand left
            self.canvas.create_line(200, 160, 160, 140)
        if wrong == 6:
            # hand right
            self.canvas.create_line(200, 160, 240, 140)


if __name__ == '__main__':
    ui = HangmanUI()
    ui.new_game()
    ui.mainloop()

