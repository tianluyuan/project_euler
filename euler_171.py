#!/usr/bin/python

# Project euler #171
# find sum of all numbers n<10^20 such that the sum of digits squared is a perfect
# square
#
# since we're summing over the last 9 digits, it's fruitful
# to divide the problem into two parts.  First count the multiplicities
# in the first 10 digits, second find the possible 9 digit numbers which
# when added to a combination of the first 10 digits produces a perfect
# square.  the total sum is then the multiplicity of that combination 
# times the sum of the possible 9 digit numbers.
import copy
import math
import timeit

class Euler171:
    def __init__(self):
        # number of digits we're concerned with
        self.n_digits = 19
        # sum over only the last sum_digits
        self.sum_digits = 9
        # the max that the first 10 digits can add up to
        self.max_count_int = 81*(self.n_digits-self.sum_digits)
        # a list of single digit squares [0..81]
        self.single_digit_squares = self.possibleperfectsquares(1)
        # perf_square targets we want to hit
        self.perf_squares = self.possibleperfectsquares(self.n_digits)
        # keep track of the sum of the last 9 digits
        self.sum_psquared = 0
        # keep track of the multiplicity of the first 10 digits
        self.count = 0
        # dict to keep track of count
        self.count_dict = {}
        # keep track of the total sum across all different possible
        # combinations of multiplicities
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
        for i in range(self.max_count_int+1):
            self.count = 0
            self.count_psquaredigits(self.n_digits-self.sum_digits, i, self.single_digit_squares)

            self.count_dict[i] = self.count
    
    def main(self):
        self.create_count_dict()
        for a_square in self.perf_squares:
            for i in range(a_square):
                # cannot make a_square if i is too big.  i.e. the max possible sum 
                # of squares for numbers of the length (n_digits-sum_digits) digits
                # is 81 * (n_digits-sum_digits).  e.g. if we're tryign to hit
                # ps = 1600, we cannot have the last nine digits sum to 1.
                if not self.count_dict.has_key(i):
                    continue

                n_repeats = self.count_dict[i]
                self.sum_psquared = 0
                self.sum_psquaredigits(self.sum_digits, a_square - i, self.single_digit_squares)
                self.sum_total += n_repeats * self.sum_psquared
                self.sum_total = self.sum_total % 10**(self.sum_digits)
