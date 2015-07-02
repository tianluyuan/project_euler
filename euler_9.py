"""
There exists exactly one Pythagorean triplet for which a + b + c =
1000.

Find the product abc.
"""


def pythagorean_triplet():
    """ Solve for a in terms of b and find combination that's integer
    """
    sum = 1000
    for a in range(1, sum):
        remainder = (500 - a)*1000 % (1000 - a)
        if remainder == 0:
            b = (500 - a)*1000 / (1000 - a)
            break
    
    c = sum - a - b
    return a*b*c
