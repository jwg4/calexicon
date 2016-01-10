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
            n = other.days
        except:
            return None
        if n < self.day:
            return DistantDate(self.year, self.month, self.day - n)
        n_days_in_month = days_in_month(self.year, self.month)
        if self.day < n_days_in_month < n:
            if month == 1:
                y = self.year - 1
                m = 12
            else:
                y = self.year
                m = self.month - 1
            return DistantDate(y, m, self.day) - timedelta(days=(n - n_days_in_month))
        return DistantDate(10000, 1, 1)

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
    def make_assertEqual(test_case):
        def assertEqual(a, b, msg):
            if a.year == b.year and a.month == b.month and a.day == b.day:
                return True
            else:                # pragma: no cover
                if msg is None:
                    msg = (
                        "DistantDate %d-%d-%d is not equal to DistantDate %d-%d-%d"
                        % (a.year, a.month, a.day, b.year, b.month, b.day)
                    )
                raise test_case.failureException(msg)
        return assertEqual

    @staticmethod
    def julian_to_gregorian(y, m, d):
        return distant_julian_to_gregorian(y, m, d)
