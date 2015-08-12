"""We shall say that an n-digit number is pandigital if it makes use
of all the digits 1 to n exactly once; for example, the 5-digit
number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9
pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.
"""
from itertools import permutations


def candidates():
    """yieldds a product that satisfies the 1-9 pandigital mult identity
    """
    digits = set(xrange(1,10))
    multiplier_len = [3, 4]
    for product in permutations(digits, 4):
        remaining = digits - set(product)
        p = int(''.join(map(str, product)))
        for mlen in multiplier_len:
            for multiplier in permutations(remaining, mlen):
                if multiplier > product:
                    continue
                mr = int(''.join(map(str, multiplier)))
                left = remaining - set(multiplier)
                for multiplicand in permutations(left):
                    md = int(''.join(map(str, multiplicand)))
                    if md*mr == p:
                        yield p


def p32():
    return sum(set(candidates()))
