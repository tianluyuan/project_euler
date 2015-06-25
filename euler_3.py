"""
project-euler #3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def factors(n=600851475143):
    """ Returns a list of prime factors of n
    """
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0 and len(factors(i))==1:
            return [i]+factors(n/i)

    return [n]
