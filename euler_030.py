"""Find the sum of all the numbers that can be written as the sum of
fifth powers of their digits.
"""
def upper(nthpow):
    """Returns the upper limit that we should scan. This is because at
    some point adding an additional digit will mean larger than
    9**nthpow increase for any number
    """
    return nthpow * 9 ** nthpow


def dig_sum_pow(nthpow):
    """returns sum of numbers that can be written as sum of the nthpow of
    their digits
    """
    from functools import partial
    power = partial(pow, exponent=nthpow)
    return filter(lambda n: n == sum(map(power, map(int, str(n)))), xrange(2, upper(nthpow)))


def p30():
    return sum(dig_sum_pow(5))
