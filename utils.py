"""
Useful functions
"""
from math import sqrt


def hash_answer(answer):
    """ Returns the md5 hash for checking against answers here:
    http://kmkeen.com/local-euler/project_euler.txt
    """
    import hashlib
    md5 = hashlib.md5()
    md5.update(str(answer))
    return md5.hexdigest()


def memoize(f):
    """ Memoization decorator for functions taking one or more arguments.
    http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
    """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)


def sieve(upto):
    """ The sieve algorithm to get all primes less than 'upto'
    """
    primes = [2]
    possibles = range(3, upto, 2)
    while primes[-1] < sqrt(upto):
        primes.append(possibles[0])
        possibles = [x for x in possibles if x % primes[-1]]

    return primes + possibles


def pfactors(n, primes=None):
    """ Returns a list of prime factors of n
    """
    if primes is None:
        primes = []

    for i in xrange(2, int(sqrt(n))+1):
        if n%i == 0:
            primes.append(i)
            return pfactors(n/i, primes)

    if n > 1:
        primes.append(n)
        return primes
    else:
        return []


def divisors(n):
    """ divisors of n, not optimal
    """
    div = []
    for i in xrange(1, int(sqrt(n))+1):
        if n%i == 0:
            div.append(n/i)
            if n/i != i:
                div.append(i)
    return div


@memoize
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
