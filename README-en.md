# Chinese Calendar [中文](/README.md)

Check if some date is workday in China.
Available for Python2 and Python3.

``` python
import datetime

from chinese_calendar.utils import is_workday, is_holiday

march_first = datetime.date(2017, 5, 1)

print(is_workday(march_first))  # False

print(is_holiday(march_first))  # True
```

