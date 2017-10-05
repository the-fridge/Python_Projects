# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# authors: Pranav Goel / Pierre Bouillon

"""`average_of_3_numbers.py` Takes three 
float numbers and returns their average
"""

if __name__ == '__main__':
    l = []
    l.append(float(input("Enter the first number: ")))
    l.append(float(input("Enter the second number: ")))
    l.append(float(input("Enter the third number: ")))
    average = sum(l) / len(l)
    print('Average is: {}'.format(average))
