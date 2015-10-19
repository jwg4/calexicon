from test_calendar import CalendarTest

from qual.calendars import EnglishHistoricalCalendar

class TestEnglishHistoricalCalendar(CalendarTest):
    def setUp(self):
        self.calendar = EnglishHistoricalCalendar()

    def test_before_switch(self):
        self.check_valid_date(1752, 9, 1)

    def test_after_switch(self):
        self.check_valid_date(1752, 9, 13)

    def test_during_switch(self):
        self.check_invalid_date(1752, 9, 6)
