"""How many Sundays fell on the first of the month during the
twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from datetime import date, timedelta


def sundays_first_of_month(start=date(1901, 1, 1),
                           end=date(2000, 12, 31)):
    elapsed = end - start

    count = 0
    for days in xrange(elapsed.days):
        this_date = start + timedelta(days)

        if this_date.weekday() == 6 and this_date.day == 1:
            count += 1

    return count
