"""
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2x12 15 = 7 + 2x22 21 = 3 + 2x32 25 = 7 + 2x32 27 = 19 + 2x22
33 = 31 + 2x12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum
of a prime and twice a square?
"""
from utils import sieve, is_prime, every_pred
from math import sqrt
from itertools import ifilter, count


def notdecomposeable(odd):
    return not any(sqrt((odd - pr)/2.).is_integer() for pr in sieve(odd))


def p46():
    return ifilter(every_pred(lambda x: not is_prime(x), notdecomposeable),
                   count(33, 2)).next()
