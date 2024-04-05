# TODO description

# Word List from:
# https://github.com/charlesreid1/five-letter-words

# Project inspired by:
# https://realpython.com/python-wordle-clone/

import contextlib
import pathlib
import random
import re
import sys
import trie
from string import ascii_letters, ascii_uppercase

from rich.console import Console
from rich.theme import Theme

alpha_regex = re.compile('[^a-zA-Z]')
DEBUG_MODE = False


WORD_PATH = "wordlist.txt"


def checkChars(guess_word):
    return alpha_regex.sub('', guess_word)


def debug_print(s):
    if DEBUG_MODE:
        print(s)


class Wrdle:
    def __init__(self):
        self.WORD = "SNAKE"
        self.WORD_LIST = ["SNAKE"]
        self.GUESS_LIMIT_PLUS_ONE = 7  # one more than necessary
        self.WORD_LENGTH = 5
        self.guesses = ["_" * self.WORD_LENGTH] * (self.GUESS_LIMIT_PLUS_ONE - 1)
        self.LETTER_STATUS = {letter: letter for letter in ascii_uppercase}
        self.RECENT_WORDS = set()
        self.WORD_TRIE = trie.Trie()
        self.console = Console(width=40, theme=Theme({"warning": "red on yellow"}))
        self.refresh_page("Wrdle")

    def load_words(self, path: str):
        word_path = pathlib.Path(path)
        self.WORD_LIST = [
            word.upper()
            for word in word_path.read_text(encoding="utf-8").strip().split("\n")
        ]

        for w in self.WORD_LIST:
            self.WORD_TRIE.insert(w)

    def get_random_word(self):
        if not self.WORD_LIST or len(self.WORD_LIST) < 1:
            self.console.print("No valid words in the list", style="warning")
            raise SystemExit()
        word = random.choice(self.WORD_LIST)
        while word in self.RECENT_WORDS:
            word = random.choice(self.WORD_LIST)
        self.RECENT_WORDS.add(word)
        self.WORD = word

    def show_guesses(self):
        for guess in self.guesses:
            styled_guess = []
            for letter, correct in zip(guess, self.WORD):
                if letter == correct:
                    style = "bold white on green"
                elif letter in self.WORD:
                    style = "bold white on yellow"
                elif letter in ascii_letters:
                    style = "white on #666666"
                else:
                    style = "dim"
                styled_guess.append(f"[{style}]{letter}[/]")
                if letter != "_":
                    self.LETTER_STATUS[letter] = f"[{style}]{letter}[/]"
            self.console.print("".join(styled_guess), justify="center")
        self.console.print("\n" + "".join(self.LETTER_STATUS.values()), justify="center")

    def guess_word(self) -> str:
        guess = self.console.input("\nGuess word: ").upper()

        guess = checkChars(guess)

        if len(guess) != self.WORD_LENGTH:
            self.console.print(f"Your guess must be {self.WORD_LENGTH} letters.", style="warning")
            return self.guess_word()

        if guess in self.guesses:
            self.console.print(f"You've already guessed {guess}.", style="warning")
            return self.guess_word()

        if not self.WORD_TRIE.check_word_exists(guess):
            self.console.print(f"{guess} is not in the word list! Try again.")
            return self.guess_word()

        return guess

    def play(self):
        with contextlib.suppress(KeyboardInterrupt):
            while True:
                correct_guess = False
                self.get_random_word()
                debug_print(self.WORD)

                for guess_num in range(1, self.GUESS_LIMIT_PLUS_ONE):
                    self.refresh_page(headline=f"Guess {guess_num}")
                    self.show_guesses()
                    cur_guess = self.guess_word()

                    self.guesses[guess_num - 1] = cur_guess.upper()

                    if cur_guess == self.WORD:
                        correct_guess = True
                        break

                    self.show_guesses()

                self.game_over(correct_guess)

                stop_playing = input(f"\nWould you like to play again? (yes or no)\n").lower() == 'no'

                if stop_playing:
                    self.console.print("Thanks for playing!")
                    raise SystemExit
                else:
                    debug_print(self.RECENT_WORDS)
                    self.reset_game()

        self.game_over()

    def refresh_page(self, headline):
        self.console.clear()
        self.console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

    def game_over(self, guessed_correctly: bool = False):
        self.refresh_page(headline="Game Over")
        self.show_guesses()

        if guessed_correctly:
            self.console.print(f"\n[bold white on green]Correct, the word is {self.WORD}[/]")
        else:
            self.console.print(f"\n[bold white on red]Sorry, the word was {self.WORD}[/]")

    def reset_game(self):
        self.guesses = ["_" * self.WORD_LENGTH] * (self.GUESS_LIMIT_PLUS_ONE - 1)
        self.LETTER_STATUS = {letter: letter for letter in ascii_uppercase}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'd':
            print("Running in debug mode")
            DEBUG_MODE = True

    wrdle = Wrdle()
    wrdle.load_words(WORD_PATH)
    wrdle.play()
