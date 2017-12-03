# Chinese Calendar

[![Package](https://img.shields.io/pypi/v/chinesecalendar.svg)](https://pypi.python.org/pypi/chinesecalendar)
[![Travis](https://img.shields.io/travis/LKI/chinese-calendar.svg)](https://travis-ci.org/LKI/chinese-calendar)
[![Codecov](https://img.shields.io/codecov/c/github/LKI/chinese-calendar.svg)](http://codecov.io/github/LKI/chinese-calendar?branch=master)
[![License](https://img.shields.io/github/license/LKI/chinese-calendar.svg)](https://github.com/LKI/chinese-calendar/blob/master/LICENSE)
[![README](https://img.shields.io/badge/简介-中文-brightgreen.svg)](https://github.com/LKI/chinese-calendar/blob/master/README.md)

Check if some date is workday or holiday in China.
Support 2016 ~ 2017 currently.
Available in Python2 and Python3.

## Installation

```
pip install chinesecalendar
```

## Sample

``` python
import datetime

from chinese_calendar.utils import is_workday, is_holiday

march_first = datetime.date(2017, 5, 1)

print(is_workday(march_first))  # False

print(is_holiday(march_first))  # True
```

