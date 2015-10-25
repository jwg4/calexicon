from test_calendar import CalendarTest

from qual.calendars import EnglishHistoricalCalendar

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

class TestSpanishHistoricalCalendar(BaseTestHistoricalCalendar, CalendarTest):
    calendar_type = SpanishHistoricalCalendar
    gregorian_triplets = [(1582, 10, 15), (1752, 9, 2), (1752, 9, 14)]
    julian_triplets = [(1582, 10, 4)]
    transition_triplets = [(1582, 10, 5), (1582, 10, 9), (1582, 10, 14)]
