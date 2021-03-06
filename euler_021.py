"""Let d(n) be defined as the sum of proper divisors of n (numbers
less than n which divide evenly into n).  If d(a) = b and d(b) = a,
where a != b, then a and b are an amicable pair and each of a and b are
called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284
are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from utils import memoize, divisors


@memoize
def d(n):
    """ Sums proper divisors of n
    """
    return 0 if n<=1 else sum(divisors(n))-n


def amicables(upto):
    return [i for i in range(1, upto) if i == d(d(i)) and i != d(i)]


def p21():
    return sum(amicables(10000))

