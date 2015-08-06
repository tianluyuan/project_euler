# project-euler #41
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
#

# If sum of digits is divisible by 3, the original number is divisible by 3.  This lets us ignore
# 9-digit pandigitals
# We can also ignore numbers that end in 2,4,6,8 or 5
import itertools
import math

def get_good_lengths():
    good = []
    summed = 0
    for i in range(1, 10):
        summed +=i
        if not summed%3==0:
            good.append(i)

    return good

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def get_largest_prime():
    prime_lengths  = get_good_lengths()
    prime_lengths.reverse()
    primes_list = []
    for good_length in prime_lengths:
        digits_list = range(1, good_length+1)
        digits_list.reverse()

        perms = itertools.permutations(digits_list)

        for perm in perms:
            # ignore numbers with last digit even or 5
            if perm[-1]%2 == 0 or perm[-1]%5 == 0:
                continue
            # ignore numbers with digits taht sum to be divisible by 3
            elif reduce(lambda x,y: x+y, perm) % 3 == 0:
                continue

            num = int(''.join(map(str,perm)))
            # Now everything that is a multiple of 2,3, or 5 should be 
            # removed.  We generate a list of primes up to sqrt of the largest
            # number using sieve and check to see if it's prime using the
            # generated list
            if len(primes_list) == 0:
                print 'generating primes list'
                primes_list.extend(list(primes_sieve2(int(math.sqrt(num)+1))))

            num_is_prime = True
            for prime in primes_list[3:]:
                if num%prime ==0:
                    num_is_prime = False
                    break

            if num_is_prime:
                print 'Largest prime', num
                return
