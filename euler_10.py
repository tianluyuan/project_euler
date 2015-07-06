""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sum_primes(nmax=2e6):
    """ Returns the sum of all primes less than nmax
    """
    from math import sqrt

    sum_total = 2
    curr_number = 3

    prime_list = [2]

    while curr_number < nmax:
        for prime in prime_list:
            if curr_number % prime == 0:
                curr_number += 2
                break

            if prime > sqrt(curr_number):
                prime_list.append(curr_number)
                sum_total += curr_number
                curr_number += 2

                break

    return sum_total
