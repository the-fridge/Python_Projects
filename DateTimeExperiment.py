# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# authors: unknown / Pierre Bouillon

"""`DateTimeExperiment.py` prints
datetime through different functions
"""

import datetime
from datetime import datetime

def print_from_instance(now):
    """ Prints each attribute of the current datetime

    Argument:
        - now : (datetime) current datetime
    """
    msg = 'Current date and time using instance attributes:\n'
    msg+= '\tyear:   {}\n'
    msg+= '\tmonth:  {}\n'
    msg+= '\tday:    {}\n'
    msg+= '\thour:   {}\n'
    msg+= '\tminute: {}\n'
    msg+= '\tsecond: {}\n'
    msg+= '\tmicrosecond: {}\n'
    print (msg.format(
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute,
            now.second,
            now.microsecond
        ))

def print_from_strftime(now):
    """ Prints the current datetime with strftime

    Argument:
        - now : (datetime) current datetime
    """
    msg = 'Current date from strftime: {}\n'
    print (msg.format(now.strftime("%Y-%m-%d %H:%M")))

def print_object(now):
    """ Prints the current datetime raw

    Argument:
        - now : (datetime) current datetime
    """
    msg = 'Current date: {}\n'
    print (msg.format(now))


if __name__ == '__main__':
    now = datetime.now()

    print_object(now)
    print_from_instance(now)
    print_from_strftime(now)
