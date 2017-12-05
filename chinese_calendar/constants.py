# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime
from enum import Enum


class Holiday(Enum):
    def __new__(cls, english, chinese, days):
        obj = object.__new__(cls)
        obj._value_ = english

        obj.chinese = chinese
        obj.days = days
        return obj

    new_years_day = 'New Year\'s Day', '元旦', 1
    spring_festival = 'Spring Festival', '春节', 3
    tomb_sweeping_day = 'Tomb-sweeping Day', '清明', 1
    labour_day = 'Labour Day', '劳动节', 1
    dragon_boat_festival = 'Dragon Boat Festival', '端午', 1
    national_day = 'National Day', '国庆节', 3
    mid_autumn_festival = 'Mid-autumn Festival', '中秋', 1


holidays = {
    datetime.date(year=2016, month=1, day=1): Holiday.new_years_day.value,
    datetime.date(year=2016, month=2, day=8): Holiday.spring_festival.value,
    datetime.date(year=2016, month=2, day=9): Holiday.spring_festival.value,
    datetime.date(year=2016, month=2, day=10): Holiday.spring_festival.value,
    datetime.date(year=2016, month=2, day=11): Holiday.spring_festival.value,
    datetime.date(year=2016, month=2, day=12): Holiday.spring_festival.value,
    datetime.date(year=2016, month=4, day=4): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2016, month=5, day=2): Holiday.labour_day.value,
    datetime.date(year=2016, month=6, day=9): Holiday.dragon_boat_festival.value,
    datetime.date(year=2016, month=9, day=15): Holiday.mid_autumn_festival.value,
    datetime.date(year=2016, month=9, day=16): Holiday.mid_autumn_festival.value,
    datetime.date(year=2016, month=10, day=3): Holiday.national_day.value,
    datetime.date(year=2016, month=10, day=4): Holiday.national_day.value,
    datetime.date(year=2016, month=10, day=5): Holiday.national_day.value,
    datetime.date(year=2016, month=10, day=6): Holiday.national_day.value,
    datetime.date(year=2016, month=10, day=7): Holiday.national_day.value,
    datetime.date(year=2017, month=1, day=2): Holiday.new_years_day.value,
    datetime.date(year=2017, month=1, day=27): Holiday.spring_festival.value,
    datetime.date(year=2017, month=1, day=30): Holiday.spring_festival.value,
    datetime.date(year=2017, month=1, day=31): Holiday.spring_festival.value,
    datetime.date(year=2017, month=2, day=1): Holiday.spring_festival.value,
    datetime.date(year=2017, month=2, day=2): Holiday.spring_festival.value,
    datetime.date(year=2017, month=4, day=3): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2017, month=4, day=4): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2017, month=5, day=1): Holiday.labour_day.value,
    datetime.date(year=2017, month=5, day=29): Holiday.dragon_boat_festival.value,
    datetime.date(year=2017, month=5, day=30): Holiday.dragon_boat_festival.value,
    datetime.date(year=2017, month=10, day=2): Holiday.national_day.value,
    datetime.date(year=2017, month=10, day=3): Holiday.national_day.value,
    datetime.date(year=2017, month=10, day=4): Holiday.mid_autumn_festival.value,
    datetime.date(year=2017, month=10, day=5): Holiday.national_day.value,
    datetime.date(year=2017, month=10, day=6): Holiday.national_day.value,
    datetime.date(year=2018, month=1, day=1): Holiday.new_years_day.value,
    datetime.date(year=2018, month=2, day=15): Holiday.spring_festival.value,
    datetime.date(year=2018, month=2, day=16): Holiday.spring_festival.value,
    datetime.date(year=2018, month=2, day=19): Holiday.spring_festival.value,
    datetime.date(year=2018, month=2, day=20): Holiday.spring_festival.value,
    datetime.date(year=2018, month=2, day=21): Holiday.spring_festival.value,
    datetime.date(year=2018, month=4, day=5): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2018, month=4, day=6): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2018, month=4, day=7): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2018, month=4, day=29): Holiday.labour_day.value,
    datetime.date(year=2018, month=4, day=30): Holiday.labour_day.value,
    datetime.date(year=2018, month=5, day=1): Holiday.labour_day.value,
    datetime.date(year=2018, month=6, day=18): Holiday.dragon_boat_festival.value,
    datetime.date(year=2018, month=9, day=24): Holiday.mid_autumn_festival.value,
    datetime.date(year=2018, month=10, day=1): Holiday.national_day.value,
    datetime.date(year=2018, month=10, day=2): Holiday.national_day.value,
    datetime.date(year=2018, month=10, day=3): Holiday.national_day.value,
    datetime.date(year=2018, month=10, day=4): Holiday.national_day.value,
    datetime.date(year=2018, month=10, day=5): Holiday.national_day.value,
}

workdays = {
    datetime.date(year=2016, month=2, day=6): Holiday.spring_festival.value,
    datetime.date(year=2016, month=2, day=14): Holiday.spring_festival.value,
    datetime.date(year=2016, month=6, day=12): Holiday.dragon_boat_festival.value,
    datetime.date(year=2016, month=9, day=18): Holiday.mid_autumn_festival.value,
    datetime.date(year=2016, month=10, day=8): Holiday.national_day.value,
    datetime.date(year=2016, month=10, day=9): Holiday.national_day.value,
    datetime.date(year=2017, month=2, day=4): Holiday.spring_festival.value,
    datetime.date(year=2017, month=4, day=1): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2017, month=5, day=27): Holiday.dragon_boat_festival.value,
    datetime.date(year=2017, month=9, day=30): Holiday.mid_autumn_festival.value,
    datetime.date(year=2018, month=2, day=11): Holiday.spring_festival.value,
    datetime.date(year=2018, month=2, day=24): Holiday.spring_festival.value,
    datetime.date(year=2018, month=4, day=8): Holiday.tomb_sweeping_day.value,
    datetime.date(year=2018, month=4, day=28): Holiday.labour_day.value,
    datetime.date(year=2018, month=9, day=29): Holiday.national_day.value,
    datetime.date(year=2018, month=9, day=30): Holiday.national_day.value,
}
