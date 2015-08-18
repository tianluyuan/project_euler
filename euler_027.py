"""
   Find the product of the coefficients, a and b, for the quadratic
   expression that produces the maximum number of primes for consecutive
   values of n, starting with n = 0.
"""
from utils import pfactors, is_prime


def fns(a, b):
    """ yields n**2 + a*n + b for consec n=0, 1, 2, ... while prime
    """
    func = lambda n: n**2 + a * n + b

    n = 0
    while func(n)>1 and is_prime(func(n)):
        n += 1
        yield func(n)


def loop(absupto):
    """ We know that b must be prime and a must be odd
    """
    from utils import sieve
    possbs = sieve(absupto)
    max_consec = 0
    consec_ab = (0,0)
    for b in possbs:
        for a in range(-b, absupto, 2):
            length = len(list(fns(a,b)))
            if length > max_consec:
                max_consec = length
                consec_ab = (a, b)

    return max_consec, consec_ab


def p27():
    from operator import mul
    return reduce(mul, loop(1000)[1])
