from test_calendar import CalendarTest

from qual.calendars import EnglishHistoricalCalendar

class TestHistoricalCalendar(object):
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

class TestEnglishHistoricalCalendar(TestHistoricalCalendar, CalendarTest):
    calendar_type = EnglishHistoricalCalendar
    gregorian_triplets = [(1752, 9, 14)]
    julian_triplets = [(1752, 9, 1), (1752, 9, 2)]
    transition_triplets = [(1752, 9, 3), (1752, 9, 6), (1752, 9, 13)]
