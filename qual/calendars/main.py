from datetime import date, timedelta

from date import DateWithCalendar, InvalidDate
from base import Calendar

class ProlepticGregorianCalendar(Calendar):
    def date(self, year, month, day):
        try:
            d = date(year, month, day)
        except ValueError as e:
            raise InvalidDate(e.message)
        return self.from_date(d)

class JulianCalendar(Calendar):
    @staticmethod
    def is_julian_leap_year(y):
        return (y % 4) == 0

    @staticmethod
    def is_gregorian_leap_year(y):
        if (y % 400) == 0:
            return True
        if (y % 100) == 0:
            return False
        if (y % 4) == 0:
            return True
        return False

    def number_of_extra_leap_days(self, end, start=date(200, 3, 1)):
        count = 0
        for x in range(start.year, end.year + 1, 100):
            if not self.is_gregorian_leap_year(x):
                leap_day = date(x, 2, 28)
                if start < leap_day < end:
                    count = count + 1
        return count

    def date(self, year, month, day):
        if day == 29 and month == 2 and self.is_julian_leap_year(year):
            d = date(year, 2, 28)
            offset = self.number_of_extra_leap_days(d) + 1
        else:
            d = date(year, month, day)
            offset = self.number_of_extra_leap_days(d)
        d = d + timedelta(days=offset)
        return self.from_date(d)

