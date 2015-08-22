"""
An irrational decimal fraction is created by concatenating the
positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value
of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""
def digit(pos):
    """returns the digit at position for the concatenated irrational
    decimal
    """
    curr = 0
    l = 1
    while True:
        step = 9*10**(l-1)*l
        if curr + step > pos:
            break
        else:
            curr += step
            l += 1

    left = pos - curr
    (nnums, rem) = divmod(left-1, l)
    posnum = nnums + 10**(l-1)
    return int(str(posnum)[rem])


def p40():
    from operator import mul
    return reduce(mul, (map(digit, (10**n for n in xrange(7)))))

