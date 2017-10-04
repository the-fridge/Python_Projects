# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
from os import stat

import random
from random import randint

class Hangman_Game(object):
    def __init__(self):
        self._lifes = 5
        self._secret_word    = self._get_random()
        self._displayed_word = self._set_hidden()
        self._wrong_letters  = []

    def _check_win(self):
        displayed = [c for c in self._displayed_word]
        found = True
        for i in range(len(self._secret_word)):
            if self._secret_word[i] != displayed[i]:
                found = False
        if found:
            exit('\n\n** Well done ! **\n')


    def _get_random(self):
        total_bytes = stat('./dict.txt').st_size

        file = open('./dict.txt')
        file.seek(randint(0, total_bytes))
        file.readline()

        secret = [c for c in file.readline()]
        secret = secret[:-1]
        return ''.join(secret)

    def _set_hidden(self):
        clue = ''
        for i in range(len(self._secret_word)):
            clue += '_'
        return clue

    def get_clue (self):
        return self._displayed_word

    def guess(self, letter):
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
    game = Hangman_Game()
    while True:
        guess = '__'
        while len(guess) != 1:
            guess = input('\n------\nPlease input a letter: ')
            game.guess(guess)

if __name__ == '__main__':
    play()
