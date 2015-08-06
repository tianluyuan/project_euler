"""Starting in the top left corner of a 2x2 grid, and only being able
to move to the right and down, there are exactly 6 routes to the
bottom right corner.

How many such routes are there through a 20x20 grid?
"""
from utils import memoize

@memoize
def nroutes(coords, dims):
    if any([coord == dim
            for coord, dim in zip(coords, dims)]):
        return 1

    return nroutes((coords[0], coords[1]+1), dims)+nroutes((coords[0]+1, coords[1]), dims)


def routes(coords=(0,0),dims=(20,20)):
    return nroutes(coords, dims)
