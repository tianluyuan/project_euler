"""
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from utils import no_evens, is_prime, truncate, lazy_primes, every_pred
from itertools import islice, ifilter, dropwhile


def check(num):
    snum = str(num)
    return no_evens(snum[1:])


def truncatable_prime(prime):
    return all(is_prime(num) for num in truncate(prime))


def truncatable_primes():
    return islice(ifilter(every_pred(truncatable_prime, check),
                          dropwhile(lambda x: 10 > x, lazy_primes())),
                          11)


def p37():
    return sum(truncatable_primes())
