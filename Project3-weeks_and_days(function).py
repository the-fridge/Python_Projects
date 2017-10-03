# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# authors: Syed Marwan Jamal / Pierre Bouillon

"""`Project3-weeks_and_days(functions).py` contains a function
that translate days into weeks and days
"""

def readable_timedelta(days):
    """ Display days in a human readable way

    original function by Syed Marwan Jamal

    Attributes:
        - days : (int) amount of day to translate

    Returns:
        - : (str) human readable string with date
    """
    number_of_weeks = days // 7  
    number_of_days  = days % 7
    return '{} week(s) and {} day(s)'.format(number_of_weeks, number_of_days)
   
def readable_timedelta_reworked(days):
    """ Display days in a human readable way

    reworked function by Pierre Bouillon

    Attributes:
        - days : (int) amount of day to translate

    Returns:
        - translation : (str)  human readable string with date
    """
    translation = '{} week(s) and {} day(s)'
    return translation.format(days // 7, days % 7)

if __name__ == '__main__':
    print(readable_timedelta(19))
    print(readable_timedelta_reworked(19))
