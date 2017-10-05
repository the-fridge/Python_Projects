# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Pierre Bouillon

import os 
from os import stat

import random
from random import randint

class Hangman_Game(object):
    """ Hangman game

    Attributes:
        - _lifes : (int) life remaining before game over
        - _secret_word    : (str) word to guess
        - _displayed_word : (str) user display
        - _wrong_letters  : (char[]) letters not in the word
    """
    def __init__(self):
        self._lifes = 5
        self._secret_word    = self._get_random()
        self._displayed_word = self._set_hidden()
        self._wrong_letters  = []

    def _check_win(self):
        """ Check if the word is guessed

        Return:
            - True if _secret_word and _displayed_word are the same
        """
        displayed = [c for c in self._displayed_word]
        found = True
        for i in range(len(self._secret_word)):
            if self._secret_word[i] != displayed[i]:
                found = False
        if found:
            exit('\n\n** Well done ! **\n')


    def _get_random(self):
        """ Get a random word from a file
        """
        total_bytes = stat('./dict.txt').st_size

        file = open('./dict.txt')
        file.seek(randint(0, total_bytes))
        file.readline()

        secret = [c for c in file.readline()]
        secret = secret[:-1]
        return ''.join(secret)

    def _set_hidden(self):
        """ Build _displayed_word
        """
        clue = ''
        for i in range(len(self._secret_word)):
            clue += '_'
        return clue

    def guess(self, letter):
        """ Get the user letter and check if the word is guessed
        """
        correct = 0

        splitted_display = self._displayed_word.replace(' ','')
        splitted_display = [c for c in self._displayed_word]
        for i in range(len(self._secret_word)):
            if self._secret_word[i] == letter:
                splitted_display[i] = letter
                correct += 1
        self._displayed_word = ''.join(splitted_display)

        if correct == 0 :
            if letter not in self._wrong_letters:
                self._wrong_letters.append(letter)
            self._lifes -= 1
        else:
            self._check_win()

        if not self._lifes:
            msg = 'You loose.. The correct word was {}'
            msg = msg.format(self._secret_word)
            exit(msg)

        msg = '\n{}\n(lives: {} - letters: {}) Wrong letters: {}'
        msg = msg.format(
            self._displayed_word, 
            self._lifes, 
            len(self._displayed_word),
            str(self._wrong_letters))
        print(msg)


def play() :
    """ Start the hangman game
    """
    game = Hangman_Game()
    while True:
        guess = '__'
        while len(guess) != 1:
            guess = input('\n------\nPlease input a letter: ')
            game.guess(guess)

if __name__ == '__main__':
    play()
