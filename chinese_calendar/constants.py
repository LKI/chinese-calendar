# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime


class Holiday(object):
    new_years_day = 'New Year\'s Day'
    spring_festival = 'Spring Festival'
    tomb_sweeping_day = 'Tomb-sweeping Day'
    labour_day = 'Labour Day'
    dragon_boat_festival = 'Dragon Boat Festival'
    national_day = 'National Day'
    mid_autumn_festival = 'Mid-autumn Festival'


holidays = {
    datetime.date(year=2016, month=1, day=1): Holiday.new_years_day,
    datetime.date(year=2016, month=2, day=8): Holiday.spring_festival,
    datetime.date(year=2016, month=2, day=9): Holiday.spring_festival,
    datetime.date(year=2016, month=2, day=10): Holiday.spring_festival,
    datetime.date(year=2016, month=2, day=11): Holiday.spring_festival,
    datetime.date(year=2016, month=2, day=12): Holiday.spring_festival,
    datetime.date(year=2016, month=4, day=4): Holiday.tomb_sweeping_day,
    datetime.date(year=2016, month=5, day=2): Holiday.labour_day,
    datetime.date(year=2016, month=6, day=9): Holiday.dragon_boat_festival,
    datetime.date(year=2016, month=9, day=15): Holiday.mid_autumn_festival,
    datetime.date(year=2016, month=9, day=16): Holiday.mid_autumn_festival,
    datetime.date(year=2016, month=10, day=3): Holiday.national_day,
    datetime.date(year=2016, month=10, day=4): Holiday.national_day,
    datetime.date(year=2016, month=10, day=5): Holiday.national_day,
    datetime.date(year=2016, month=10, day=6): Holiday.national_day,
    datetime.date(year=2016, month=10, day=7): Holiday.national_day,
    datetime.date(year=2017, month=1, day=2): Holiday.new_years_day,
    datetime.date(year=2017, month=1, day=27): Holiday.spring_festival,
    datetime.date(year=2017, month=1, day=30): Holiday.spring_festival,
    datetime.date(year=2017, month=1, day=31): Holiday.spring_festival,
    datetime.date(year=2017, month=2, day=1): Holiday.spring_festival,
    datetime.date(year=2017, month=2, day=2): Holiday.spring_festival,
    datetime.date(year=2017, month=4, day=3): Holiday.tomb_sweeping_day,
    datetime.date(year=2017, month=4, day=4): Holiday.tomb_sweeping_day,
    datetime.date(year=2017, month=5, day=1): Holiday.labour_day,
    datetime.date(year=2017, month=5, day=29): Holiday.dragon_boat_festival,
    datetime.date(year=2017, month=5, day=30): Holiday.dragon_boat_festival,
    datetime.date(year=2017, month=10, day=2): Holiday.national_day,
    datetime.date(year=2017, month=10, day=3): Holiday.national_day,
    datetime.date(year=2017, month=10, day=4): Holiday.mid_autumn_festival,
    datetime.date(year=2017, month=10, day=5): Holiday.national_day,
    datetime.date(year=2017, month=10, day=6): Holiday.national_day,
}

workdays = {
    datetime.date(year=2016, month=2, day=6): Holiday.spring_festival,
    datetime.date(year=2016, month=2, day=14): Holiday.spring_festival,
    datetime.date(year=2016, month=6, day=12): Holiday.dragon_boat_festival,
    datetime.date(year=2016, month=9, day=18): Holiday.mid_autumn_festival,
    datetime.date(year=2016, month=10, day=8): Holiday.national_day,
    datetime.date(year=2016, month=10, day=9): Holiday.national_day,
    datetime.date(year=2017, month=2, day=4): Holiday.spring_festival,
    datetime.date(year=2017, month=4, day=1): Holiday.tomb_sweeping_day,
    datetime.date(year=2017, month=5, day=27): Holiday.dragon_boat_festival,
}
