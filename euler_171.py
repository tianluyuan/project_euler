#!/usr/bin/python

# Project euler #171
# find sum of all numbers n<10^20 such that the sum of digits squared is a perfect
# square

n_digits = 20

def possibleperfectsquares(n):
    ''' given n where n is the maximum number of digits, return
    a list of possible perfect squares
    '''
    psquare = []
    
    curr = 1
    while curr**2 < (9**2)*n:
        psquare.append(curr**2)
        curr+=1
        
    return psquare

def psquaredigits(n, psquare):
    ''' given a max number of digits n and a perfect square, return list of list of
    possible digits that satisfy their sum of squares being a perfect square
    '''
