# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime
from unittest import TestCase

from utils import is_holiday, is_workday


class BasicTests(TestCase):
    def test_opposite(self):
        date = datetime.date.today()
        self.assertEqual(not is_workday(date), is_holiday(date))

    def test_holidays(self):
        dates = [
            datetime.date(year=2017, month=5, day=30),
            datetime.date(year=2017, month=6, day=4),
            datetime.date(year=2017, month=10, day=1),
        ]
        for date in dates:
            self.assertFalse(is_workday(date))
            self.assertTrue(is_holiday(date))

    def test_workdays(self):
        dates = [
            datetime.date(year=2017, month=5, day=27),
            datetime.date(year=2017, month=6, day=5),
            datetime.date(year=2017, month=10, day=31),
        ]
        for date in dates:
            self.assertFalse(is_holiday(date))
            self.assertTrue(is_workday(date))
