"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not
include leading zeros.)
"""
from utils import is_palindrome


def is_palindrome_both(num):
    binnum = bin(num)[2:]
    return is_palindrome(num) and binnum == binnum[::-1]


def sum_palindromic(upto):
    return sum(num for num in xrange(upto) if is_palindrome_both(num))


def p36():
    return sum_palindromic(1000000)
