"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def p7():
    from utils import lazy_primes
    from itertools import islice
    return list(islice(lazy_primes(), 10001))[-1]
