from datetime import date

def ordinal(n):
    if n == 3:
        return "3rd"
    return "%dth" % n

def month_string(n):
    d = date(1995, n, 1)
    return d.strftime("%B")
    
