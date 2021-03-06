"""
Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The
first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their
difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum
and difference are pentagonal and D = |Pk - Pj| is minimised; what is
the value of D?
"""
from math import sqrt
from utils import pentagonal, is_pentagonal


def criteria(n,m):
    return (is_pentagonal(pentagonal(n)-pentagonal(m)) and
            is_pentagonal(pentagonal(n)+pentagonal(m)))


def p44():
    n = 2
    while True:
        for m in xrange(n-1, 0, -1):
            if criteria(n, m):
                return pentagonal(n)-pentagonal(m)

        n += 1
