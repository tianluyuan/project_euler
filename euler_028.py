"""
Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:


It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
"""
def spiral_sum(size):
    """ sum = 1 + 4*(1+2*4)-2*6 + 4*(1+2*4+4*4)-4*6 ...
    reduceable to closed form using partial sums of i and i**2
    """
    if size % 2 == 0:
        raise RuntimeError('size must be odd!')

    n = size/2
    return 1 + 4*n + 10*(n**2+n) + 16*(n**3-n)/3


def p28():
    return spiral_sum(1001)

