"""What is the millionth lexicographic permutation of the digits 0, 1,
2, 3, 4, 5, 6, 7, 8 and 9?
"""
from math import factorial

def nth_perm(n, perm):
    """ Returns the nth permutation of perm
    """
    perm.sort()
    if n == 0:
        return perm
    ndigs = len(perm)
    stride = factorial(ndigs-1)
    step_idx = n/stride
    perm[0], perm[step_idx] = perm[step_idx], perm[0]

    return [perm[0]] + nth_perm(n - step_idx*stride, perm[1:])


def p24():
    return int(reduce(lambda x, y: x+y,
                      (map(str, nth_perm(int(1e6)-1, range(10))))))
