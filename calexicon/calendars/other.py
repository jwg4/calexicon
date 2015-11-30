from datetime import date as vanilla_date

from .base import Calendar

class JulianDayNumber(Calendar):
    first_ce_day = vanilla_date(1, 1, 1)
    first_ce_day_number = 1721423
    display_name = "Julian Day Number"

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


