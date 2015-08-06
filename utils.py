"""
Useful functions
"""
def hash_answer(answer):
    """ Returns the md5 hash for checking against answers here:
    http://kmkeen.com/local-euler/project_euler.txt
    """
    import hashlib
    md5 = hashlib.md5()
    md5.update(str(answer))
    return md5.hexdigest()


def sieve(upto):
    """ The sieve algorithm to get all primes less than 'upto'
    """
    from math import sqrt
    primes = [2]
    possibles = range(3, upto, 2)
    while primes[-1] < sqrt(upto):
        primes.append(possibles[0])
        possibles = [x for x in possibles if x % primes[-1]]

    return primes + possibles


def pfactors(n, primes=None):
    """ Returns a list of prime factors of n
    """
    from math import sqrt
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
