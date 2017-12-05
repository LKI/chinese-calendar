# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from chinese_calendar.constants import holidays, workdays


def _validate_date(date):
    """
    check if the date is supported

    :type date: datetime.date
    :rtype: bool
    """
    min_year, max_year = min(holidays.keys()).year, max(holidays.keys()).year
    if not (min_year <= date.year <= max_year):
        raise NotImplementedError('no available data for year {}, only year between [{}, {}] supported'.format(
            date.year, min_year, max_year))


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
    _validate_date(date)

    weekday = date.weekday()
    return bool(date in workdays.keys() or (weekday <= 4 and date not in holidays.keys()))


def get_holiday_detail(date):
    """
    check if one date is holiday in China,
    and return the holiday name (None if it's a normal day)

    :type date: datetime.date
    :return: holiday bool indicator, and holiday name if it's holiday related day
    :rtype: (bool, str | None)
    """
    _validate_date(date)
    if date in workdays.keys():
        return False, workdays[date]
    elif date in holidays.keys():
        return True, holidays[date]
    else:
        return date.weekday() > 4, None
