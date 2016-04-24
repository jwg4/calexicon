import sys

if sys.hexversion < 0x02070000:
    import unittest2 as unittest
else:
    import unittest

from hypothesis import given
from hypothesis.extra.datetime import datetimes

from calexicon.dates import DateWithCalendar
from calexicon.internal.exception import InvalidDate


class CalendarTest(unittest.TestCase):
    calendar = None

    def setUpDateEquality(self):
        self.addTypeEqualityFunc(
            DateWithCalendar,
            DateWithCalendar.make_assertEqual(self)
        )

    def check_valid_date(self, year, month, day, expected_class=None):
        d = self.calendar.date(year, month, day)
        self.assertIsNotNone(d)
        if expected_class is None:
            expected_class = self.calendar.__class__
        self.assertEqual(d.calendar, expected_class)

    def check_invalid_date(self, year, month, day):
        self.assertRaises(InvalidDate, lambda: self.calendar.date(year, month, day))

    @given(datetimes(timezones=[]))
    def test_date_strings(self, dt):
        if self.calendar is None:
            return
        d = dt.date()
        dc = self.calendar.from_date(d)
        self.assertIsNotNone(dc.__str__())

    @given(datetimes(timezones=[]))
    def test_native_representation(self, dt):
        if self.calendar is None:
            return
        d = dt.date()
        dc = self.calendar.from_date(d)
        representation = dc.native_representation()
        self.assertIsNotNone(representation)
        self.assertEqual(set(representation.keys()), self.calendar.representation_keys)

    def display_string_comparison(self, year, month, day, expected):
        d = self.calendar.date(year, month, day)
        self.assertEqual(d.__str__(), expected)
