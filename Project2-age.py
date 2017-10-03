# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# authors: Syed Marwan Jamal / Pierre Bouillon

"""`Project1-name.py` is a program that asks for the user's age
Then displays his age
Then asks for a amount of years `years` and displays the user's 
age when `years` years will be passed

"""

def initial_way ():
    """ asks the age, print it and print it in a few years

    Original code by Syed Marwan Jamal, using several `print()`
    """
    print('Hello')
    user_age = int(input('What is your age? \n'))
    print('Oh so your age is', user_age)
    years = int(input('Enter a number to know your age after that many years \n'))
    print('You will be',years+user_age, 'in', years ,'years')

def initial_way_2():
    """ asks the age, print it and print it in a few years

    Original code by Syed Marwan Jamal, using a variable to
    store the message and format it before display
    """
    user_age = int(input('Hello!\nWhat is your age? '))
    response = 'Oh so your age is {0}.'.format(user_age)
    print(response)
    years = int(input('Enter a number to know your age after that many years: '))
    print('You will be', years + user_age, 'in', years, 'years.')

def get_age_info():
    """ asks the age, print it and print it in a few years

    Remake of initial_way() by Pierre Bouillon
    """
    age   = input('Hello,\nPlease, write your age: ')
    years = input('Input a number to see your age in the future: ')
    print('---\nYour age is {} and you will be {} in {} years.\n---'
        .format(age, 
            int(age) + int(years), 
            years)
        )

def main() :
    """ Main function of the script

    Call the other functions
    """
    get_age_info()

if __name__ == '__main__':
    main()

