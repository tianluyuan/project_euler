"""
The nth term of the sequence of triangle numbers is given by, tn =
½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word
value. For example, the word value for SKY is 19 + 11 + 25 = 55 =
t10. If the word value is a triangle number then we shall call the
word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text
file containing nearly two-thousand common English words, how many are
triangle words?
"""
from utils import load_words, alpha_value
from math import sqrt, floor, ceil


def is_triangle(word):
    """A triangle number can be formed if we can factorize
    n**2+n+2*tn. This requires 2*tn to have divisors spaced 1 apart.
    """
    testval = 2*alpha_value(word)
    upper = ceil(sqrt(testval))
    lower = floor(sqrt(testval))

    return upper * lower == testval and upper != lower


def p42():
    words = load_words('resources/p042_words.txt')
    return len(filter(is_triangle, words))




