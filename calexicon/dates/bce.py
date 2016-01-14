from datetime import timedelta

from base import BasicBCEDate
from ..internal.output import ordinal, month_string
from ..constants import first_julian_date


class BCEDate(BasicBCEDate):
    def __str__(self):
        date_string = "%s %s %s BCE" % (
            ordinal(self.day),
            month_string(self.month),
            -self.year
        )
        display_name = (
            "Julian Calendar"
            if (self >= first_julian_date)
            else "Proleptic Julian Calendar"
        )
        return "%s (%s)" % (date_string, display_name)

    def __ge__(self, other):
        if self.year != other.year:
            return self.year > other.year
        if self.month != other.month:
            return self.month > other.month
        return self.day >= other.day

    @property
    def _date(self):
        return self

    @staticmethod
    def _is_julian_leap_year(y):
        return (y % 4) == 0

    @staticmethod
    def _month_length(y, m):
        if BCEDate._is_julian_leap_year(y):
            return [None, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m]
        else:
            return [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m]

    @staticmethod
    def _year_length(y):
        if BCEDate._is_julian_leap_year(y):
            return 366
        else:
            return 365

    @staticmethod  # noqa
    def _subtract(a, b):
        if (a.year == b.year and a.month == b.month and a.day == b.day):
            return 0
        if ((a.year < b.year) or
                (a.year == b.year and a.month < b.month) or
                (a.year == b.year and a.month == b.month and a.day < b.day)):
            return -BCEDate._subtract(b, a)
        if (a.year == b.year and a.month == b.month):
            return a.day - b.day
        if (a.day != 1):
            return a.day - 1 + BCEDate._subtract(BCEDate(a.year, a.month, 1), b)
        if (a.month != 3):
            if a.month == 1:
                previous_year = a.year - 1
                if previous_year == 0:
                    previous_year = -1
                return 31 + BCEDate._subtract(BCEDate(previous_year, 12, 1), b)
            return (
                BCEDate._month_length(a.year, a.month - 1) +
                BCEDate._subtract(BCEDate(a.year, a.month - 1, 1), b)
            )
        if a.year - b.year > 3:
            n_cycles = (a.year - b.year) // 4
            n_days = n_cycles * (365 * 3 + 366)
            return n_days + BCEDate._subtract(BCEDate(a.year - 4 * n_cycles, 3, 1), b)
        return (
            BCEDate._year_length(a.year) +
            BCEDate._subtract(BCEDate(a.year - 1, 3, 1), b)
        )

    def __sub__(self, other):
        try:
            other_date = other._date
        except:
            other_date = other
        return timedelta(days=BCEDate._subtract(self._date, other_date))

    def julian_representation(self):
        return (self.year, self.month, self.day)
