from datetime import date

from base import Calendar
from date import InvalidDate
from main import JulianCalendar

class JulianToGregorianCalendar(Calendar):
    def date(self, year, month, day):
        gregorian_date = date(year, month, day)
        if gregorian_date < self.first_gregorian_day:
            julian_date = JulianCalendar().date(year, month, day)
            if julian_date > self.first_gregorian_day:
                raise InvalidDate("This is a 'missing day' when the calendars changed.")
            self.bless(julian_date)
            return julian_date
        return self.from_date(gregorian_date)

    def bless(self, date):
        date.calendar = self.__class__

class EnglishHistoricalCalendar(JulianToGregorianCalendar):
    first_gregorian_day = date(1752, 9, 13)
