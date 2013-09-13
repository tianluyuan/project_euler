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
    def __init__(self, sum_digits=9):
        # number of digits we're concerned with
        self.n_digits = sum_digits*2+1
        # sum over only the last sum_digits
        self.sum_digits = sum_digits
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
        # keep track of sums already calculated
        self.sum_dict = {}

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

    def multiplicity(self, possible, last_square):
        ''' possible is a 9 digit number, last square is the last digit squared to
        make it a 10 digit number
        '''
        mult = 1
        for digit in possible:
            if str(int(math.sqrt(last_square))) != digit:
                mult+=1

        return mult

    def sum_psquaredigits(self,
                          n, 
                          num, 
                          psquares, 
                          last_square=0,
                          iteration=0, 
                          possible=''):
        ''' given a max number of digits n and a number, return list of list of
        possible digits that satisfy their sum of squares equaling num

        possible is a list of possible numbers that add up to num
        '''
        # base case 
        if num==0:
            possible+='0'*(n-iteration)
            self.count += self.multiplicity(possible, last_square)
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
            self.sum_psquaredigits(n, num-square, psquares, last_square, iteration, temp)

    def count_psquaredigits(self, num):
        for a_square in self.single_digit_squares:
            self.sum_psquaredigits(self.sum_digits, num-a_square, self.single_digit_squares, a_square)
    
    def main(self):
        for a_square in self.perf_squares:
            print 'current square', a_square
            for i in range(a_square+1):
                # create count_dict as necessary
                if not self.count_dict.has_key(i):
                    self.count = 0
                    self.count_psquaredigits(i)
                    print i, self.count

                    self.count_dict[i] = self.count

                n_repeats = self.count_dict[i]

                if n_repeats == 0:
                    continue

                if not self.sum_dict.has_key(a_square-i):
                    self.sum_psquared = 0
                    self.sum_psquaredigits(self.sum_digits, a_square - i, self.single_digit_squares)
                    self.sum_dict[a_square-i] = self.sum_psquared
                    this_sum = self.sum_psquared
                else:
                    this_sum = self.sum_dict[a_square-i]

                self.sum_total += n_repeats * this_sum
                self.sum_total = self.sum_total % 10**(self.sum_digits)
