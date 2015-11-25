## Important sources
 - How to build a package is at http://python-packaging.readthedocs.org/en/latest/index.html

## Calendar sources
 - Lots of detail about calendar conversion is at http://norbyhus.dk/calendar.php
 - A mistake in Wolfram Alpha (and a good test case) http://mathematica.stackexchange.com/questions/97818/why-does-mathematicas-date-for-the-battle-agincourt-differ-from-the-us-navys
 - This page has lots of information about conversion algorithms: https://en.wikipedia.org/wiki/Julian_day

## Interesting calendars
 - Swedish historical calendar
 - Alaskan historical calendar
 - French revolutionary calendar
 - Julian day numbers
 - Roman historical calendar - not Julian until 4BC, due to leap year corrections.

## Year conversions
 - A special case of calendars - all dates are the same, but the years have different numbers.
 - Eg. Juche calendar https://en.wikipedia.org/wiki/North_Korean_calendar
 - Given a calendar, we should be able map a given year number to the start and end days of the year.
 - Eg. the British tax year, the Jewish year.

## Recurrent events
 - Easter
 - Thanksgiving
 - Rosh Hashanah
 - Hannukah
 - Leap days

## Daily observations
 - Soviet five-day work week
 - Phases of the moon

## 'Day collections'
 For example, the set of public holidays in the UK is a day collection. It isn't a single recurrent event, but we can check if any day is in the collection, or count the number of such days between any two dates.

## 'Day measurements'
 A function from the set of pairs of days, to a set of measurements. For example, age, measured in weeks for young babies, months for infants, years and quarter years for children, years for older people.

## Date edge cases
 1. Days which are in a different year in Julian and Gregorian.
 2. Epochs: Microsoft, Java, Unix, Julian.
 3. End days, Millenium, Mayan, Unix 32-bit rollover.
 4. Dates which are in different years depending on when the year starts.
 5. Dates which are leap days of the Julian calendar.

## Code things
 1. Always do `import ..helpers` etc. instead of `import calexicon.helpers`, except in tests where we can equally expect to run the tests from a the root folder and from a virtualenv which contains an installed version of the package.

