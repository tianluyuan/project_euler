"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz
Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
CACHE = {1:1}
def length_collatz_chain(num):
    if CACHE.has_key(num):
        return CACHE[num]

    if num % 2 == 0:
        length = 1 + length_collatz_chain(num/2)
    else:
        length = 2 + length_collatz_chain((3*num+1)/2)

    CACHE[num] = length
    return length


def num_for_longest_chain(maxnum=int(1e6)):
    curr_max = 1
    curr_max_num = 1

    for num in xrange(1, maxnum):
        chain_length = length_collatz_chain(num)
        if chain_length > curr_max:
            curr_max = chain_length
            curr_max_num = num

    return curr_max_num

