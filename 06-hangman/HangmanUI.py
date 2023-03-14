from tkinter import Tk, Label, Text, Button, END
from HangmanModel import HangmanModel


class HangmanUI(Tk):
    def __init__(self):
        super().__init__()
        self.model = HangmanModel()
        self.secret_label = Label(self, text="")
        self.secret_label.grid(row=0, column=0)
        self.user_input = Text(self, width=5, height=1)
        self.user_input.grid(row=1, column=0)
        self.play_button = Button(self, text="Guess", command=self.check)
        self.play_button.grid(row=1, column=1)
        # EXERCISE: Add label to display win or lose
        # EXERCISE: Add  button to PLAY AGAIN

    def new_game(self):
        self.model.get_word()
        self.secret_label.configure(text=self.model.get_secret())

    def check(self):
        letter = self.user_input.get("1.0")
        print(letter)
        self.user_input.delete("1.0", END)
        self.model.play(letter)
        self.secret_label.configure(text=self.model.get_secret())
        # EXERCISE: Check Win or Lose and display in appropriate label


if __name__ == '__main__':
    ui = HangmanUI()
    ui.new_game()
    ui.mainloop()

