from datetime import timedelta

from base import DateWithCalendar

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
            if self.year == o_year:
                if self.month == other.month:
                    return timedelta(days=self.day - other.day)
            return timedelta(days=0)
        except AttributeError:
            pass
        try:
            _ = other.days
            return DistantDate(10000, 1, 1)
        except:
            pass
        return None

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
