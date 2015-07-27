"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def sieve(prime, list_to_check):
    # cross out multiples of curr_prime in list_to_check
    for idx, number in enumerate(list_to_check):
        if number <= 1:
            continue
        elif number % prime == 0:
            list_to_check[idx] = -1


def nth_prime_sieve(n=10001):
    """ returns the nth prime
    """
    prime_list = [2]
    iteration = 0
    while len(prime_list) < n:
        list_min = iteration*n
        list_max = (iteration+1)*n
        list_to_check = range(list_min, list_max)

        # loop over primes in prime_list and do sieve of erasthones
        for curr_prime in prime_list:
            sieve(curr_prime, list_to_check)

        # loop and do sieve on list_to_check
        for number in list_to_check:
            if number <= 1:
                continue

            curr_prime = number
            prime_list.append(curr_prime)

            sieve(curr_prime, list_to_check)

        iteration += 1

    return prime_list[n-1]


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
