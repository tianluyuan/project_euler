"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""
def big_sum(upto):
    return sum((n**n for n in xrange(1, upto+1)))


def p48():
    return str(big_sum(1000))[-10:]

