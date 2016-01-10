from datetime import date as vanilla_date, timedelta

from gregorian import is_gregorian_leap_year

def _number_of_extra_leap_days(end, start=vanilla_date(200, 3, 1)):
    count = 0
    for x in range(start.year, end.year + 1, 100):
        if not is_gregorian_leap_year(x):
            leap_day = vanilla_date(x, 2, 28)
            if start < leap_day and end > leap_day:
                count = count + 1
    return count

def _is_julian_leap_year(y):
    return (y % 4) == 0

def julian_to_gregorian(year, month, day):
    if day == 29 and month == 2 and _is_julian_leap_year(year):
        d = vanilla_date(year, 2, 28)
        offset = _number_of_extra_leap_days(d) + 1
    else:
        d = vanilla_date(year, month, day)
        offset = _number_of_extra_leap_days(d)
    d = d + timedelta(days=offset)
    return d

def distant_julian_to_gregorian(y, m, d):
    n = (y - 1600) // 400
    d = julian_to_gregorian(y - n * 400, m, d)
    d = d + timedelta(days=3 * n)
    return (d.year + n * 400, d.month, d.day)

