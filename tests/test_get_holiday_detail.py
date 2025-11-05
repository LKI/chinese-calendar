import unittest
import datetime

from chinese_calendar.utils import get_holiday_detail


class getHolidayDetailsTests(unittest.TestCase):
    def test_get_holiday_detail_eng(self):
        nation_day = datetime.date(2025, 10, 1)
        is_on_holiday, holiday_name_eng = get_holiday_detail(nation_day)
        self.assertEqual(is_on_holiday, True)
        self.assertEqual(holiday_name_eng, 'National Day')

    def test_get_holiday_chn(self):
        nation_day = datetime.date(2025, 10, 1)
        is_on_holiday, holiday_name_chn = get_holiday_detail(nation_day, in_english=False)
        self.assertEqual(is_on_holiday, True)
        self.assertEqual(holiday_name_chn, '国庆节')


if __name__ == '__main__':
    unittest.main()