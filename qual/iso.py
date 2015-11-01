from datetime import date, timedelta

def iso_to_gregorian(year, week, weekday):
    if week < 1 or week > 54:
        raise ValueError("Week number %d is invalid for an ISO calendar." % (week, ))
    jan_8 = date(year, 1, 8).isocalendar()
    offset = (week - jan_8[1]) * 7 + (weekday - jan_8[2])
    d = date(year, 1, 8) + timedelta(days=offset)
    if d.isocalendar()[0] != year:
        raise ValueError("Week number %d is invalid for ISO year %d." % (week, year))
    return d

