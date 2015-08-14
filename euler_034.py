"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math
from utils import sum_digits


def curious_numbers():
    """yields all curious numbers. Upper bound can be found by taking a
    n-digit number, then the max sum of its factorials is n*9!. So we
    want to find the limit on n. This happens when 10**(n-1) > n*9!,
    or when n~=7.
    """
    for curr in range(3, 10**6):
        if curr == sum_digits(curr, math.factorial):
            yield curr


def p34():
    return sum(curious_numbers())

