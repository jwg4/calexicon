import sys

if sys.hexversion < 0x02070000:
    import unittest2 as unittest
else:
    import unittest

from hypothesis import given, example
from hypothesis.extra.datetime import datetimes

from qual.calendars import DateWithCalendar, ProlepticGregorianCalendar, JulianCalendar, InvalidDate

class CalendarTest(unittest.TestCase):
    calendar = None

    def check_valid_date(self, year, month, day):
        d = self.calendar.date(year, month, day)
        self.assertIsNotNone(d)
        self.assertEqual(d.calendar, self.calendar.__class__)

    def check_invalid_date(self, year, month, day):
        self.assertRaises(InvalidDate, lambda : self.calendar.date(year, month, day))

    @unittest.skipIf(calendar is None, 'We do not want this test to run in the base class.')
    @given(datetimes(timezones=[]))
    def test_date_strings(self, dt):
        d = dt.date()
        dc = self.calendar.from_date(d)
        self.assertIsNotNone(dc.__str__())

