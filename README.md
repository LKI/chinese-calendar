# 中国节假日

[![Package](https://img.shields.io/pypi/v/chinesecalendar.svg)](https://pypi.python.org/pypi/chinesecalendar)
[![Travis](https://img.shields.io/travis/LKI/chinese-calendar.svg)](https://travis-ci.org/LKI/chinese-calendar)
[![License](https://img.shields.io/github/license/LKI/chinese-calendar.svg)](https://github.com/LKI/chinese-calendar/blob/master/LICENSE)
[![README](https://img.shields.io/badge/README-English-brightgreen.svg)](https://github.com/LKI/chinese-calendar/blob/master/README.en.md)

判断某年某月某一天是不是工作日/节假日。
支持 2004年 至 2021年，包括 2020年 的春节延长。

## 安装

```
pip install chinesecalendar
```

## 样例

``` python
import datetime

# 判断 2018年4月30号 是不是节假日
from chinese_calendar import is_workday, is_holiday
april_last = datetime.date(2018, 4, 30)
self.assertFalse(is_workday(april_last))
self.assertTrue(is_holiday(april_last))

# 或者在判断的同时，获取节日名
import chinese_calendar as calendar  # 也可以这样 import
on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
self.assertTrue(on_holiday)
self.assertEqual(calendar.Holiday.labour_day.value, holiday_name)

# 还能判断法定节假日是不是调休
import chinese_calendar
self.assertFalse(chinese_calendar.is_in_lieu(datetime.date(2006, 1, 1)))
self.assertTrue(chinese_calendar.is_in_lieu(datetime.date(2006, 1, 2)))
```

## 其它语言

假如你没法使用Python，
你也可以转译现成的[常量文件][constants.py]来获取最全的节假日安排表。

## 贡献代码

1. Fork + Clone 项目到本地
2. 修改[节假日定义][scripts/data.py]
3. 执行[脚本][scripts/__init__.py]自动生成[常量文件][constants.py]
4. 提交PR

[constants.py]: https://github.com/LKI/chinese-calendar/blob/master/chinese_calendar/constants.py
[scripts/data.py]: https://github.com/LKI/chinese-calendar/blob/master/chinese_calendar/scripts/data.py
[scripts/__init__.py]: https://github.com/LKI/chinese-calendar/blob/master/chinese_calendar/scripts/__init__.py
