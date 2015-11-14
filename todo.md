## Cleanups and fixes TODO

 1. ~~DateWithCalendar should not have member 'date' -> 'inner_date'~~
 2. ~~Don't use a variable name 'date' either -> 'dt_date'~~
 3. ~~Implement all the comparison operators correctly for DateWithCalendar.~~
 4. ~~Make DateWithCalendar inherit from datetime.date so that operators don't have to be reimplemented.~~ Not going to do this - datetime.date is an old-style object.

## TODO before version 0.1

 1. ~~Catholic historical calendar.~~
 2. ~~Display strings for dates.~~
 3. Years before 1.
 4. Astronomical calendar (depends on 3.).
 5. Make a calendar for ISO.
 6. ~~README.md~~
 7. ~~Julian Date numbers (calendar?)~~

## Fixes before version 0,1
 1. ~~'1th March 1500'~~

## TODO after completing features for 0.1

 1. Register with pypi and upload.
 2. Make it work with Python 3.x.
 3. Complete documentation.

## TODO harder
 1. Deal with displaying calendar-specific strings in different locales.
 2. Deal with displaying calendar-specific strings with some notion of formatting.

