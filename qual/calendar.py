from datetime import date, timedelta

class DateWithCalendar(object):
    def __init__(self, calendar_class, date):
        self.calendar = calendar_class
        self.date = date

    def convert_to(self, calendar):
        return calendar.from_date(self.date)

    def __eq__(self, other):
        return self.calendar == other.calendar and self.date == other.date

    def __str__(self):
        return "%s (%s)" % (self.date, self.calendar.__name__)

    @staticmethod
    def make_assertEqual(test_case):
        def assertEqual(a, b, msg):
            if a.__eq__(b):
                return True
            else:
                if msg is None:
                    msg = "%s is not equal to %s" % (a, b)
                raise test_case.failureException(msg)
        return assertEqual

class Calendar(object):
    def from_date(self, date):
        return DateWithCalendar(self.__class__, date)

class ProlepticGregorianCalendar(Calendar):
    def date(self, year, month, day):
        d = date(year, month, day)
        return self.from_date(d)

class JulianCalendar(Calendar):
    @staticmethod
    def is_julian_leap_year(y):
        return (y % 4) == 0

    def number_of_extra_leap_days(self, end, start=date(100, 3, 1)):
        def is_gregorian_leap_year(y):
            if (y % 400) == 0:
                return True
            if (y % 100) == 0:
                return False
            if (y % 4) == 0:
                return True
            return False
        count = 0
        for x in range(100, end.year + 1, 100):
            if not is_gregorian_leap_year(x):
                leap_day = date(x, 2, 28)
                if start < leap_day < end:
                    count = count + 1
        return count

    def date(self, year, month, day):
        if day == 29 and month == 2 and self.is_julian_leap_year(year):
            d = date(year, month, 28)
        else:
            d = date(year, month, day)
        d = d + timedelta(days=self.number_of_extra_leap_days(d))
        return self.from_date(d)

