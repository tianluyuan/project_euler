#!/usr/bin/python

# Project euler #171
# find sum of all numbers n<10^20 such that the sum of digits squared is a perfect
# square
import copy
import math
import timeit

n_digits = 20

def possibleperfectsquares(n):
    ''' given n where n is the maximum number of digits, return
    a list of possible perfect squares
    '''
    psquare = []
    
    curr = 0
    while curr**2 <= (9**2)*n:
        psquare.append(curr**2)
        curr+=1
        
    return psquare

master_list = []
single_digit_squares = possibleperfectsquares(1)
def psquaredigits(n, num, psquares=single_digit_squares, iteration=0, possible=[]):
    ''' given a max number of digits n and a number, return list of list of
    possible digits that satisfy their sum of squares equaling num

    possible is a list of possible numbers that add up to num
    '''
    # base case 
    if num==0:
        possible.extend([0]*(n-iteration))
        # print possible
        master_list.append(possible)
        return
    elif num < 0 or iteration >= n or num > 81*(n-iteration):
        return

    iteration+=1
    for square in psquares:
        temp = copy.copy(possible)
        temp.append(math.sqrt(square))
        psquaredigits(n, num-square, psquares, iteration, temp)
