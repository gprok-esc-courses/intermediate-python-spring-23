import requests
import json


class HangmanModel:
    def __init__(self):
        self.word = ''
        self.wrong = []
        self.correct = []

    def get_word(self):
        response = requests.get('https://random-word-api.herokuapp.com/word')
        data = json.loads(response.text)
        print(data[0])
        self.word = data[0]

    def reset(self):
        # EXERCISE: This function will reset the game by
        # getting a new word, and emptying the correct and wrong listscd
        pass

    def get_secret(self):
        secret = self.word[0]
        for i in range(1, len(self.word)-1):
            if self.word[i] in self.correct:
                secret += self.word[i]
            else:
                secret += "_"
        secret += self.word[-1]
        return secret

    def play(self, letter):
        if letter in self.correct or letter in self.wrong:
            print("Letter already used")
        else:
            if letter in self.word:
                self.correct.append(letter)
            else:
                self.wrong.append(letter)

    def win(self):
        for letter in self.word[1:-1]:
            if letter not in self.correct:
                return False
        return True

    def lost(self):
        if len(self.wrong) == 6:
            return True
        else:
            return False


if __name__ == '__main__':
    hangman = HangmanModel()
    hangman.get_word()
    while True:
        print(hangman.get_secret())
        letter = input("Guess: ")
        hangman.play(letter)
        if hangman.win():
            print(hangman.word + " found!")
            break
        if hangman.lost():
            print("You are hanged ...")
            break

