"""Find the sum of all the numbers that can be written as the sum of
fifth powers of their digits.
"""
def upper(nthpow):
    """Returns the upper limit that we should scan. This is because at
    some point adding an additional digit will mean larger than
    9**nthpow increase for any number
    """
    return nthpow * 9 ** nthpow


def solve(nthpow):
    """returns sum of numbers that can be written as sum of the nthpow of
    their digits
    """
    from functools import partial
    from utils import sum_digits
    power = partial(pow, exponent=nthpow)

    return filter(lambda n: n == sum_digits(n, power), xrange(2, upper(nthpow)))


def p30():
    return sum(solve(5))
