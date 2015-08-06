"""2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""
from fractions import gcd

def smallest_divisible(nmax=20):
    smallest = 1
    for i in range(1, nmax+1):
        if smallest % i:
            smallest *= i/gcd(i, smallest)

    return smallest
