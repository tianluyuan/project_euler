"""
The number, 197, is called a circular prime because all rotations of
the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from utils import (pfactors,
                   no_evens,
                   rotations)

def circular_primes(upto):
    """ Yields all circular primes up to upto
    """
    for num in range(2, upto):
        if num == 2:
            yield num

        if not no_evens(num):
            continue

        iscirc = True
        for rotated in rotations(num):
            if len(pfactors(rotated)) > 1:
                iscirc = False
                break

        if iscirc:
            yield num


def p35():
    return len(list(circular_primes(1000000)))

