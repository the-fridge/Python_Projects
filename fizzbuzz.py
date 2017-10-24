#!/usr/bin/env python3

"""
This program is the implementation of the famous fizzbuzz program.
If the number is divisible by both 3 and 5, then the progrma prints 'FizzBuzz'.
If the number is only divisible by 3, then the program prints 'Fizz'.
If the number is only divisible by 5, then the program prints 'Buzz'.
If the number is not divisible by 3 nor by 5 the programm prints the number.
"""
def fizz_buzz(num):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

for i in range(1, 101):
    fizz_buzz(i)

