"""
Find the sum of the digits in the number 100!
"""

def factorial_digit_sum(n=100):
    from math import factorial
    return sum(map(int, str(factorial(n))))

