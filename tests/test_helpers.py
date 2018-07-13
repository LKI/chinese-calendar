# -*- coding: utf-8 -*-
import datetime
import unittest

from chinese_calendar.utils import find_workday


class HelperTests(unittest.TestCase):
    def test_find_workdays(self):
        dates = [
            datetime.date(2017, 12, 30),
            datetime.date(2017, 12, 31),
            datetime.date(2018, 1, 1),
            datetime.date(2018, 1, 2),
        ]
        cases = [[find_workday(i, date) for i in range(-7, 7)] for date in dates]
        for i in range(len(cases) - 1):
            self.assertListEqual(cases[i], cases[i + 1])
