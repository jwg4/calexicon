from datetime import date, timedelta

from calexicon.helpers import ordinal, month_string
from dates import DateWithCalendar, InvalidDate
from base import Calendar

class ProlepticGregorianCalendar(Calendar):
    display_name = "Proleptic Gregorian Calendar"

    def date(self, year, month, day):
        try:
            d = date(year, month, day)
        except ValueError as e:
            raise InvalidDate(e.message)
        return self.from_date(d)

    @staticmethod
    def date_display_string(d):
        return "%s %s %s" % (ordinal(d.day), month_string(d.month), d.year)

class JulianCalendar(Calendar):
    display_name = "Julian Calendar"

    @staticmethod
    def _is_julian_leap_year(y):
        return (y % 4) == 0

    @staticmethod
    def _is_gregorian_leap_year(y):
        if (y % 400) == 0:
            return True
        if (y % 100) == 0:
            return False
        if (y % 4) == 0:
            return True
        return False

    def julian_day_number(self, d):
        td = d - self.date(1, 1, 1)
        return td.days + 1721426

    @staticmethod
    def date_display_string(d):
        year, month, day = JulianCalendar.julian_representation(d)
        return "%s %s %s" % (ordinal(day), month_string(month), year)

    @staticmethod
    def julian_representation(d):
        original_month = d.month
        offset = JulianCalendar._number_of_extra_leap_days(d)
        d = d - timedelta(days=offset)
        if JulianCalendar._is_julian_leap_year(d.year) and not JulianCalendar._is_gregorian_leap_year(d.year):
            if original_month >= 3 and d.month <= 2:
                if d.month == 2 and d.day == 28:
                    return (d.year, 2, 29)
                d = d + timedelta(days=1)
        return (d.year, d.month, d.day)
        
    @staticmethod
    def _number_of_extra_leap_days(end, start=date(200, 3, 1)):
        count = 0
        for x in range(start.year, end.year + 1, 100):
            if not JulianCalendar._is_gregorian_leap_year(x):
                leap_day = date(x, 2, 28)
                if start < leap_day < end:
                    count = count + 1
        return count

    def date(self, year, month, day):
        if day == 29 and month == 2 and self._is_julian_leap_year(year):
            d = date(year, 2, 28)
            offset = self._number_of_extra_leap_days(d) + 1
        else:
            d = date(year, month, day)
            offset = self._number_of_extra_leap_days(d)
        d = d + timedelta(days=offset)
        return self.from_date(d)

class ProlepticJulianCalendar(JulianCalendar):
    class BCEDate(DateWithCalendar):
        def __init__(self, year, month, day):
            self._validate(year, month, day)
            self.calendar = None
            self.date = None
            self.year = year
            self.month = month
            self.day = day

        @staticmethod
        def _validate(year, month, day):
            if year == 0:
                raise InvalidDate('There is no year 0 in the Proleptic Julian Calendar')
            lengths = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if year % 4 == 0:
                lengths[2] = 29
            if day > lengths[month]:
                raise InvalidDate('That month does not have %d days.' % day) 

        def __str__(self):
            date_string = "%s %s %s BCE" % (ordinal(self.day), month_string(self.month), -self.year)
            display_name = "Julian Calendar" if (self >= ProlepticJulianCalendar.first_date) else "Proleptic Julian Calendar"
            return "%s (%s)" % (date_string, display_name)
        
        def __ge__(self, other):
            if self.year != other.year:
                return self.year > other.year
            if self.month != other.month:
                return self.month > other.month
            return self.day >= other.day

    first_date = BCEDate(-45, 1, 1)
        
    def date(self, year, month, day):
        try:
            d = JulianCalendar().date(year, month, day)
        except ValueError:
            d = ProlepticJulianCalendar.BCEDate(year, month, day)
        self.bless(d)
        return d