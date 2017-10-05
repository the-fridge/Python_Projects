# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# authors: unknown / Pierre Bouillon

"""`random_game.py` is a small game
in which you have to find a combination of
CODE_LENGTH numbers
"""

import random
from random import sample
from random import shuffle

CODE_LENGTH = 3
MAX_DIGIT   = 10

class Secret_Code(object):
    """ Build and check a secret code
    """
    def __init__(self):
        self._solved = False
        self._code = self._generate ()

    def _generate(self):
        """ Generate the secret code

        Pick CODE_LENGTH numbers between 0 and MAX_DIGIT

        Returns:
            - : (int[]) A 3 digits code 
        """
        code = [num for num in range(MAX_DIGIT)]
        return sample(code, CODE_LENGTH)

    def _get_matches(self, usr_list):
        """ Parse list and compare it with the secret code

        Attribute:
            - usr_list : (int[]) the user input

        Returns:
            - match : (int) number of digits in the right place
        """
        match = 0
        for i in range(len(self._code)):
            if usr_list[i] == self._code[i]:
                match += 1
        return match

    def guess(self, usr_code):
        """ Compare the user code and the secret code

        convert the user code as a list and compare it
        pass its attribute _solved on true if everything match

        Arguments:
            - usr_code : (str) the input of the user

        Returns:
            - 'Well done' if everything match
            - 'Almost ! {} correct(s)' if not everything match
            - 'No match' if nothing match
        """
        match    = 0
        usr_code = [int(c) for c in usr_code]

        match = self._get_matches(usr_code)

        if match == len(self._code):
            self._solved = True
            return 'Well done !'
        elif match > 0 :
            return 'Almost ! {} correct(s)'.format(match)
        else :
            return 'No match'

    def solved(self):
        """ Getter for _solved

        Returns:
            - _solved : (bool) True if secret code is broken
        """
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
