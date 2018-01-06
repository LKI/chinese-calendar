# Chinese Calendar

[![Package](https://img.shields.io/pypi/v/chinesecalendar.svg)](https://pypi.python.org/pypi/chinesecalendar)
[![Travis](https://img.shields.io/travis/LKI/chinese-calendar.svg)](https://travis-ci.org/LKI/chinese-calendar)
[![License](https://img.shields.io/github/license/LKI/chinese-calendar.svg)](https://github.com/LKI/chinese-calendar/blob/master/LICENSE)
[![README](https://img.shields.io/badge/简介-中文-brightgreen.svg)](https://github.com/LKI/chinese-calendar/blob/master/README.md)

Check if some date is workday or holiday in China.
Support 2006 ~ 2018.
Available in Python2 and Python3.

## Installation

```
pip install chinesecalendar
```

## Sample

``` python
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
```

