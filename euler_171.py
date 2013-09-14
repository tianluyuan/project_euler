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
#
# It is possible to write an algorithm that efficiently does both parts.  We
# store the 9-digit sums and their multiplicities in two dictionaries with keys
# corresponding to the the sum of squares of digits.  The mult-dictionary can then
# be used to caculate teh 10-digit multiplicities, and the sum-dictionary gives us
# all 9-digit sums
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
        # create lookup dictionary for digit squared
        # with strings as keys and dict for keeping trakc of the differences
        # this will ensure we don't have to loop through every
        # number, just add from lookup-dict
        self.squares_lookup_dict = {}
        for i in range(10):
            self.squares_lookup_dict[str(i)] = i**2
        self.squares_diff_dict = {}
        self.squares_diff_dict['0'] = 0
        for i in range(1, 10):
            self.squares_diff_dict[i] = 2*i-1

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
        self.sum_dict = dict.fromkeys(range(81*self.sum_digits+1), 0)
        self.sum_multiplicity_dict = dict.fromkeys(range(81*self.sum_digits+1), 0)

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

    def create_sum_dict(self):
        split = self.sum_digits/2
        for j in range(10**split):
            subrange_min = j * 10**(self.sum_digits-split)
            subrange_max = (j+1) * 10**(self.sum_digits-split)
           
            print 'range', j, 'out of', 10**split
            print 'subranges', subrange_min, subrange_max
            sum_of_squares = 0
            for i in range(subrange_min, subrange_max):
                # need to recalculate the sum of digits squared
                # every ten increments
                if i % 10 == 0:                    
                    iteration = 0
                    str_i = str(i)

                    sum_of_squares = 0
                    for digit in str_i:
                        sum_of_squares += self.squares_lookup_dict[digit]
                else:
                    iteration += 1
                    sum_of_squares += self.squares_diff_dict[iteration]

                self.sum_dict[sum_of_squares] += i
                self.sum_dict[sum_of_squares] %= 10**self.sum_digits
                self.sum_multiplicity_dict[sum_of_squares] +=1

    def count_psquaredigits(self, num):
        for a_square in self.single_digit_squares:
            if num < a_square:
                # break out of loop if num-a_square < 0
                break
            if self.sum_multiplicity_dict.has_key(num-a_square):
                self.count+=self.sum_multiplicity_dict[num-a_square]
    
    def create_count_dict(self):
        if not self.sum_multiplicity_dict[0]:
            self.create_sum_dict()
        for i in range(self.max_count_int+1):
            self.count = 0
            self.count_psquaredigits(i)
            # print i, self.count
                    
            self.count_dict[i] = self.count
            

    def main(self):
        self.create_count_dict()
        for a_square in self.perf_squares:
            for i in range(a_square+1):
                if not self.count_dict.has_key(i):
                    continue
                elif not self.sum_dict.has_key(a_square-i):
                    continue

                multiplicity = self.count_dict[i]
                
                this_sum = self.sum_dict[a_square-i]

                # print 'square', a_square
                # print 'first sum', i, 'last sum', a_square - i
                # print 'multiplicity', multiplicity, 'sum', this_sum
                self.sum_total += (multiplicity * this_sum)
                self.sum_total %= 10**(self.sum_digits)

            print 'current square', a_square, 'sum_total', self.sum_total
