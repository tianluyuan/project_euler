"""If the numbers 1 to 5 are written out in words: one, two, three,
four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?
"""
ONES = ['',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen']

TENS = ['',
        '',
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety']

TRIPLETS = ['',
            'thousand',
            'million',
            'billion',
            'trillion',
            'quadrillion',
            'quintillion',
            'sextillion',
            'septillion']


def tripled_digits(num):
    """Splits num into a list of at most three digits each, starting from
    the right
    """
    digits = map(int, str(num))
    triples = []
    triple = []
    for digit in reversed(digits):
        triple.insert(0,digit)
        if len(triple) == 3:
            triples.append(triple)
            triple = []
    if triple:
        triples.append(triple)
    return triples


def digits_to_num(digits):
    place = 0
    num = 0
    for digit in reversed(digits):
        num += digit * 10**place
        place += 1

    return num


def build_tripled(digits):
    """ builds numbers up to but not including 1000 into a word
    """
    num = digits_to_num(digits)
    ndigits = len(digits)
    inwords = ''
    for idx, digit in enumerate(digits):
        place = ndigits - idx - 1
        if place == 2:
            if digit != 0:
                inwords += ONES[digit]+'hundredand'
        elif place == 1:
            if digit == 1:
                return inwords+ONES[num % 100]
            else:
                inwords += TENS[digit]
        elif place == 0:
            inwords += ONES[digit]
    return (inwords if inwords[-3:] != 'and' else inwords[:-3])


def convert_to_word(num):
    """convert number to a word
    e.g. 123-> onehundredandtwentythree
    """
    triples = tripled_digits(num)
    inwords = ''
    for idx, triple in enumerate(triples):
        inwords = build_tripled(triple) + TRIPLETS[idx] + inwords

    return inwords


def numletters(up_to_num=1000):
    nletters = 0
    for i in range(1, up_to_num+1):
        nletters += len(convert_to_word(i))

    return nletters
