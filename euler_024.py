"""What is the millionth lexicographic permutation of the digits 0, 1,
2, 3, 4, 5, 6, 7, 8 and 9?
"""
from math import factorial
from utils import nth_perm


def p24():
    return int(reduce(lambda x, y: x+y,
                      (map(str, nth_perm(int(1e6)-1, range(10))))))
