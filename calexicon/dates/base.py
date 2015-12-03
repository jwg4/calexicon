from ..helpers import ordinal, month_string

class InvalidDate(Exception):
    pass

class DateWithCalendar(object):
    def __init__(self, calendar_class, d):
        self.calendar = calendar_class
        self._date = d

    def to_date(self):
        return self._date

    def convert_to(self, calendar):
        return calendar.from_date(self._date)

    def __eq__(self, other):
        return self.calendar == other.calendar and self._date == other._date

    def __str__(self):
        return "%s (%s)" % (self.calendar.date_display_string(self._date), self.calendar.display_name)

    def __lt__(self, other):
        try:
            other_date = other._date
        except:
            other_date = other
        return self._date < other_date

    def __gt__(self, other):
        try:
            other_date = other._date
        except:
            other_date = other
        return self._date > other_date

    def __le__(self, other):
        try:
            other_date = other._date
        except:
            other_date = other
        return self._date <= other_date

    def __ge__(self, other):
        try:
            other_date = other._date
        except:
            other_date = other
        return self._date >= other_date

    def __sub__(self, other):
        try:
            other_date = other._date
        except:
            other_date = other
        return self._date - other_date

    @staticmethod
    def make_assertEqual(test_case):
        def assertEqual(a, b, msg):
            if a.__eq__(b):
                return True
            else:                # pragma: no cover
                if msg is None:
                    msg = "%s (%s) is not equal to %s (%s)" % (a, a._date, b, b._date)
                raise test_case.failureException(msg)
        return assertEqual

    def native_representation(self):
        return self.calendar.representation(self._date)

class BasicBCEDate(DateWithCalendar):
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

