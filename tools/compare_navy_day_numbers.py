import logging
import re
import requests

from datetime import timedelta, date as vanilla_date

from calexicon.calendars import JulianDayNumber

logging.basicConfig(level=logging.INFO)

URL = "http://aa.usno.navy.mil/cgi-bin/aa_jdconv.pl?form=1&year=%d&month=%d&day=%d&era=1&hr=0&min=0&sec=0.0"

def get_navy_day_number(year, month, day):
    url = URL % (year, month, day)
    logging.debug("Retrieving %s" % url)
    r = requests.get(url)
    assert(r.status_code == 200)
    content = r.text
    logging.debug("Response: %s" % content)
    match = re.search('JD ([0-9]+)[.]', content)
    if not match:
        raise Exception("Could not parse a Julian day number from the response")
    return int(match.group(1))

def get_calexicon_number(year, month, day):
    vd = vanilla_date(year, month, day)
    d = JulianDayNumber().from_date(vd)
    return d.native_representation()['day_number']

def compare(vd):
    year = vd.year
    month = vd.month
    day = vd.day
    navy_number = get_navy_day_number(year, month, day)
    calexicon_number = get_calexicon_number(year, month, day)
    logging.info("Navy: %d, Calexicon: %d." % (navy_number, calexicon_number))
    if get_navy_day_number(year, month, day) != get_calexicon_number(year, month, day):
        return False
    else:
        return True

def binary_search(start, end):
    logging.info("Searching for anomalies between %s and %s" % (start, end))
    delta = (end - start).days
    half = int(delta / 2)
    if half == 0:
        return start, end
    mid = start + timedelta(days=half)
    if compare(mid) != compare(start):
        return binary_search(start, mid)
    elif compare(mid) != compare(end):
        return binary_search(mid, end)
    else:
        raise Exception("Couldn't properly subdivide the interval.")

print binary_search(vanilla_date(1, 1, 1), vanilla_date(2013, 1, 1))

