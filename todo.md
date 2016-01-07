## Cleanups and fixes TODO

 1. ~~DateWithCalendar should not have member 'date' -> 'inner_date'~~
 2. ~~Don't use a variable name 'date' either -> 'dt_date'~~
 3. ~~Implement all the comparison operators correctly for DateWithCalendar.~~
 4. ~~Make DateWithCalendar inherit from datetime.date so that operators don't have to be reimplemented.~~ Not going to do this - datetime.date is an old-style object.

## TODO before version 0.1

 1. ~~Catholic historical calendar.~~
 2. ~~Display strings for dates.~~
 3. ~~Years before 1.~~
 4. Astronomical calendar (depends on 3.).
 5. Make a calendar for ISO.
 6. ~~README.md~~
 7. ~~Julian Date numbers (calendar?)~~
 8. ~~Methods for direct conversion between Julian and Gregorian.~~

## Fixes before version 0,1
 1. ~~'1th March 1500'~~

## Changes before version 0.1
 1. ~~Create a property which returns a datetime.date if possible, rather than using x._date._~~
 2. ~~Check all imports to make sure that we are importing the local code correctly.~~
 3. ~~Change all imports of date/datetime so that we import them as 'vanilla_date' etc.~~

## Tests before version 0.1
 1. ~~Every calendar should be able to generate a representation for all reasonable dates.~~
 2. ~~Every calendar should be able to generate a display string for all reasonable dates.~~
 3. Tests on constants.py.

## Cleanups before version 0.1
 1. Move all constants into constants.py.
 2. Remove JulianCalendar.julian_day_number() and replace functionality with JulianDayNumber calendar.
 3. Move _is_julian_leap_year etc from several places into global helpers.
 4. All calculations in internal. calendars, dates and fn call these helper functions.

## TODO after completing features for 0.1

 1. Register with pypi and upload.
 2. Complete documentation.

## TODO harder
 1. Deal with displaying calendar-specific strings in different locales.
 2. Deal with displaying calendar-specific strings with some notion of formatting.
 3. Make it work with Python 3.x.
 4. Use a single polymorphic date object which every calendar can be based on. Calendar objects are maybe not so important anymore.

