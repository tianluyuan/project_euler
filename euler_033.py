"""The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""
from fractions import Fraction
from utils import map_occurrences


def cancel(num1, num2):
    """returns num1 and num2 both less the digits they had in common
    """
    num1str = str(num1)
    num2str = str(num2)
    common = set(num1str).intersection(set(num2str))
    if not common:
        return 0, 1

    num1map = map_occurrences(num1str)
    num2map = map_occurrences(num2str)
    for com in common:
        if com == '0':
            return 0, 1

        min_occ = min(num1map[com], num2map[com])
        num1str = num1str.replace(com, '', min_occ)
        num2str = num2str.replace(com, '', min_occ)

    if num1str and num2str and num2str != '0':
        return int(num1str), int(num2str)
    else:
        return 0, 1


def curious_fractions():
    """ returns a list of curious fractions
    """
    for numer in range(10, 100):
        for denom in range(numer+1, 100):
            if Fraction(numer, denom) == Fraction(*cancel(numer, denom)):
                yield Fraction(numer, denom)


def p33():
    from operator import mul
    return reduce(mul, curious_fractions()).denominator
