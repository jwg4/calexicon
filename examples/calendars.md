# Converting dates between calendars

>>> from datetime import date
>>> from calexicon.calendars import *
>>> d = ProlepticGregorianCalendar().from_date(date(2010, 8, 1))
>>> converted = d.convert_to(JulianCalendar())
>>> str(converted)
'19th July 2010 (Julian Calendar)'

# Creating dates in the calendar's own notation
>>> d = AstronomicalCalendar().date(0, 4, 1)
>>> str(d)
'0/4/1 (Astronomical Calendar)'
>>> representation = d.native_representation()
>>> sorted(representation.keys())
['day', 'month', 'year']
>>> representation['day']
1
>>> representation['year']
0
