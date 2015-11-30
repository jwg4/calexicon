from datetime import date as vanilla_date

from calendar_testing import CalendarTest

from calexicon.calendars.other import JulianDayNumber

class TestJulianDayNumber(CalendarTest):
    def setUp(self):
        self.calendar = JulianDayNumber()

    def test_make_date(self):
        vd = vanilla_date(2010, 8, 1)
        d = self.calendar.from_date(vd)
        self.assertIsNotNone(d)


