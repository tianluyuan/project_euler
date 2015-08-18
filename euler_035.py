"""
The number, 197, is called a circular prime because all rotations of
the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from utils import (is_prime,
                   no_evens,
                   rotations,
                   lazy_primes,
                   every_pred)
from itertools import ifilter, takewhile


def is_circular(num):
    return all(is_prime(rotated) for rotated in rotations(num))


def no_evens2(num):
    return no_evens(num) or num == 2


def circular_primes(upto):
    return ifilter(every_pred(no_evens2, is_circular),
                   takewhile(lambda x: x < upto, lazy_primes()))


def p35():
    return len(list(circular_primes(1000000)))

