"""
How many different ways can 200p be made using any number of coins?
"""
from utils import memoize


@memoize
def count_change(value, allowed_coins):
    """recursively break value into a set of equal or smaller coins
    """
    if value < 0:
        return 0
    if value == 0:
        return 1

    ways = 0
    for idx, coin in enumerate(allowed_coins):
        ways += count_change(value - coin, allowed_coins[idx:])

    return ways


def p31():
    coins = (200, 100, 50, 20, 10, 5, 2, 1)
    return count_change(200, coins)

