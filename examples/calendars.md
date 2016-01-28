# Converting dates between calendars

>>> from datetime import date
>>> from calexicon.calendars import *
>>> d = GregorianCalendar().from_date(date(2010, 8, 1))
>>> d.convert_to(JulianCalendar())
