import numpy as np
import cv2

"""
    The height and width of the result can be specified here.
"""
HEIGHT = 100
WIDTH  = 100

"""
    primesfrom2to uses the sieve method to generate an array of prime numbers less than the given parameter n.
"""
def _primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

"""
    createMatrix creates a matrix containing the value 255 if the index is prime, else it contains 0.    
"""    
def _createMatrix(n):
    primes = _primesfrom2to(n)
    array = np.zeros(n)
    for i in primes:
        array[i] = 255
    return array.reshape(HEIGHT,WIDTH) 
    
"""
    createImage writes the matrix to a PNG image.
"""    
def _createImage(data):
    cv2.imwrite('primesArt.png',data)
    
"""
    This script creates a PNG image wherein every white pixel corresponds to a prime number.
"""    
if __name__ == '__main__':
    _createImage(_createMatrix(HEIGHT*WIDTH))