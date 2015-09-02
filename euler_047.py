"""
The first two consecutive numbers to have two distinct prime factors
are:

14 = 2 x 7 15 = 3 x 5

The first three consecutive numbers to have three distinct prime
factors are:

644 = 2**2 x 7 x 23 645 = 3 x 5 x 43 646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime
factors. What is the first of these numbers?
"""
from utils import map_occurrences, pfactors


def uniqueprimes(n):
    return map_occurrences(pfactors(n)).keys()


def p47(nconsec=4, start=647):
    while start:
        filtered = filter(lambda n: len(uniqueprimes(n)) == nconsec,
                          xrange(start, start+nconsec))

        if len(filtered) == nconsec:
            return filtered[0]
        start += 1

