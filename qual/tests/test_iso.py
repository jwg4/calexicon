import unittest
from hypothesis import given
from hypothesis.strategies import integers
from hypothesis.extra.datetime import datetimes

import qual

from datetime import date, MINYEAR, MAXYEAR

class TestIsoUtils(unittest.TestCase):
    @given(datetimes(timezones=[]))
    def test_round_trip_date(self, dt):
        d = dt.date()
        self.assertEqual(qual.iso_to_gregorian(*d.isocalendar()), d)

    @given(integers(MINYEAR, MAXYEAR), integers(1, 52), integers(1, 7))
    def test_round_trip_iso_date(self, year, week, day):
        y, w, d = qual.iso_to_gregorian(year, week, day).isocalendar()
        self.assertEqual(year, y)
        self.assertEqual(week, w)
        self.assertEqual(day, d)

    @given(integers(MINYEAR, MAXYEAR), integers(54), integers(1, 7))
    def test_weeks_greater_than_53_fail(self, year, week, day):
        self.assertRaises(ValueError, lambda : qual.iso_to_gregorian(year, week, day))

    @given(integers(MINYEAR, MAXYEAR), integers(None, 0), integers(1, 7))
    def test_weeks_smaller_than_1_fail(self, year, week, day):
        self.assertRaises(ValueError, lambda : qual.iso_to_gregorian(year, week, day))

