# !/usr/bin/env python3
# author: @alumyen
# Given a number x, print all permutations of [1,2,3,...,x]

import math
count = 0
def permute(a, p, l, r):
    if l == r:
        # p[count] = a
        print(a)
        global count
        count += 1
    else:
        for i in range(l, r+1):
            a_l = a[l]
            a_i = a[i]
            a[l] = a_i
            a[i] = a_l
            permute(a, p, l+1, r)
            a[l] = a_l
            a[i] = a_i                            

if __name__ == '__main__':
    x = input('Enter a number to which permutations are to be considered : ')
    x = int(x)
    a = []
    for i in range(1, x+1):
        a.append(i)
    
    p = [None]*math.factorial(len(a))
    permute(a, p, 0, len(a)-1)
