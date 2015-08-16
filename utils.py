"""
Useful functions
"""
from math import sqrt
from collections import defaultdict


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


@memoize
def sieve(upto):
    """ The sieve algorithm to get all primes less than 'upto'
    """
    primes = [2]
    possibles = range(3, upto, 2)
    while primes[-1] < sqrt(upto):
        primes.append(possibles[0])
        possibles = [x for x in possibles if x % primes[-1]]

    return primes + possibles


@memoize
def pfactors(n):
    def pfactors_recur(n, primes):
        """ Returns a list of prime factors of n
        """
        for i in xrange(2, int(sqrt(n))+1):
            if n%i == 0:
                primes.append(i)
                return pfactors_recur(n/i, primes)

        if n > 1:
            primes.append(n)
            return primes
        else:
            return []

    return pfactors_recur(n, [])


@memoize
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


def sum_digits(num, func=lambda x: x):
    """Applies func to each digit in num and returns the sum
    """
    s = 0
    while num:
        s += func(num % 10)
        num /= 10

    return s


def map_occurrences(iterable):
    """returns a mapping of each item in iterable to the number of its
    occurences
    """
    occmap = defaultdict(int)
    for i in iterable:
        occmap[i] += 1

    return occmap


def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
