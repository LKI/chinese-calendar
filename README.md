# 中国节假日

[![Package](https://img.shields.io/pypi/v/chinesecalendar.svg)](https://pypi.python.org/pypi/chinesecalendar)
[![Travis](https://img.shields.io/travis/LKI/chinese-calendar.svg)](https://travis-ci.org/LKI/chinese-calendar)
[![License](https://img.shields.io/github/license/LKI/chinese-calendar.svg)](https://github.com/LKI/chinese-calendar/blob/master/LICENSE)
[![README](https://img.shields.io/badge/README-English-brightgreen.svg)](https://github.com/LKI/chinese-calendar/blob/master/README.en.md)

判断某年某月某一天是不是工作日/节假日。
目前支持 2016 年至 2018年。
兼容 Python2 与 Python3.

## 安装

```
pip install chinese calendar
```

## 样例

``` python
import datetime

from chinese_calendar.utils import is_workday, is_holiday

march_first = datetime.date(2017, 5, 1)

print(is_workday(march_first))  # False

print(is_holiday(march_first))  # True
```

