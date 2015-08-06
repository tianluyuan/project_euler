"""
What is the sum of the digits of the number 2**1000?
"""
def sum_digits(num=2**1000):
    return reduce(lambda x,y: int(x)+int(y), str(num))

