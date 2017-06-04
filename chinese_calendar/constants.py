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
    datetime.date(year=2017, month=2, day=4): Holiday.spring_festival,
    datetime.date(year=2017, month=4, day=1): Holiday.tomb_sweeping_day,
    datetime.date(year=2017, month=5, day=27): Holiday.dragon_boat_festival,
}
