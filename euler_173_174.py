# euler-173,174

# Using up to one million tiles how many different "hollow" square laminae can be formed?

# Let T be the number of tiles we can use
# Solution is the set of all integer (m,k) such that 4k(m+k)<=T

import math
import time

# 173
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

def num_laminae2(T=100):
    num = 0
    
    # since m>=1, we can set the max for k by solving the equation 
    # with m=1
    k_max = int((math.sqrt(T+1)-1)/2)
    for k in range(1, k_max+1):
        m_poss = T/(4*k) - k
        num+=m_poss

    return num

# 174
def num_distinct_laminae(T=100, distinct_laminae_range=range(1,11)):
    num_distinct = 0
    max_N = distinct_laminae_range[-1]
    
    # smallest T can be is 8
    # also t must be even
    for t in xrange(8, T+1, 2):
        # since m>=1, we can set the max for k by solving the equation 
        # with m=1
        k_max = int((math.sqrt(t+1)-1)/2)
        counter = 0
        counter_in_range = True
        for k in range(1, k_max+1):
            m = float(t)/(4*k) - k
            
            if not m - int(m) > 0:
                counter+=1
            
            if counter==0 or counter > max_N:
                counter_in_range = False
                break
        if counter_in_range:
            num_distinct+=1

    return num_distinct

def num_distinct_laminae2(T=100, distinct_laminae_range=range(1,11)):
    start = time.clock()
    tile_dict = {}

    # since m>=1, we can set the max for k by solving the equation 
    # with m=1
    k_max = int((math.sqrt(T+1)-1)/2)
    for k in range(1, k_max+1):
        m_poss = T/(4*k) - k
        # calculate tiles
        for m in range(1, m_poss+1):
            t = 4*k*(m+k)
            if tile_dict.has_key(t):
                tile_dict[t] +=1
            else:
                tile_dict[t] =1
            

    num = 0
    for n_tiles, n_tiled_laminae in tile_dict.iteritems():
        if n_tiled_laminae >= distinct_laminae_range[0] and n_tiled_laminae <= distinct_laminae_range[-1]:
            num+=1

    end = time.clock()
    print 'num_distinct_laminae2(%i) took %f seconds' % (T, end-start)
    return num
