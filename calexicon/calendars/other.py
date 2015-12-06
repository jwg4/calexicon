from datetime import date as vanilla_date, timedelta

from .base import Calendar
from ..dates.bce import BCEDate


class JulianDayNumber(Calendar):
    first_ce_day = vanilla_date(1, 1, 1)
    first_ce_day_number = 1721423
    display_name = "Julian Day Number"
    representation_keys = set(['day_number'])

    @staticmethod
    def date_display_string(d):
        n = JulianDayNumber._day_number(d)
        return "Day %d" % n

    @staticmethod
    def representation(d):
        return {'day_number': JulianDayNumber._day_number(d)}

    @staticmethod
    def _day_number(d):
        return (d - JulianDayNumber.first_ce_day).days + JulianDayNumber.first_ce_day_number

    def date(self, n):
        offset = n - self.first_ce_day_number
        if offset >= 0:
            vd = self.first_ce_day + timedelta(days=offset)
            return JulianDayNumber().from_date(vd)
        else:
            d = BCEDate(1, 1, 1)
            self.bless(d)
            return d
