"""Using names.txt (right click and 'Save Link/Target As...'), a 46K
text file containing over five-thousand first names, begin by sorting
it into alphabetical order. Then working out the alphabetical value
for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""
def load_names(filepath):
    """ Reads file into list
    """
    with open(filepath) as f:
        all_names = f.read()
        names = map(lambda name: name.strip('"'), all_names.split(','))

    return names


def alpha_value(name):
    """ returns the alphabetical value for name
    """
    return sum(map(lambda ch: ord(ch)-ord('A')+1, name.upper()))


def score_name(name, pos):
    return alpha_value(name) * pos


def p22():
    names = load_names('resources/p022_names.txt')
    names.sort()
    return sum([score_name(name, idx+1) for idx, name in enumerate(names)])
