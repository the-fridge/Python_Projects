# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from random import sample
from random import shuffle

CODE_LENGTH = 3
MAX_DIGIT   = 10

class Secret_Code(object):
    def __init__(self):
        self._solved = False
        self._code = self._generate ()

    def _generate(self):
        code = [num for num in range(MAX_DIGIT)]
        return sample(code, CODE_LENGTH)

    def _get_matches(self, usr_list):
        match = 0
        for i in range(len(self._code)):
            if usr_list[i] == self._code[i]:
                match += 1
        return match

    def guess(self, usr_code):
        match    = 0

        usr_code = [int(c) for c in usr_code]
        match = self._get_matches(usr_code)

        if match == len(self._code):
            self._solved = True
            return 'Well done !'
        elif match > 0 :
            return 'Almost {} correct(s)'.format(match)
        else :
            return 'No match'

    def solved(self):
        return self._solved


def start_game() :
    guess_msg = 'Guess the {} digits of the code: '
    guess_msg = guess_msg.format(CODE_LENGTH)

    secret = Secret_Code()
    while not secret.solved():
        usr_code =  input(guess_msg)
        if len(usr_code) == CODE_LENGTH:
            print(secret.guess(usr_code))
        else:
            print('Bad length')

if __name__ == '__main__':
    start_game()
