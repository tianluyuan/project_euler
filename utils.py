"""
Useful functions
"""
from math import sqrt, factorial
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


def compose(*fns):
    """ Compose fn with any number of args
    """
    def helper(f, g):
        def wrapper(*args, **kwargs):
            return g(f(*args, **kwargs))
        return wrapper
    return reduce(helper, fns)


def every_pred(*fns):
    """ Returns true if all of fns returns true
    """
    def conjoined(*args, **kwargs):
        return all(fn(*args, **kwargs) for fn in fns)
    return conjoined


def any_pred(*fns):
    """ Returns true if any of fns returns true
    """
    def disjoined(*args, **kwargs):
        return any(fn(*args, **kwargs) for fn in fns)
    return disjoined


def lazy_primes():
    """ Get primes indefinitely, suboptimal algo
    """
    yield 2

    candidate = 3
    while True:
        if len(pfactors(candidate)) == 1:
            yield candidate
        candidate += 2


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


def is_prime(n):
    return len(pfactors(n)) == 1


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


def n_divisors(prime_factors):
    """use divisor (or tau) function since we have the prime
    factorization
    """
    occurences = map_occurrences(prime_factors)

    ndiv = 1
    for occ in occurences.itervalues():
        ndiv *= (occ+1)

    return ndiv


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


def no_evens(num):
    """ Returns True if num has no even perm
    """
    return all(int(d) % 2 for d in str(num))


def rotations(num):
    """ Yields all rotations of integer num
    """
    snum = str(num)
    for idx, sdig in enumerate(snum):
        yield int(snum[idx:] + snum[:idx])


def truncate(num):
    """ Yields truncated num from right and left
    e.g. 3787->378, 787, 37, 87, 3, 7
    """
    snum = str(num)
    yield num
    for idx in range(len(snum)-1):
        yield int(snum[:idx+1])
        yield int(snum[idx+1:])


def nth_perm(n, perm, reverse=False):
    """Returns the nth permutation of perm in lexicographic or reverse
    lexicographic order
    """
    perm.sort(reverse=reverse)
    if n == 0:
        return perm
    ndigs = len(perm)
    stride = factorial(ndigs-1)
    step_idx = n/stride
    perm[0], perm[step_idx] = perm[step_idx], perm[0]

    return [perm[0]] + nth_perm(n - step_idx*stride, perm[1:], reverse)


def sorted_perms(perm, reverse=False):
    """Yields possible permutations of a list perm sorted in
    lexicographic or reverse order. Lazy eval
    """
    for i in xrange(factorial(len(perm))):
        yield nth_perm(i, perm, reverse)


def load_words(filepath):
    """ Reads file into list
    """
    with open(filepath) as f:
        all_words = f.read()
        words = [word.strip('"') for word in all_words.split(',')]

    return words


def alpha_value(word):
    """ returns the alphabetical value for word
    """
    return sum((ord(ch)-ord('A')+1 for ch in word.upper()))


def triangle(n):
    return n*(n+1)/2


def is_trianglel(tn):
    return ((-1+sqrt(1+8*tn))/2).is_integer()


def pentagonal(n):
    return n*(3*n-1)/2


def is_pentagonal(pn):
    return ((1+sqrt(1+24*pn))/6).is_integer()


def hexagonal(n):
    return n*(2*n-1)


def is_hexagonal(hn):
    return ((1+sqrt(1+8*hn))/4).is_integer()
