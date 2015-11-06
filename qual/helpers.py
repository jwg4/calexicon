from datetime import date

def ordinal(n):
    suffix = "th"
    if n % 10 == 1:
        suffix =  "st"
    if n % 10 == 2:
        suffix =  "nd"
    if n % 10 == 3:
        suffix =  "rd"
    return "%d%s" % (n, suffix)

def month_string(n):
    d = date(1995, n, 1)
    return d.strftime("%B")
    
