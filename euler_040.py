"""
An irrational decimal fraction is created by concatenating the
positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value
of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""
from itertools import takewhile, count


def step(x):
    return int(9*10**(x-1)*x)


def find_limit(pos):
   return list(takewhile(lambda x: step(x) < pos, count(0)))[-1]


def digit(pos):
    """returns the digit at position for the concatenated irrational
    decimal
    """
    limit = find_limit(pos)
    ndigits = sum(map(step, xrange(limit+1)))

    left = pos - ndigits
    (nnums, rem) = divmod(left-1, limit+1)
    posnum = nnums + 10**(limit)
    return int(str(posnum)[rem])


def p40():
    from operator import mul
    return reduce(mul, (map(digit, (10**n for n in xrange(7)))))

