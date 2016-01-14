# calexicon - dates and calendars

This is package for interpretation, conversion, information and testing of calendar systems. 

[![Build Status](https://travis-ci.org/jwg4/calexicon.svg?branch=master)](https://travis-ci.org/jwg4/calexicon)
[![Coverage Status](https://coveralls.io/repos/jwg4/calexicon/badge.svg?branch=master&service=github)](https://coveralls.io/github/jwg4/calexicon?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/81a3e2bb39384e33a7bde326a66e0dd4)](https://www.codacy.com/app/jack-grahl/calexicon)

 - What's this package for, doesn't everyone use the same calendar?
 - *Well, everyone agrees on what today is (apart from some people in other time zones), which is why datetime doesn't have to worry about this stuff. But not everyone agrees on what a date 2050 years ago should be called. Python `datetime` and Unix `cal` don't even agree on how many days there are in September 1752.*
 - How does it work?
 - *There are lots of different calendar classes, with different names such as `GregorianCalendar`, `EnglishHistoricalCalendar`, `ProlepticGregorianCalendar`, and so on. You create a calendar object which is an instance of one of these classes. You can use this object to create a date using the convention of that calendar, to convert from a vanilla date or a date in another calendar, to convert to a vanilla date or a date in another calendar. Any dates created in that calendar will be calendar-aware - they know the identity of the calendar they were created with.*
 - So what different calendars are there?
 - *See the list of exported symbols in `calexicon/calendars/__init__.py`*
 - What about i18n? I can format vanilla dates in my own language and locale-speific format, what about this for dates with weird calendars?
 - *There is no internationalization at present. If you output the `str` of a date, you get English words and conventions for both the date itself and the name of the calendar.*

## How to create a date in a given calendar
```
In [1]: import calexicon

In [2]: cal = calexicon.calendars.FrenchHistoricalCalendar()

In [3]: cal2 = calexicon.calendars.JulianCalendar()

In [4]: cal3 = calexicon.calendars.ProlepticGregorianCalendar()

In [5]: d = cal.date(1500, 3, 1)

In [6]: str(d)
Out[6]: '1st March 1500 (French Historical Calendar - Julian)'

In [7]: d2 = d.convert_to(cal2)

In [8]: str(d2)
Out[8]: '1st March 1500 (Julian Calendar)'

In [9]: d3 = d.convert_to(cal3)

In [10]: str(d3)
Out[10]: '11th March 1500 (Proleptic Gregorian Calendar)'

In [11]: d3.native_representation()
Out[11]: {'day': 11, 'month': 3, 'year': 1500}
```

