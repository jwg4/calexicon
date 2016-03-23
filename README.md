# calexicon - dates and calendars

This is package for interpretation, conversion, information and testing of calendar systems. 

[![PyPI](https://img.shields.io/pypi/v/calexicon.svg)](https://pypi.python.org/pypi/calexicon)
[![PyPI](https://img.shields.io/pypi/dm/calexicon.svg)](https://pypi.python.org/pypi/calexicon)
[![PyPI](https://img.shields.io/pypi/l/calexicon.svg)](https://pypi.python.org/pypi/calexicon)
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
>>> import calexicon
>>> cal = calexicon.calendars.FrenchHistoricalCalendar()
>>> cal2 = calexicon.calendars.JulianCalendar()
>>> cal3 = calexicon.calendars.ProlepticGregorianCalendar()
>>> d = cal.date(1000, 3, 1)
>>> str(d)
'1st March 1000 (French Historical Calendar - Julian)'
>>> d2 = d.convert_to(cal2)
>>> str(d2)
'1st March 1000 (Julian Calendar)'
>>> d3 = d.convert_to(cal3)
>>> str(d3)
'7th March 1000 (Proleptic Gregorian Calendar)'
>>> mydate = d3.native_representation()
>>> mydate['day']
7
>>> mydate['month']
3

```

