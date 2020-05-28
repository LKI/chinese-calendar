# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest
from collections import defaultdict

from chinese_calendar.constants import holidays, workdays


class HolidayAmountTests(unittest.TestCase):
    def test_holiday_amount(self):
        holiday_amounts = defaultdict(int)
        for date in holidays.keys():
            if date.weekday() <= 4:
                holiday_amounts[date.year] += 1
        for date in workdays.keys():
            if date.weekday() > 4:
                holiday_amounts[date.year] -= 1
        holiday_amounts[2007] -= 2  # 07年法定节假日有13天（国庆多了两天）
        holiday_amounts[2008] -= 2  # 08年同上
        holiday_amounts[2011] += 1  # 11年要补班12年的元旦假期
        holiday_amounts[2012] -= 1  # 12年可以享受11年补班的假
        holiday_amounts[2015] -= 1  # 15年是中国人民抗日战争暨世界反法西斯战争胜利70周年，多放1天
        holiday_amounts[2020] -= 2  # 20年春节因为新型冠状病毒疫情防控，延长假期2天
        for year in range(2007, 2020 + 1):  # 06年数据少，不测了
            self.assertEqual(11, holiday_amounts[year], "Holiday amount of year {}".format(year))
        self.assertEqual(1, 1)
