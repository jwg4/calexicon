from datetime import date as vanilla_date, timedelta

from ..helpers import ordinal, month_string
from ..dates import DateWithCalendar, InvalidDate
from ..dates.bce import BCEDate
from ..constants import first_julian_date
from base import Calendar

class ProlepticGregorianCalendar(Calendar):
    display_name = "Proleptic Gregorian Calendar"
    representation_keys = set(['year', 'month', 'day'])

    def date(self, year, month, day):
        try:
            d = vanilla_date(year, month, day)
        except ValueError as e:
            raise InvalidDate(e.message)
        return self.from_date(d)

    @staticmethod
    def date_display_string(d):
        return "%s %s %s" % (ordinal(d.day), month_string(d.month), d.year)

    @staticmethod
    def representation(d):
        return { 'year': d.year, 'month': d.month, 'day': d.day }
        

class JulianCalendar(Calendar):
    display_name = "Julian Calendar"
    representation_keys = set(['year', 'month', 'day'])

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
        return False # pragma: no cover

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
        original_year = d.year
        offset = JulianCalendar._number_of_extra_leap_days(d)
        d = d - timedelta(days=offset)
        if JulianCalendar._is_julian_leap_year(original_year) and not JulianCalendar._is_gregorian_leap_year(original_year):
            if original_month >= 3 and (d.month <= 2 or d.year < original_year):
                if d.month == 2 and d.day == 28:
                    return (d.year, 2, 29)
                d = d + timedelta(days=1)
        return (d.year, d.month, d.day)

    @staticmethod
    def representation(d):
        year, month, day = JulianCalendar.julian_representation(d)
        return { 'year': year, 'month': month, 'day': day }
        
    @staticmethod
    def _number_of_extra_leap_days(end, start=vanilla_date(200, 3, 1)):
        count = 0
        for x in range(start.year, end.year + 1, 100):
            if not JulianCalendar._is_gregorian_leap_year(x):
                leap_day = vanilla_date(x, 2, 28)
                if start < leap_day < end:
                    count = count + 1
        return count

    def date(self, year, month, day):
        if day == 29 and month == 2 and self._is_julian_leap_year(year):
            d = vanilla_date(year, 2, 28)
            offset = self._number_of_extra_leap_days(d) + 1
        else:
            d = vanilla_date(year, month, day)
            offset = self._number_of_extra_leap_days(d)
        d = d + timedelta(days=offset)
        return self.from_date(d)

class ProlepticJulianCalendar(JulianCalendar):
    first_date = first_julian_date
    representation_keys = set(['year', 'month', 'day'])
        
    def date(self, year, month, day):
        try:
            d = JulianCalendar().date(year, month, day)
        except ValueError:
            d = BCEDate(year, month, day)
        self.bless(d)
        return d
