# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# authors: Syed Marwan Jamal / Pierre Bouillon

"""`Project2-annoying_while_loop.py` is a program with
an infinity loop
"""

if __name__ == '__main__':
    try:
        while True:
            print('Hello World')
    except KeyboardInterrupt:
        print('Ending the program')
