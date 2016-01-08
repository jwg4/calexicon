from datetime import timedelta, date as vanilla_date

from base import DateWithCalendar
from ..internal.julian import distant_julian_to_gregorian
from ..constants import number_of_days_in_400_gregorian_years

class DistantDate(DateWithCalendar):
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    @property
    def _date(self):
        return self

    def __str__(self):
        s = "%d/%d/%d CE (Distant Date)"
        return s % (self.year, self.month, self.day)

    def __sub__(self, other):
        try:
            o_year = other.year
            if o_year < 10000:
                a = self - DistantDate(10000, 1, 1)
                b = vanilla_date(9999, 12, 31) - other
                x = a.days + b.days + 1
                return timedelta(days=x)
            if self.year == o_year:
                if self.month == other.month:
                    return timedelta(days=self.day - other.day)
                offset = ((self.year - 1600) // 400) * 400
                offset_self = vanilla_date(self.year - offset, self.month, self.day)
                offset_other = vanilla_date(other.year - offset, other.month, other.day)
                return offset_self - offset_other
            return timedelta(days=0)
        except AttributeError:
            pass
        try:
            _ = other.days
            return DistantDate(10000, 1, 1)
        except:
            pass
        return None

    def __add__(self, other):
        try:
            n = other.days
            td = other
        except:
            n = other
            td = timedelta(days=other)
        if n > number_of_days_in_400_gregorian_years:
            shifted_date = DistantDate(self.year - 400, self.month, self.day)
            shift = n - number_of_days_in_400_gregorian_years
            return shifted_date + shift
        offset = ((self.year - 1600) // 400) * 400
        offset_self = vanilla_date(self.year - offset, self.month, self.day)
        offset_sum = offset_self + td
        return DistantDate(offset_sum.year + offset, offset_sum.month, offset_sum.day)

    def __ge__(self, other):
        if self.year != other.year:
            return self.year > other.year
        if self.month != other.month:
            return self.month > other.month
        return self.day >= other.day

    def __le__(self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return not (self >= other)

    def __lt__(self, other):
        return not (self >= other)

    def __gt__(self, other):
        return not (self <= other)

    @staticmethod
    def julian_to_gregorian(y, m, d):
        return distant_julian_to_gregorian(y, m, d)
