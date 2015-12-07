from ..calendars import JulianCalendar, ProlepticGregorianCalendar


def julian_to_gregorian(year, month, day):
    calendar = JulianCalendar()
    d = calendar.date(year, month, day)
    converted = d.convert_to(ProlepticGregorianCalendar())
    converted = converted.native_representation()
    return (converted['year'], converted['month'], converted['day'])


def gregorian_to_julian(year, month, day):
    calendar = ProlepticGregorianCalendar()
    d = calendar.date(year, month, day)
    converted = d.convert_to(JulianCalendar()).native_representation()
    return (converted['year'], converted['month'], converted['day'])


def julian_to_julian_day_number(year, month, day):
    return 1


def julian_day_number_to_julian(number):
    return (-4713, 1, 1)
