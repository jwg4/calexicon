# This file is to test the most basic functionality after installing calexicon.
This is how you might import a calendar:
```
>>> from calexicon.calendars import JulianCalendar
>>> cal = JulianCalendar()

```

or import all calendars:
```
>>> from calexicon.calendars import *
>>> cal = JulianCalendar()
>>> cal2 = ProlepticGregorianCalendar()

```

or import the namespace of calendars:
```
>>> import calexicon.calendars
>>> cal = calexicon.calendars.JulianCalendar()

```
