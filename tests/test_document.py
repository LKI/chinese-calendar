# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest


class DocTests(unittest.TestCase):
    def test_same_code_as_readme(self):
        import datetime

        # Check if 2018-04-30 is holiday in China
        from chinese_calendar import is_workday, is_holiday

        april_last = datetime.date(2018, 4, 30)
        self.assertFalse(is_workday(april_last))
        self.assertTrue(is_holiday(april_last))

        # or check and get the holiday name
        import chinese_calendar as calendar  # with different import style

        on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
        self.assertTrue(on_holiday)
        self.assertEqual(calendar.Holiday.labour_day.value, holiday_name)

        # even check if a holiday is in lieu
        import chinese_calendar

        self.assertFalse(chinese_calendar.is_in_lieu(datetime.date(2006, 2, 1)))
        self.assertTrue(chinese_calendar.is_in_lieu(datetime.date(2006, 2, 2)))
