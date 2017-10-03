# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# authors: jalbertsr / Pierre Bouillon

"""`Project3-weeks_and_days(functions).py` is an implementation 
of three sorting algorithms with complexity 0(n^2) and the comparison 
of their execution time
"""

import random
from random import randint
import time
from time import time

def bubble_sort(array): 
    """ Bubble sort implementation

    Attributes:
        - array : (int[]) array of int to sort

    Returns:
        - array : (int[]) sorted numbers
    """
    for i in range(len(array)):
        for j in range(len(array)-1-i):
             if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
   
def insertion_sort(array):
    """ Insertion sort implementation

    Attributes:
        - array : (int[]) array of int to sort

    Returns:
        - array : (int[]) sorted numbers
    """
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array

def selection_sort(array):
    """ Selection sort implementation

    Attributes:
        - array : (int[]) array of int to sort

    Returns:
        - array : (int[]) sorted numbers
    """
    for slot in range(len(array)-1,0,-1):
        maxpos = 0
        for index in range(slot+1):
           if array[index] > array[maxpos]:
               maxpos = index
        temp = array[slot]
        array[slot] = array[maxpos]
        array[maxpos] = temp
    return array
        
def get_sort_time(sort, array):
    """ Sort an array and return the time for it

    Attribute:
        - sort  : (func)  sort used 
        - array : (int[]) array of int to sort

    Returns:
        - : (float) execution time of the function `sort`
    """
    t = time()
    sort(array)
    return time() - t

def get_random_array(size=50, start=0, end=200):
    """ Generate a random array of int

    Attributes:
        - size  : (int) size of the array
        - start : (int) smallest number that can be picked
        - end   : (int) biggest number that can be picked

    Returns:
        - : (int[]) an array of `size` int
    """
    return [randint(start, end) for x in range(size)]

def print_best_sort(algorithms):
    """ Print sort algorithms results

    Attributes:
        algorithms : (dict) values as {algorithm: execution time}
    """
    msg = 'Sorts order by efficiency:\n'

    results = sorted(algorithms.items(), key=lambda x:x[1])
    for result in results:
        msg += '\t {}: {:10f} seconds\n'.format(result[0], result[1])

    print(msg)

def print_results(algorithms):
    """ Print best sort algorithms regarding their execution time

    Attributes:
        algorithms : (dict) values as {algorithm: execution time}
    """
    for key in algorithms:
        msg = '{} sort algorithm:\n'
        msg+= 'Execution time: {:.10f} seconds\n'
        msg+= '===================================\n'
        print(msg.format(key, algorithms[key]))


if __name__ == '__main__':
    algorithms = {
            'Bubble':    get_sort_time(bubble_sort, get_random_array()), 
            'Insertion': get_sort_time(insertion_sort, get_random_array()), 
            'Selection': get_sort_time(selection_sort, get_random_array())
            }   
    print_results(algorithms)
    print_best_sort(algorithms)
