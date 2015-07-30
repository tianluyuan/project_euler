"""
Find the sum of the digits in the number 100!
"""

def factorial_digit_sum(n=100):
    return sum(map(int, str(reduce(lambda x,y: int(str(x*y).strip('0')), xrange(1,n+1)))))

