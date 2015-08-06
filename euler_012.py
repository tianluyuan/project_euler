"""
What is the value of the first triangle number to have over five hundred divisors?
"""
from utils import pfactors
from collections import defaultdict

def get_factors_quick(num, cache):
    if cache.has_key(num):
        return cache[num]
    else:
        factors = pfactors(num)
        cache[num] = factors
        return factors


def n_divisors(prime_factors):
    """use divisor (or tau) function since we have the prime
    factorization
    """
    occurences = defaultdict(int)
    for prime in prime_factors:
        occurences[prime] += 1

    ndiv = 1
    for occ in occurences.itervalues():
        ndiv *= (occ+1)

    return ndiv


def first_triangle_ndivisors_gt(min_divisors=500):
    tri = lambda x: x*(x+1)/2

    ndivisors = 1
    curr = 1
    factors_cache = {}
    while ndivisors <= min_divisors:
        curr += 1

        if curr % 2 == 0:
            prime_factors = (get_factors_quick(curr/2, factors_cache) +
                             get_factors_quick(curr+1, factors_cache))
        else:
            prime_factors = (get_factors_quick((curr+1)/2, factors_cache) +
                             get_factors_quick(curr, factors_cache))

        factors_cache[tri(curr)] = prime_factors

        ndivisors = n_divisors(prime_factors)

    return tri(curr)
