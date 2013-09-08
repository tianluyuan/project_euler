#!/usr/bin/python

# Project euler #172

import math
from operator import mul

n_digits = 18
max_reps = 3

## Going to use recursion so memoize results
def memoize(func):
    cache = {}
 
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
 
 
# Define Permutation
# assuming valid ranges
@memoize
def nPk(n, k):
    if k == 0:
        return 1
    return reduce(mul, range(n-k+1, n+1))
 
 
# Define Combination:
# assuming valid ranges
@memoize
def nCk(n, k):
    return nPk(n, k) / nPk(k, k)

def possibilities(n_digits_repeat_thrice):
    # number of digits that we can still use
    n_possible_digits = 10 - n_digits_repeat_thrice
    # number of digits remaining out of our n-digit number
    n_digits_remaining = n_digits-n_digits_repeat_thrice*max_reps
    # number of digits that rrepeat TWICE
    n_digits_repeat_twice_min = n_digits_remaining-n_possible_digits
    
    possible_repeating = nCk(10, n_digits_repeat_thrice)
    possible_perm = nPk(n_digits, n_digits)
    p = 0
    for i in range(n_digits_remaining/2+1):
        if i < n_digits_repeat_twice_min:
            continue
            
        n_digits_repeat_twice = i
        possible_remaining = nCk(n_possible_digits, n_digits_repeat_twice)*nCk(n_possible_digits-n_digits_repeat_twice, n_digits_remaining-2*n_digits_repeat_twice)
        if n_digits_repeat_thrice == 0:
            possible_perm_repeating = nPk(2, 2)**n_digits_repeat_twice
        elif n_digits_repeat_twice == 0:
            possible_perm_repeating = nPk(max_reps, max_reps)**n_digits_repeat_thrice
        else:
            possible_perm_repeating = (nPk(max_reps, max_reps)**n_digits_repeat_thrice)*(nPk(2, 2)**n_digits_repeat_twice)

        p += possible_repeating*possible_remaining*possible_perm/possible_perm_repeating

    return p

count = 0
for i in range(n_digits/max_reps+1):
    count += possibilities(i)

print count*9/10
