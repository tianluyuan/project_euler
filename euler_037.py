"""
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from utils import no_evens, is_prime, truncate


def truncatable_primes():
    curr = 11
    nprimes = 0
    while nprimes < 11:
        scurr = str(curr)
        if (scurr[0] != '1' and
            scurr[-1] != '1' and
            no_evens(int(scurr[1:]))):
            flag = True
            for truncated in truncate(curr):
                if not is_prime(truncated):
                    flag = False
                    break

            if flag:
                nprimes += 1
                yield curr

        curr += 2


def p37():
    return sum(truncatable_primes())
