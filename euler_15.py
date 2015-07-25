"""Starting in the top left corner of a 2x2 grid, and only being able
to move to the right and down, there are exactly 6 routes to the
bottom right corner.

How many such routes are there through a 20x20 grid?
"""
def memoize(f):
    """ Memoization decorator for functions taking one or more arguments.
    http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
    """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)


@memoize
def nroutes(coords, dims):
    if any([coord == dim
            for coord, dim in zip(coords, dims)]):
        return 1

    return nroutes((coords[0], coords[1]+1), dims)+nroutes((coords[0]+1, coords[1]), dims)


def routes(coords=(0,0),dims=(20,20)):
    return nroutes(coords, dims)
