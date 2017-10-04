# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# authors: Pranav Goel / Pierre Bouillon

"""`random_house.py` is an implementation 
of the random function `choice` 
"""

import random
from random import choice

HOUSES = [
        'Bungalow',
        'Mansion',
        'Villa'
    ]

if __name__ == '__main__':
    msg = 'Greetings '
    msg+= input('Enter your name: ')
    msg+= ', you will have a {} when you grow up ! :)'
    print(msg.format(choice(HOUSES)))
