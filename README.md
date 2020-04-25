# 中国节假日

[![Package](https://img.shields.io/pypi/v/chinesecalendar.svg)](https://pypi.python.org/pypi/chinesecalendar)
[![Travis](https://img.shields.io/travis/LKI/chinese-calendar.svg)](https://travis-ci.org/LKI/chinese-calendar)
[![License](https://img.shields.io/github/license/LKI/chinese-calendar.svg)](https://github.com/LKI/chinese-calendar/blob/master/LICENSE)
[![README](https://img.shields.io/badge/README-English-brightgreen.svg)](https://github.com/LKI/chinese-calendar/blob/master/README.en.md)

判断某年某月某一天是不是工作日/节假日。
支持 2004年 至 2020年，包括 2020年 的春节延长。
兼容 Python2 与 Python3.

> [武汉加油！](https://wuhan2020.github.io/)

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
print(is_workday(april_last))
print(is_holiday(april_last))

# 或者在判断的同时，获取节日名
import chinese_calendar as calendar  # 也可以这样 import
on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
print(on_holiday)
print(calendar.Holiday.labour_day.value, holiday_name)

# 还能判断法定节假日是不是调休
import chinese_calendar
print(chinese_calendar.is_in_lieu(datetime.date(2020, 4, 26)))
print(chinese_calendar.is_in_lieu(datetime.date(2020, 5, 1)))
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
