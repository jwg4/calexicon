import sys

if sys.hexversion < 0x02070000:
    import unittest2 as unittest
else:
    import unittest

from datetime import date

from .test_calendar import CalendarTest
from calexicon.dates.tests.test_dates import TestDateWithCalendar

from calexicon.calendars import EnglishHistoricalCalendar, SpanishHistoricalCalendar, FrenchHistoricalCalendar  # noqa
from calexicon.calendars.historical import SwitchDateWithCalendar


class BaseTestHistoricalCalendar(object):
    def setUp(self):
        self.calendar = self.calendar_type()

    def test_before_switch(self):
        for triplet in self.julian_triplets:
            self.check_valid_date(*triplet)

    def test_after_switch(self):
        for triplet in self.gregorian_triplets:
            self.check_valid_date(*triplet)

    def test_during_switch(self):
        for triplet in self.transition_triplets:
            self.check_invalid_date(*triplet)


class TestEnglishHistoricalCalendar(BaseTestHistoricalCalendar, CalendarTest):
    calendar_type = EnglishHistoricalCalendar
    gregorian_triplets = [(1752, 9, 14)]
    julian_triplets = [(1752, 9, 1), (1752, 9, 2)]
    transition_triplets = [(1752, 9, 3), (1752, 9, 6), (1752, 9, 13)]

    def test_correct_class(self):
        self.assertIsInstance(self.calendar.date(1415, 10, 25), SwitchDateWithCalendar)

    def test_display_string(self):
        self.display_string_comparison(
            1415, 10, 25,
            "25th October 1415 (English Historical Calendar - Julian)"
        )

    def test_display_string_gregorian_date(self):
        self.display_string_comparison(
            2012, 10, 30,
            "30th October 2012 (English Historical Calendar - Gregorian)"
        )


class TestSpanishHistoricalCalendar(BaseTestHistoricalCalendar, CalendarTest):
    calendar_type = SpanishHistoricalCalendar
    gregorian_triplets = [(1582, 10, 15), (1752, 9, 2), (1752, 9, 14)]
    julian_triplets = [(1582, 10, 4)]
    transition_triplets = [(1582, 10, 5), (1582, 10, 9), (1582, 10, 14)]


class TestFrenchHistoricalCalendar(BaseTestHistoricalCalendar, CalendarTest):
    calendar_type = FrenchHistoricalCalendar
    gregorian_triplets = []
    julian_triplets = []
    transition_triplets = []


class TestHistoricalCalendars(unittest.TestCase):
    def test_FrenchHistoricalCalendar(self):
        self.assertIsNotNone(FrenchHistoricalCalendar())


class TestSwitchDateWithCalendar(TestDateWithCalendar):
    def setUp(self):
        self.date_wc = SwitchDateWithCalendar(None, date(2010, 8, 1))
