#!/usr/bin/env python3
""" Determine remaining set of Wordle answers after guesses """

import click


class Wordle:
    def __init__(self, path='word_list.txt') -> None:
        self.words = self._get_word_list(path)

    @staticmethod
    def _get_word_list(path: str) -> list:
        words = []
        with open(path, 'r') as f:
            for line in f:
                words.append(line.rstrip())
        return words

    def update_words(self, guess: str, yellow_pos: str, green_pos: str) -> int:
        # Remove words with gray letters
        yellow = [guess[int(pos)-1] for pos in yellow_pos]
        green = [guess[int(pos)-1] for pos in green_pos]
        bad_letters = [letter for letter in guess if letter not in yellow and letter not in green]
        for word in reversed(self.words):
            for bl in bad_letters:
                if bl in word:
                    self.words.remove(word)
                    break

        # Remove answers with incorrect green letters
        for gp in green_pos:
            self._remove_green(guess[int(gp)-1], int(gp))

        # Remove answers without yellow letters
        for yp in yellow_pos:
            self._remove_yellow(guess[int(yp) - 1], int(yp))

        # Return remaining possible answers
        return len(self.words)

    def _remove_yellow(self, letter: str, pos: int) -> None:
        self.words = [word for word in self.words if letter in word and word[pos-1] != letter]

    def _remove_green(self, letter: str, pos: int) -> None:
        self.words = [word for word in self.words if word[pos-1] == letter]

    def print_words(self, batch=10):
        print(f'Final set size: {len(self.words)} words')
        c = 0
        while c < len(self.words):
            line = ''
            for x in range(batch):
                i = c + x
                if i >= len(self.words):
                    break
                line += f'{self.words[i]} '
            print(line)
            c += batch


@click.command()
@click.option('-f', '--filename', type=str, default='word_list.txt', help='File path to possible word answers')
@click.option('-b', '--batch', type=int, default=10, help='Number of possible answers per output row')
@click.option('-q', '--quiet', is_flag=True, help='Suppress the final word list')
def main(filename, batch, quiet):
    """Show remaining wordle possibilities"""
    w = Wordle(filename)

    word_count = []
    c = 1
    while c <= 6:
        # Gather guess data
        guess = input(f'Guessed word (word {c}) (empty to stop): ').lower()
        if not guess:
            break
        yellow = input(f'Yellow positions (word {c}): ').lower()
        green = input(f'Green positions (word {c}): ').lower()

        # Update possibilities
        word_count.append(w.update_words(guess, yellow, green))

        # Iterate word
        c += 1

    # Print choices after each guess
    for i, c in enumerate(word_count):
        if i == 0:
            print('')
        print(f'Possible answers after guess {i+1}: {c}')

    # Print remaining possible answers
    if not quiet:
        w.print_words(batch)


if __name__ == '__main__':
    main()

