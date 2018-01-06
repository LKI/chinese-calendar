# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from os.path import dirname, join, realpath

from chinese_calendar.scripts.data import Arrangement, constants_template


def _get_lines(days):
    yield '{'
    sentence = '    datetime.date(year={}, month={}, day={}): {}.value,'
    for date in sorted(days.keys()):
        yield sentence.format(date.year, date.month, date.day, days[date])
    yield '}'


def get_constants_file_path():
    return join(dirname(dirname(realpath(__file__))), 'constants.py')


def generate_constants():
    arrangement = Arrangement()
    file_content = constants_template.format(
        '\n'.join(_get_lines(arrangement.holidays)),
        '\n'.join(_get_lines(arrangement.workdays)),
    )
    file_path = get_constants_file_path()
    with open(file_path, 'wb') as f:
        f.write(file_content.encode('utf-8'))


if __name__ == '__main__':
    generate_constants()
