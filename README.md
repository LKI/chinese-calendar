# 中国节假日 [En](/README-en.md)

获取某年某月某一天是不是工作日/节假日。
兼容 Python2 与 Python3.

``` python
import datetime

from chinese_calendar.utils import is_workday, is_holiday

march_first = datetime.date(2017, 5, 1)

print(is_workday(march_first))  # False

print(is_holiday(march_first))  # True
```

