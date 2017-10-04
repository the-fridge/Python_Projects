# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# authors: Syed Marwan Jamal / Pierre Bouillon

"""`whiletrue.py` never ending 
loop which prints black lines till the program is stopped
"""

if __name__ == '__main__':
    try:
        while True:
            print('\n')
    except KeyboardInterrupt:
        print('Ending the program')
