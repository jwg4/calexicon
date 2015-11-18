# calexicon - dates and calendars

This is package for interpretation, conversion, information and testing of calendar systems. 

 - What's this package for, doesn't everyone use the same calendar?
 - * Well everyone agrees on what today is (apart from people in different time zones), which is why datetime doesn't have to worry about this stuff. But not everyone agrees on what a date 2050 years ago should be called. Python datetime and Unix cal don't even agree on how many days there are in September 1752.*

## How to create a date in a given calendar
```
In [1]: import qual

In [2]: cal = qual.calendars.FrenchHistoricalCalendar()

In [3]: cal2 = qual.calendars.JulianCalendar()

In [4]: cal3 = qual.calendars.ProlepticGregorianCalendar()

In [5]: d = cal.date(1500, 3, 1)

In [6]: str(d)
Out[6]: '1th March 1500 (French Historical Calendar - Julian)'

In [7]: d2 = d.convert_to(cal2)

In [8]: str(d2)
Out[8]: '1th March 1500 (Julian Calendar)'

In [9]: d3 = d.convert_to(cal3)

In [10]: str(d3)
Out[10]: '12th March 1500 (Proleptic Gregorian Calendar)'
```

