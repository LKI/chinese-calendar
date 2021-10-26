# Chinese Calendar

[![Package](https://img.shields.io/pypi/v/chinesecalendar.svg)](https://pypi.python.org/pypi/chinesecalendar)
[![Travis](https://img.shields.io/travis/LKI/chinese-calendar.svg)](https://travis-ci.org/LKI/chinese-calendar)
[![License](https://img.shields.io/github/license/LKI/chinese-calendar.svg)](https://github.com/LKI/chinese-calendar/blob/master/LICENSE)
[![README](https://img.shields.io/badge/简介-中文-brightgreen.svg)](https://github.com/LKI/chinese-calendar/blob/master/README.md)

Check if some date is workday or holiday in China.
Support 2004 ~ 2022.

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

# even check if a holiday is in lieu
import chinese_calendar
self.assertFalse(chinese_calendar.is_in_lieu(datetime.date(2006, 1, 1)))
self.assertTrue(chinese_calendar.is_in_lieu(datetime.date(2006, 1, 2)))
```

## Other Languages

If you fail to use Python directly,
you can translate the [constants file][constants.py] to get the complete chinese holiday arrangement.

## Contributing

1. Fork & Clone this project
2. Modify [calendar definition file][scripts/data.py]
3. Run [script][scripts/__init__.py] to generate the [constants file][constants.py]
4. Create a PR

[constants.py]: https://github.com/LKI/chinese-calendar/blob/master/chinese_calendar/constants.py
[scripts/data.py]: https://github.com/LKI/chinese-calendar/blob/master/chinese_calendar/scripts/data.py
[scripts/__init__.py]: https://github.com/LKI/chinese-calendar/blob/master/chinese_calendar/scripts/__init__.py
