# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime

from chinese_calendar.constants import holidays, workdays


def is_holiday(date):
    """
    check if one date is holiday in China.
    in other words, Chinese people get rest at that day.
    :type date: datetime.date
    :rtype: bool
    """
    return not is_workday(date)


def is_workday(date):
    """
    check if one date is workday in China.
    in other words, Chinese people works at that day.
    :type date: datetime.date
    :rtype: bool
    """
    weekday = date.weekday()
    return bool(date in workdays.keys() or (weekday <= 4 and date not in holidays.keys()))
