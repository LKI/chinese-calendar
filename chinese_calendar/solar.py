# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from enum import Enum


class SolarTerm(Enum):
    def __new__(cls, chinese):
        obj = object.__new__(cls)
        obj._value_ = chinese
        obj.chinese = chinese
        return obj

    LICHUN = '立春'
    YUSHUI = '雨水'
    JINGZHE = '惊蛰'
    CHUNFEN = '春分'
    QINGMING = '清明'
    GUYU = '谷雨'
    LIXIA = '立夏'
    XIAOMAN = '小满'
    MANGZHONG = '芒种'
    XIAZHI = '夏至'
    XIAOSHU = '小暑'
    DASHU = '大暑'
    LIQIU = '立秋'
    CHUSHU = '处暑'
    BAILU = '白露'
    QIUFEN = '秋分'
    HANLU = '寒露'
    SHUANGJIANG = '霜降'
    LIDONG = '立冬'
    XIAOXUE = '小雪'
    DAXUE = '大雪'
    DONGZHI = '冬至'
    XIAOHAN = '小寒'
    DAHAN = '大寒'
