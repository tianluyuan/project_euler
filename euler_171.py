#!/usr/bin/python

# Project euler #171
# find sum of all numbers n<10^20 such that the sum of digits squared is a perfect
# square
import copy
import math
import timeit

class Euler171:
    def __init__(self):
        self.n_digits = 10
        # sum over only the last sum_digits
        self.sum_digits = 4
        self.single_digit_squares = self.possibleperfectsquares(1)
        # perf_square targets we want to hit
        self.perf_squares = self.possibleperfectsquares(self.n_digits)
        self.sum_psquared = 0
        self.count = 0
        self.master_dict = {}
        self.sum_total = 0

    def possibleperfectsquares(self, n):
        ''' given n where n is the maximum number of digits, return
        a list of possible perfect squares
        '''
        psquare = []

        curr = 0
        while curr**2 <= (9**2)*n:
            psquare.append(curr**2)
            curr+=1

        return psquare

    def sum_psquaredigits(self,
                          n, 
                          num, 
                          psquares, 
                          iteration=0, 
                          possible=''):
        ''' given a max number of digits n and a number, return list of list of
        possible digits that satisfy their sum of squares equaling num

        possible is a list of possible numbers that add up to num
        '''
        # base case 
        if num==0:
            possible+='0'*(n-iteration)
            self.sum_psquared += int(possible)
            # only keep last n sum_digits
            self.sum_psquared = self.sum_psquared % 10**(self.sum_digits+1)
            return
        elif num < 0 or iteration >= n or num > 81*(n-iteration):
            return

        iteration+=1
        for square in psquares:
            temp = possible
            temp += str(int(math.sqrt(square)))
            self.sum_psquaredigits(n, num-square, psquares, iteration, temp)

    def count_psquaredigits(self,
                            n, 
                            num,
                            psquares,
                            iteration=0):
        ''' given a max number of digits n and a number, return list of list of
        possible digits that satisfy their sum of squares equaling num

        possible is a list of possible numbers that add up to num
        '''
        # base case     
        if num==0:
            self.count += 1
            return
        elif num < 0 or iteration >= n or num > 81*(n-iteration):
            return

        iteration+=1
        for square in psquares:
            self.count_psquaredigits(n, num-square, psquares, iteration)

    def create_count_dict(self):
        for i in range(self.perf_squares[-1]+1):
            self.count = 0
            self.count_psquaredigits(self.n_digits-self.sum_digits, i, self.single_digit_squares)

            self.master_dict[i] = self.count
    
    def main(self):
        self.create_count_dict()
        for a_square in self.perf_squares:
            for i in range(a_square):
                n_repeats = self.master_dict[i]
                self.sum_psquared = 0
                self.sum_psquaredigits(self.sum_digits, a_square - i, self.single_digit_squares)
                self.sum_total += n_repeats * self.sum_psquared
                self.sum_total = self.sum_total % 10**(self.sum_digits+1)
