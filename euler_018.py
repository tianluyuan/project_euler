"""Find the maximum total from top to bottom of the triangle in
resources/p18.txt
"""
from math import sqrt, ceil

def load_triangle(filepath):
    """ Reads file into list
    """
    with open(filepath) as f:
        lines = list(f.readlines())
        nrows = len(lines)
        return (reduce(lambda x, y: x+y,
                       [map(int, line.split()) for line in lines]),
                nrows)


def get_row(index):
    """the row corresponding to the index can be found by solving for
    n*(n+1)/2 = index+1
    """
    return int(ceil((-1+sqrt(1+8*(index+1)))/2))


def recalculate_at_index(index, triangle):
    """calculates the max possible based on the max of value[index]+
    either of the two possible paths below
    """
    row = get_row(index)
    triangle[index] = max(triangle[index]+triangle[index+row],
                          triangle[index]+triangle[index+row+1])


def max_possible(filepath):
    """ Returns the maximum path from top to bottom
    """
    triangle, nrows = load_triangle(filepath)
    curr_index = len(triangle) - nrows - 1

    while curr_index >= 0:
        recalculate_at_index(curr_index, triangle)
        curr_index -= 1

    return triangle[0]


def p18():
    return max_possible('resources/p018_triangle.txt')
