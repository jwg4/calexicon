import unittest
from hypothesis import given, example
from hypothesis.strategies import integers
from hypothesis.extra.datetime import datetimes

import calexicon

from datetime import date, MINYEAR, MAXYEAR

class TestIsoUtils(unittest.TestCase):
    @given(datetimes(timezones=[]))
    def test_round_trip_date(self, dt):
        d = dt.date()
        self.assertEqual(calexicon.fn.iso_to_gregorian(*d.isocalendar()), d)

    @given(integers(MINYEAR, MAXYEAR), integers(1, 52), integers(1, 7))
    def test_round_trip_iso_date(self, year, week, day):
        y, w, d = calexicon.fn.iso_to_gregorian(year, week, day).isocalendar()
        self.assertEqual(year, y)
        self.assertEqual(week, w)
        self.assertEqual(day, d)

    @given(integers(MINYEAR, MAXYEAR), integers(54), integers(1, 7))
    def test_weeks_greater_than_53_fail(self, year, week, day):
        self.assertRaises(ValueError, lambda : calexicon.fn.iso_to_gregorian(year, week, day))

    @given(integers(MINYEAR, MAXYEAR), integers(None, 0), integers(1, 7))
    def test_weeks_smaller_than_1_fail(self, year, week, day):
        self.assertRaises(ValueError, lambda : calexicon.fn.iso_to_gregorian(year, week, day))

    @given(integers(MINYEAR, MAXYEAR), integers(1, 7))
    @example(9999, 1)
    def test_week_53_either_raises_or_roundtrips(self, year, day):
        week = 53
        dt = None
        try:
            dt = calexicon.fn.iso_to_gregorian(year, week, day)
        except ValueError:
            # This error is ok - some years don't have a 53rd week
            return
        # If we don't get a value error, it has to be the right date
        y, w, d = dt.isocalendar()
        self.assertEqual(year, y)
        self.assertEqual(week, w)
        self.assertEqual(day, d)

