"""A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is 9009 = 91 x
99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]


def largest_palindrome(ndigits=3):
    curr0 = 10**ndigits - 1
    curr1 = 10**ndigits - 1

    largest_palin = 0
    while curr1 >=curr0:
        palin = curr0*curr1
        if is_palindrome(palin) and palin > largest_palin:
            largest_palin = palin

        if curr1 == curr0:
            curr0 -= 1
            curr1 = 10**ndigits - 1

            if largest_palin > curr1*curr0:
                break
        elif curr1 > curr0:
            curr1 -= 1
        if curr0 < 10**(ndigits-1):
            break

    return largest_palin
