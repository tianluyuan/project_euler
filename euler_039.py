"""
If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""
from math import sqrt
from utils import compose


def integral_triangle(a, b, p):
    c = p - (a+b)
    return a**2 + b**2 == c**2 


def triplets(p):
    """returns possible integral right triangle sides with
    perimeter p
    """
    for a in xrange(1, p/2+1):
        for b in xrange(a, p/2+1):
            if integral_triangle(a, b, p):
                yield (a, b, p-(a+b))


def p39():
    all_triplets = map(compose(triplets, list), xrange(2,1001))
    zipped = zip(map(len, all_triplets), all_triplets)
    return sum(max(zipped)[1][0])
