"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192 192 x 2 = 384 192 x 3 = 576 By concatenating each
product we get the 1 to 9 pandigital, 192384576. We will call
192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2,
3, 4, and 5, giving the pandigital, 918273645, which is the
concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be
formed as the concatenated product of an integer with (1,2, ... , n)
where n > 1?
"""
from utils import sorted_perms


def sorted_pandigitals():
    for perm in sorted_perms(range(1,10), reverse=True):
        yield int(''.join(map(str, perm)))


def concatenatable(trial, num, step):
    """returns true if pandigital number satisfies criteria for this
    problem
    """
    if step*trial > num:
        return False

    numlen = len(str(num))
    triallen = len(str(step*trial))
    divideby = step*trial * 10**(numlen - triallen)
    (prin, rem) = divmod(num, divideby)
    if prin == 1 and rem == 0 and step > 1:
        return True

    if prin != 1 or str(num)[triallen:] != str(rem):
        return False

    return concatenatable(trial, rem, step+1)


def concatenatable_wrapper(num):
    idx = 1
    snum = str(num)
    trial = int(snum[0])
    while trial < num:
        if concatenatable(trial, num, 1):
            return True
        idx += 1
        trial = int(snum[:idx])

    return False


def p39():
    from itertools import islice, ifilter
    return islice(ifilter(concatenatable_wrapper, sorted_pandigitals()), 1).next()
