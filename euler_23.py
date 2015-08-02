"""A perfect number is a number for which the sum of its proper
divisors is exactly equal to the number. For example, the sum of the
proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""
import euler_21

def get_abundant(upto):
    for abd in range(upto+1):
        if sum(euler_21.divisors(abd))>2*abd:
            yield abd


def sum_no_two_abds(lower_limit=28123):
    """returns sum of all positive integers that cannot be written as sum
    of two abundant ints
    """
    two_abd = set([])

    abds = list(get_abundant(lower_limit))
    for idx, abd1 in enumerate(abds):
        for abd2 in abds[idx:]:
            abdsum = abd1 + abd2
            if abdsum > lower_limit:
                # break when above lower_limit because abds sorted
                break
            two_abd.add(abdsum)

    no_two_abd = set(range(1, lower_limit+1)) - two_abd
    return sum(no_two_abd)