from random import choice
from string import ascii_lowercase


class Guess:
    # sample consists of lowercase ascii and spaces."
    def __init__(self, sample="methinks it is like a weasel", score=0, guess=str()):
        self.__sample = sample
        self.__sample_length = len(self.__sample)
        self.__score = score
        self.__guess = guess

    def play(self, guess_one_by_one=False):
        while True:
            game_end = self._check_guess(guess_one_by_one=guess_one_by_one)
            print(self)
            if game_end:
                print("Bingo!")
                return

    def _get_guess(self, guess_one_by_one=False):
        self.__score += 1
        if guess_one_by_one:
            char_guess = self._get_random_char()
            if char_guess == self.__sample[len(self.__guess)]:
                self.__guess += char_guess
        else:
            self.__guess = "".join([self._get_random_char() for _ in range(self.__sample_length)])

    @staticmethod
    def _get_random_char():
        return choice(ascii_lowercase + " ")

    def _check_guess(self, guess_one_by_one=False):
        self._get_guess(guess_one_by_one=guess_one_by_one)
        return self.__sample == self.__guess

    def __str__(self):
        return f"score: {self.__score}, guess: {self.__guess}\n"
