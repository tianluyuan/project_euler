# euler-173

# Using up to one million tiles how many different "hollow" square laminae can be formed?

# Let T be the number of tiles we can use
# Solution is the set of all integer (m,k) such that 4k(m+k)<=T

import math

def num_laminae(T=100):
    num = 0
    
    # smallest T can be is 8
    # also t must be even
    for t in xrange(8, T+1, 2):
        # since m>=1, we can set the max for k by solving the equation 
        # with m=1
        k_max = int((math.sqrt(t+1)-1)/2)
        for k in range(1, k_max+1):
            m = float(t)/(4*k) - k
            if not m - int(m) > 0:
                num+=1

    return num
