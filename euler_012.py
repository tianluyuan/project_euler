"""
What is the value of the first triangle number to have over five hundred divisors?
"""
from utils import pfactors, n_divisors
from collections import defaultdict

def get_factors_quick(num, cache):
    if cache.has_key(num):
        return cache[num]
    else:
        factors = pfactors(num)
        cache[num] = factors
        return factors


def first_triangle_ndivisors_gt(min_divisors):
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


def p12():
    return first_triangle_ndivisors_gt(500)
