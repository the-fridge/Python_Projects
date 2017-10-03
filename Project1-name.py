# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# authors: Syed Marwan Jamal / Pierre Bouillon

"""`Project1-name.py` is a program that asks for the user name
Then it print the given name, and the lenght of this name.
"""

def initial_way ():
	""" asks the name, print it with its lenght

	Original code by Syed Marwan Jamal, using several `print()`
	"""
	print('Hello')
	user_name = input('What is your name?\n')
	print('It\'s nice to meet you', user_name)
	print('Length of your name is:')
	print(len(user_name))

def initial_way_2():
	""" asks the name, print it with its lenght

	Original code by Syed Marwan Jamal, using a variable to
	store the message and format it before display
	"""
	print('Hello')
	user_name = input('What is your name?\n').
	name_size = len(user_name)
	msg = 'It\'s nice to meet you {0}!\nThe length of your name is: {1}'
			.format(user_name, name_size)
	print(msg)

def get_name_info():
	""" asks the name, print it with its lenght

	Remake of initial_way() by Pierre Bouillon
	"""
	name = input('Hello,\nPlease, write your name: ')
	print('---\nPlease to meet you {}. You name is {} char(s) long.\n---'
		.format(name, len(name)))


def main() :
	""" Main function of the script

	Call the other functions
	"""
    get_name_info()
    initial_way()
    initial_way_2()


if __name__ == '__main__':
    main()

