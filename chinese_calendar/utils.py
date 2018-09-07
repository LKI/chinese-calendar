# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime

from chinese_calendar.constants import holidays, in_lieu_days, workdays


def _wrap_date(date):
    """
    transform datetime.datetime into datetime.date

    :type date: datetime.date | datetime.datetime
    :rtype: datetime.date
    """
    if isinstance(date, datetime.datetime):
        date = date.date()
    return date


def _validate_date(*dates):
    """
    check if the date(s) is supported

    :type date: datetime.date | datetime.datetime
    :rtype: datetime.date | list[datetime.date]
    """
    if len(dates) != 1:
        return list(map(_validate_date, dates))
    date = _wrap_date(dates[0])
    if not isinstance(date, datetime.date):
        raise NotImplementedError('unsupported type {}, expected type is datetime.date'.format(type(date)))
    min_year, max_year = min(holidays.keys()).year, max(holidays.keys()).year
    if not (min_year <= date.year <= max_year):
        raise NotImplementedError('no available data for year {}, only year between [{}, {}] supported'.format(
            date.year, min_year, max_year))
    return date


def is_holiday(date):
    """
    check if one date is holiday in China.
    in other words, Chinese people get rest at that day.

    :type date: datetime.date | datetime.datetime
    :rtype: bool
    """
    return not is_workday(date)


def is_workday(date):
    """
    check if one date is workday in China.
    in other words, Chinese people works at that day.

    :type date: datetime.date | datetime.datetime
    :rtype: bool
    """
    date = _validate_date(date)

    weekday = date.weekday()
    return bool(date in workdays.keys() or (weekday <= 4 and date not in holidays.keys()))


def is_in_lieu(date):
    """
    check if one date is in lieu in China.
    in other words, Chinese people get rest at that day because of legal holiday.

    :type date: datetime.date | datetime.datetime
    :rtype: bool
    """
    date = _validate_date(date)

    return date in in_lieu_days


def get_holiday_detail(date):
    """
    check if one date is holiday in China,
    and return the holiday name (None if it's a normal day)

    :type date: datetime.date | datetime.datetime
    :return: holiday bool indicator, and holiday name if it's holiday related day
    :rtype: (bool, str | None)
    """
    date = _validate_date(date)
    if date in workdays.keys():
        return False, workdays[date]
    elif date in holidays.keys():
        return True, holidays[date]
    else:
        return date.weekday() > 4, None


def get_dates(start, end):
    """
    get dates between start date and end date. (includes start date and end date)

    :type start: datetime.date | datetime.datetime
    :type end:  datetime.date | datetime.datetime
    :rtype: list[datetime.date]
    """
    start, end = map(_wrap_date, (start, end))
    delta_days = (end - start).days
    return [start + datetime.timedelta(days=delta) for delta in range(delta_days + 1)]


def get_holidays(start, end, include_weekends=True):
    """
    get holidays between start date and end date. (includes start date and end date)

    :type start: datetime.date | datetime.datetime
    :type end:  datetime.date | datetime.datetime
    :type include_weekends: bool
    :param include_weekends: False for excluding Saturdays and Sundays
    :rtype: list[datetime.date]
    """
    start, end = _validate_date(start, end)
    if include_weekends:
        return list(filter(is_holiday, get_dates(start, end)))
    return list(filter(lambda x: x in holidays, get_dates(start, end)))


def get_workdays(start, end):
    """
    get workdays between start date and end date. (includes start date and end date)

    :type start: datetime.date | datetime.datetime
    :type end:  datetime.date | datetime.datetime
    :rtype: list[datetime.date]
    """
    start, end = _validate_date(start, end)
    return list(filter(is_workday, get_dates(start, end)))


def find_workday(delta_days=0, date=None):
    """
    find the workday after {delta_days} days.

    :type delta_days: int
    :param delta_days: 0 means next workday (includes today), -1 means previous workday.
    :type date: datetime.date | datetime.datetime
    :param: the start point
    :rtype: datetime.date
    """
    date = _wrap_date(date or datetime.date.today())
    if delta_days >= 0:
        delta_days += 1
    sign = 1 if delta_days >= 0 else -1
    for i in range(abs(delta_days)):
        if delta_days < 0 or i:
            date += datetime.timedelta(days=sign)
        while not is_workday(date):
            date += datetime.timedelta(days=sign)
    return date
