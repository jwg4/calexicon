# Converting dates between calendars

>>> from datetime import date
>>> from calexicon.calendars import *
>>> d = ProlepticGregorianCalendar().from_date(date(2010, 8, 1))
>>> converted = d.convert_to(JulianCalendar())
>>> str(converted)
'19th July 2010 (Julian Calendar)'

# Creating dates in the calendar's own notation
>>> d = AstronomicalCalendar().date(0, 4, 1)
