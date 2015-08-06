"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def primes(n):
    """ returns the first n primes
    """
    from math import sqrt

    prime_list = [2]
    prime_index = 1

    curr_number = 3
    while prime_index < n:
        for prime in prime_list:
            if curr_number % prime == 0:
                curr_number += 2
                break
            if prime > sqrt(curr_number):
                prime_list.append(curr_number)
                prime_index += 1
                curr_number += 2

                break

    return prime_list


def nth_prime(n=10001):
    """ returns the nth prime
    """
    return primes(n)[-1]
