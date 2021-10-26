# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest


class DocTests(unittest.TestCase):
    def test_same_code_as_readme_english(self):
        import datetime

        # Check if 2018-04-30 is holiday in China
        from chinese_calendar import is_holiday, is_workday

        april_last = datetime.date(2018, 4, 30)
        assert is_workday(april_last) is False
        assert is_holiday(april_last) is True

        # or check and get the holiday name
        import chinese_calendar as calendar  # 也可以这样 import

        on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
        assert on_holiday is True
        assert holiday_name == calendar.Holiday.labour_day.value

        # even check if a holiday is in lieu
        import chinese_calendar

        assert chinese_calendar.is_in_lieu(datetime.date(2006, 2, 1)) is False
        assert chinese_calendar.is_in_lieu(datetime.date(2006, 2, 2)) is True

    def test_same_code_as_readme_chinese(self):
        import datetime

        # 判断 2018年4月30号 是不是节假日
        from chinese_calendar import is_holiday, is_workday

        april_last = datetime.date(2018, 4, 30)
        assert is_workday(april_last) is False
        assert is_holiday(april_last) is True

        # 或者在判断的同时，获取节日名
        import chinese_calendar as calendar  # 也可以这样 import

        on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
        assert on_holiday is True
        assert holiday_name == calendar.Holiday.labour_day.value

        # 还能判断法定节假日是不是调休
        import chinese_calendar

        assert chinese_calendar.is_in_lieu(datetime.date(2006, 2, 1)) is False
        assert chinese_calendar.is_in_lieu(datetime.date(2006, 2, 2)) is True
