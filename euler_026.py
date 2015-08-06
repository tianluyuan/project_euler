"""Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
"""
def digit_divide(digit, d):
    n = 0
    while digit*10**n < d:
        n += 1

    return digit*10**n/d, digit*10**n%d


def recurring_length(d, digit=1, rems=None):
    """ Returns the recurring length of 1/d
    """
    div, rem = digit_divide(digit, d)
    if rem == 0:
        return 0

    if rems is None:
        rems = []

    if rem in rems:
        return len(rems) - rems.index(rem)

    rems.append(rem)
    return recurring_length(d, rem, rems)


def longest_recurring_d(upto=1000):
    longest = 0
    max_length = 0
    for d in range(2, upto):
        length = recurring_length(d)
        if length > max_length:
            max_length = length
            longest = d

    return longest
