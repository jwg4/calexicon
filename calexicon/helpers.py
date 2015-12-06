from datetime import date as vanilla_date


def ordinal(n):
    suffix = "th"
    if n % 10 in [1, 2, 3]:
        suffix = [None, 'st', 'nd', 'rd'][n % 10]
    if 10 < n % 100 < 20:
        suffix = "th"
    return "%d%s" % (n, suffix)


def month_string(n):
    d = vanilla_date(1995, n, 1)
    return d.strftime("%B")
