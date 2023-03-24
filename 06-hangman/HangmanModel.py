import requests
import json


class HangmanModel:
    def __init__(self):
        self.word = ''
        self.wrong = []
        self.correct = []

    def get_word(self):
        """Generates a random word, retrieved from an API"""
        response = requests.get('https://random-word-api.herokuapp.com/word')
        data = json.loads(response.text)
        print(data[0])
        self.word = data[0]

    def reset(self):
        """Reset all variable to start a new game"""
        self.get_word()
        self.wrong = []
        self.correct = []

    def wrong_guesses(self):
        return len(self.wrong)

    def get_secret(self):
        """Converts the word to be presented to user with underscores in place of letters not found yet"""
        secret = self.word[0]  # get first letter
        for i in range(1, len(self.word)-1):  # loop from the 2nd to one before the last letter
            if self.word[i] in self.correct:  # if letter already guessed, add the letter
                secret += self.word[i]
            else:                             # else, add underscore
                secret += "_"
        secret += self.word[-1] # get the last letter
        return secret

    def play(self, letter):
        """Checks if letter is in the word and updates correct or wrong lists"""
        if letter in self.correct or letter in self.wrong:
            print("Letter already used")
        else:
            if letter in self.word:
                self.correct.append(letter)
            else:
                self.wrong.append(letter)

    def win(self):
        """Checks if every letter of the word (2nd to one before the last) is in the correct"""
        for letter in self.word[1:-1]:
            if letter not in self.correct:
                return False
        return True

    def lost(self):
        """Check if there are 6 letters in the wrong list"""
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

