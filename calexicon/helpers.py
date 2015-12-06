from datetime import date as vanilla_date

def ordinal(n):
    suffix = "th"
    if n % 10 == 1:
        suffix =  "st"
    if n % 10 == 2:
        suffix =  "nd"
    if n % 10 == 3:
        suffix =  "rd"
    if 10 < n % 100 < 20:
        suffix = "th"
    return "%d%s" % (n, suffix)

def month_string(n):
    d = vanilla_date(1995, n, 1)
    return d.strftime("%B")
