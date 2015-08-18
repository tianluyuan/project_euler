""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
def p10():
    from utils import lazy_primes
    from itertools import takewhile
    return sum(takewhile(lambda x: x < 2e6,
                         lazy_primes()))
