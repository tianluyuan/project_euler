"""
https://projecteuler.net/problem=6

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

def sum_square_diff(nmax=100):
    tot = 0
    for i in range(1, nmax+1):
        for j in range(1, i):
           tot += i*j

    return 2*tot
