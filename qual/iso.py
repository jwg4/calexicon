from datetime import date, timedelta

def iso_to_gregorian(year, week, weekday):
    jan_8 = date(year, 1, 8).isocalendar()
    offset = (week - jan_8[1]) * 7 + (weekday - jan_8[2])
    return date(year, 1, 8) + timedelta(days=offset)

