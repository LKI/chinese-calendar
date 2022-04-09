# -*- coding: utf-8 -*-
import datetime
import unittest

import chinese_calendar


class SolarTermTests(unittest.TestCase):
    def test_get_solar_terms(self):
        start = datetime.date(2000, 1, 1)
        end = datetime.date(2000, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2000, 1, 6), "小寒"),
            (datetime.date(2000, 1, 21), "大寒"),
            (datetime.date(2000, 2, 4), "立春"),
            (datetime.date(2000, 2, 19), "雨水"),
            (datetime.date(2000, 3, 5), "惊蛰"),
            (datetime.date(2000, 3, 20), "春分"),
            (datetime.date(2000, 4, 4), "清明"),
            (datetime.date(2000, 4, 20), "谷雨"),
            (datetime.date(2000, 5, 5), "立夏"),
            (datetime.date(2000, 5, 21), "小满"),
            (datetime.date(2000, 6, 5), "芒种"),
            (datetime.date(2000, 6, 21), "夏至"),
            (datetime.date(2000, 7, 7), "小暑"),
            (datetime.date(2000, 7, 22), "大暑"),
            (datetime.date(2000, 8, 7), "立秋"),
            (datetime.date(2000, 8, 23), "处暑"),
            (datetime.date(2000, 9, 7), "白露"),
            (datetime.date(2000, 9, 23), "秋分"),
            (datetime.date(2000, 10, 8), "寒露"),
            (datetime.date(2000, 10, 23), "霜降"),
            (datetime.date(2000, 11, 7), "立冬"),
            (datetime.date(2000, 11, 22), "小雪"),
            (datetime.date(2000, 12, 7), "大雪"),
            (datetime.date(2000, 12, 21), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2004, 1, 1)
        end = datetime.date(2004, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2004, 1, 6), "小寒"),
            (datetime.date(2004, 1, 21), "大寒"),
            (datetime.date(2004, 2, 4), "立春"),
            (datetime.date(2004, 2, 19), "雨水"),
            (datetime.date(2004, 3, 5), "惊蛰"),
            (datetime.date(2004, 3, 20), "春分"),
            (datetime.date(2004, 4, 4), "清明"),
            (datetime.date(2004, 4, 20), "谷雨"),
            (datetime.date(2004, 5, 5), "立夏"),
            (datetime.date(2004, 5, 21), "小满"),
            (datetime.date(2004, 6, 5), "芒种"),
            (datetime.date(2004, 6, 21), "夏至"),
            (datetime.date(2004, 7, 7), "小暑"),
            (datetime.date(2004, 7, 22), "大暑"),
            (datetime.date(2004, 8, 7), "立秋"),
            (datetime.date(2004, 8, 23), "处暑"),
            (datetime.date(2004, 9, 7), "白露"),
            (datetime.date(2004, 9, 23), "秋分"),
            (datetime.date(2004, 10, 8), "寒露"),
            (datetime.date(2004, 10, 23), "霜降"),
            (datetime.date(2004, 11, 7), "立冬"),
            (datetime.date(2004, 11, 22), "小雪"),
            (datetime.date(2004, 12, 7), "大雪"),
            (datetime.date(2004, 12, 21), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2005, 1, 1)
        end = datetime.date(2005, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2005, 1, 5), "小寒"),
            (datetime.date(2005, 1, 20), "大寒"),
            (datetime.date(2005, 2, 4), "立春"),
            (datetime.date(2005, 2, 18), "雨水"),
            (datetime.date(2005, 3, 5), "惊蛰"),
            (datetime.date(2005, 3, 20), "春分"),
            (datetime.date(2005, 4, 5), "清明"),
            (datetime.date(2005, 4, 20), "谷雨"),
            (datetime.date(2005, 5, 5), "立夏"),
            (datetime.date(2005, 5, 21), "小满"),
            (datetime.date(2005, 6, 5), "芒种"),
            (datetime.date(2005, 6, 21), "夏至"),
            (datetime.date(2005, 7, 7), "小暑"),
            (datetime.date(2005, 7, 23), "大暑"),
            (datetime.date(2005, 8, 7), "立秋"),
            (datetime.date(2005, 8, 23), "处暑"),
            (datetime.date(2005, 9, 7), "白露"),
            (datetime.date(2005, 9, 23), "秋分"),
            (datetime.date(2005, 10, 8), "寒露"),
            (datetime.date(2005, 10, 23), "霜降"),
            (datetime.date(2005, 11, 7), "立冬"),
            (datetime.date(2005, 11, 22), "小雪"),
            (datetime.date(2005, 12, 7), "大雪"),
            (datetime.date(2005, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2006, 1, 1)
        end = datetime.date(2006, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2006, 1, 5), "小寒"),
            (datetime.date(2006, 1, 20), "大寒"),
            (datetime.date(2006, 2, 4), "立春"),
            (datetime.date(2006, 2, 19), "雨水"),
            (datetime.date(2006, 3, 6), "惊蛰"),
            (datetime.date(2006, 3, 21), "春分"),
            (datetime.date(2006, 4, 5), "清明"),
            (datetime.date(2006, 4, 20), "谷雨"),
            (datetime.date(2006, 5, 5), "立夏"),
            (datetime.date(2006, 5, 21), "小满"),
            (datetime.date(2006, 6, 6), "芒种"),
            (datetime.date(2006, 6, 21), "夏至"),
            (datetime.date(2006, 7, 7), "小暑"),
            (datetime.date(2006, 7, 23), "大暑"),
            (datetime.date(2006, 8, 7), "立秋"),
            (datetime.date(2006, 8, 23), "处暑"),
            (datetime.date(2006, 9, 8), "白露"),
            (datetime.date(2006, 9, 23), "秋分"),
            (datetime.date(2006, 10, 8), "寒露"),
            (datetime.date(2006, 10, 23), "霜降"),
            (datetime.date(2006, 11, 7), "立冬"),
            (datetime.date(2006, 11, 22), "小雪"),
            (datetime.date(2006, 12, 7), "大雪"),
            (datetime.date(2006, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2007, 1, 1)
        end = datetime.date(2007, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2007, 1, 6), "小寒"),
            (datetime.date(2007, 1, 20), "大寒"),
            (datetime.date(2007, 2, 4), "立春"),
            (datetime.date(2007, 2, 19), "雨水"),
            (datetime.date(2007, 3, 6), "惊蛰"),
            (datetime.date(2007, 3, 21), "春分"),
            (datetime.date(2007, 4, 5), "清明"),
            (datetime.date(2007, 4, 20), "谷雨"),
            (datetime.date(2007, 5, 6), "立夏"),
            (datetime.date(2007, 5, 21), "小满"),
            (datetime.date(2007, 6, 6), "芒种"),
            (datetime.date(2007, 6, 22), "夏至"),
            (datetime.date(2007, 7, 7), "小暑"),
            (datetime.date(2007, 7, 23), "大暑"),
            (datetime.date(2007, 8, 8), "立秋"),
            (datetime.date(2007, 8, 23), "处暑"),
            (datetime.date(2007, 9, 8), "白露"),
            (datetime.date(2007, 9, 23), "秋分"),
            (datetime.date(2007, 10, 9), "寒露"),
            (datetime.date(2007, 10, 24), "霜降"),
            (datetime.date(2007, 11, 8), "立冬"),
            (datetime.date(2007, 11, 23), "小雪"),
            (datetime.date(2007, 12, 7), "大雪"),
            (datetime.date(2007, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2008, 1, 1)
        end = datetime.date(2008, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2008, 1, 6), "小寒"),
            (datetime.date(2008, 1, 21), "大寒"),
            (datetime.date(2008, 2, 4), "立春"),
            (datetime.date(2008, 2, 19), "雨水"),
            (datetime.date(2008, 3, 5), "惊蛰"),
            (datetime.date(2008, 3, 20), "春分"),
            (datetime.date(2008, 4, 4), "清明"),
            (datetime.date(2008, 4, 20), "谷雨"),
            (datetime.date(2008, 5, 5), "立夏"),
            (datetime.date(2008, 5, 21), "小满"),
            (datetime.date(2008, 6, 5), "芒种"),
            (datetime.date(2008, 6, 21), "夏至"),
            (datetime.date(2008, 7, 7), "小暑"),
            (datetime.date(2008, 7, 22), "大暑"),
            (datetime.date(2008, 8, 7), "立秋"),
            (datetime.date(2008, 8, 23), "处暑"),
            (datetime.date(2008, 9, 7), "白露"),
            (datetime.date(2008, 9, 22), "秋分"),
            (datetime.date(2008, 10, 8), "寒露"),
            (datetime.date(2008, 10, 23), "霜降"),
            (datetime.date(2008, 11, 7), "立冬"),
            (datetime.date(2008, 11, 22), "小雪"),
            (datetime.date(2008, 12, 7), "大雪"),
            (datetime.date(2008, 12, 21), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2009, 1, 1)
        end = datetime.date(2009, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2009, 1, 5), "小寒"),
            (datetime.date(2009, 1, 20), "大寒"),
            (datetime.date(2009, 2, 4), "立春"),
            (datetime.date(2009, 2, 18), "雨水"),
            (datetime.date(2009, 3, 5), "惊蛰"),
            (datetime.date(2009, 3, 20), "春分"),
            (datetime.date(2009, 4, 4), "清明"),
            (datetime.date(2009, 4, 20), "谷雨"),
            (datetime.date(2009, 5, 5), "立夏"),
            (datetime.date(2009, 5, 21), "小满"),
            (datetime.date(2009, 6, 5), "芒种"),
            (datetime.date(2009, 6, 21), "夏至"),
            (datetime.date(2009, 7, 7), "小暑"),
            (datetime.date(2009, 7, 23), "大暑"),
            (datetime.date(2009, 8, 7), "立秋"),
            (datetime.date(2009, 8, 23), "处暑"),
            (datetime.date(2009, 9, 7), "白露"),
            (datetime.date(2009, 9, 23), "秋分"),
            (datetime.date(2009, 10, 8), "寒露"),
            (datetime.date(2009, 10, 23), "霜降"),
            (datetime.date(2009, 11, 7), "立冬"),
            (datetime.date(2009, 11, 22), "小雪"),
            (datetime.date(2009, 12, 7), "大雪"),
            (datetime.date(2009, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2010, 1, 1)
        end = datetime.date(2010, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2010, 1, 5), "小寒"),
            (datetime.date(2010, 1, 20), "大寒"),
            (datetime.date(2010, 2, 4), "立春"),
            (datetime.date(2010, 2, 19), "雨水"),
            (datetime.date(2010, 3, 6), "惊蛰"),
            (datetime.date(2010, 3, 21), "春分"),
            (datetime.date(2010, 4, 5), "清明"),
            (datetime.date(2010, 4, 20), "谷雨"),
            (datetime.date(2010, 5, 5), "立夏"),
            (datetime.date(2010, 5, 21), "小满"),
            (datetime.date(2010, 6, 6), "芒种"),
            (datetime.date(2010, 6, 21), "夏至"),
            (datetime.date(2010, 7, 7), "小暑"),
            (datetime.date(2010, 7, 23), "大暑"),
            (datetime.date(2010, 8, 7), "立秋"),
            (datetime.date(2010, 8, 23), "处暑"),
            (datetime.date(2010, 9, 8), "白露"),
            (datetime.date(2010, 9, 23), "秋分"),
            (datetime.date(2010, 10, 8), "寒露"),
            (datetime.date(2010, 10, 23), "霜降"),
            (datetime.date(2010, 11, 7), "立冬"),
            (datetime.date(2010, 11, 22), "小雪"),
            (datetime.date(2010, 12, 7), "大雪"),
            (datetime.date(2010, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2011, 1, 1)
        end = datetime.date(2011, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2011, 1, 6), "小寒"),
            (datetime.date(2011, 1, 20), "大寒"),
            (datetime.date(2011, 2, 4), "立春"),
            (datetime.date(2011, 2, 19), "雨水"),
            (datetime.date(2011, 3, 6), "惊蛰"),
            (datetime.date(2011, 3, 21), "春分"),
            (datetime.date(2011, 4, 5), "清明"),
            (datetime.date(2011, 4, 20), "谷雨"),
            (datetime.date(2011, 5, 6), "立夏"),
            (datetime.date(2011, 5, 21), "小满"),
            (datetime.date(2011, 6, 6), "芒种"),
            (datetime.date(2011, 6, 22), "夏至"),
            (datetime.date(2011, 7, 7), "小暑"),
            (datetime.date(2011, 7, 23), "大暑"),
            (datetime.date(2011, 8, 8), "立秋"),
            (datetime.date(2011, 8, 23), "处暑"),
            (datetime.date(2011, 9, 8), "白露"),
            (datetime.date(2011, 9, 23), "秋分"),
            (datetime.date(2011, 10, 8), "寒露"),
            (datetime.date(2011, 10, 24), "霜降"),
            (datetime.date(2011, 11, 8), "立冬"),
            (datetime.date(2011, 11, 23), "小雪"),
            (datetime.date(2011, 12, 7), "大雪"),
            (datetime.date(2011, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2012, 1, 1)
        end = datetime.date(2012, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2012, 1, 6), "小寒"),
            (datetime.date(2012, 1, 21), "大寒"),
            (datetime.date(2012, 2, 4), "立春"),
            (datetime.date(2012, 2, 19), "雨水"),
            (datetime.date(2012, 3, 5), "惊蛰"),
            (datetime.date(2012, 3, 20), "春分"),
            (datetime.date(2012, 4, 4), "清明"),
            (datetime.date(2012, 4, 20), "谷雨"),
            (datetime.date(2012, 5, 5), "立夏"),
            (datetime.date(2012, 5, 20), "小满"),
            (datetime.date(2012, 6, 5), "芒种"),
            (datetime.date(2012, 6, 21), "夏至"),
            (datetime.date(2012, 7, 7), "小暑"),
            (datetime.date(2012, 7, 22), "大暑"),
            (datetime.date(2012, 8, 7), "立秋"),
            (datetime.date(2012, 8, 23), "处暑"),
            (datetime.date(2012, 9, 7), "白露"),
            (datetime.date(2012, 9, 22), "秋分"),
            (datetime.date(2012, 10, 8), "寒露"),
            (datetime.date(2012, 10, 23), "霜降"),
            (datetime.date(2012, 11, 7), "立冬"),
            (datetime.date(2012, 11, 22), "小雪"),
            (datetime.date(2012, 12, 7), "大雪"),
            (datetime.date(2012, 12, 21), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2013, 1, 1)
        end = datetime.date(2013, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2013, 1, 5), "小寒"),
            (datetime.date(2013, 1, 20), "大寒"),
            (datetime.date(2013, 2, 4), "立春"),
            (datetime.date(2013, 2, 18), "雨水"),
            (datetime.date(2013, 3, 5), "惊蛰"),
            (datetime.date(2013, 3, 20), "春分"),
            (datetime.date(2013, 4, 4), "清明"),
            (datetime.date(2013, 4, 20), "谷雨"),
            (datetime.date(2013, 5, 5), "立夏"),
            (datetime.date(2013, 5, 21), "小满"),
            (datetime.date(2013, 6, 5), "芒种"),
            (datetime.date(2013, 6, 21), "夏至"),
            (datetime.date(2013, 7, 7), "小暑"),
            (datetime.date(2013, 7, 22), "大暑"),
            (datetime.date(2013, 8, 7), "立秋"),
            (datetime.date(2013, 8, 23), "处暑"),
            (datetime.date(2013, 9, 7), "白露"),
            (datetime.date(2013, 9, 23), "秋分"),
            (datetime.date(2013, 10, 8), "寒露"),
            (datetime.date(2013, 10, 23), "霜降"),
            (datetime.date(2013, 11, 7), "立冬"),
            (datetime.date(2013, 11, 22), "小雪"),
            (datetime.date(2013, 12, 7), "大雪"),
            (datetime.date(2013, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2014, 1, 1)
        end = datetime.date(2014, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2014, 1, 5), "小寒"),
            (datetime.date(2014, 1, 20), "大寒"),
            (datetime.date(2014, 2, 4), "立春"),
            (datetime.date(2014, 2, 19), "雨水"),
            (datetime.date(2014, 3, 6), "惊蛰"),
            (datetime.date(2014, 3, 21), "春分"),
            (datetime.date(2014, 4, 5), "清明"),
            (datetime.date(2014, 4, 20), "谷雨"),
            (datetime.date(2014, 5, 5), "立夏"),
            (datetime.date(2014, 5, 21), "小满"),
            (datetime.date(2014, 6, 6), "芒种"),
            (datetime.date(2014, 6, 21), "夏至"),
            (datetime.date(2014, 7, 7), "小暑"),
            (datetime.date(2014, 7, 23), "大暑"),
            (datetime.date(2014, 8, 7), "立秋"),
            (datetime.date(2014, 8, 23), "处暑"),
            (datetime.date(2014, 9, 8), "白露"),
            (datetime.date(2014, 9, 23), "秋分"),
            (datetime.date(2014, 10, 8), "寒露"),
            (datetime.date(2014, 10, 23), "霜降"),
            (datetime.date(2014, 11, 7), "立冬"),
            (datetime.date(2014, 11, 22), "小雪"),
            (datetime.date(2014, 12, 7), "大雪"),
            (datetime.date(2014, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2015, 1, 1)
        end = datetime.date(2015, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2015, 1, 6), "小寒"),
            (datetime.date(2015, 1, 20), "大寒"),
            (datetime.date(2015, 2, 4), "立春"),
            (datetime.date(2015, 2, 19), "雨水"),
            (datetime.date(2015, 3, 6), "惊蛰"),
            (datetime.date(2015, 3, 21), "春分"),
            (datetime.date(2015, 4, 5), "清明"),
            (datetime.date(2015, 4, 20), "谷雨"),
            (datetime.date(2015, 5, 6), "立夏"),
            (datetime.date(2015, 5, 21), "小满"),
            (datetime.date(2015, 6, 6), "芒种"),
            (datetime.date(2015, 6, 22), "夏至"),
            (datetime.date(2015, 7, 7), "小暑"),
            (datetime.date(2015, 7, 23), "大暑"),
            (datetime.date(2015, 8, 8), "立秋"),
            (datetime.date(2015, 8, 23), "处暑"),
            (datetime.date(2015, 9, 8), "白露"),
            (datetime.date(2015, 9, 23), "秋分"),
            (datetime.date(2015, 10, 8), "寒露"),
            (datetime.date(2015, 10, 24), "霜降"),
            (datetime.date(2015, 11, 8), "立冬"),
            (datetime.date(2015, 11, 22), "小雪"),
            (datetime.date(2015, 12, 7), "大雪"),
            (datetime.date(2015, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2016, 1, 1)
        end = datetime.date(2016, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2016, 1, 6), "小寒"),
            (datetime.date(2016, 1, 20), "大寒"),
            (datetime.date(2016, 2, 4), "立春"),
            (datetime.date(2016, 2, 19), "雨水"),
            (datetime.date(2016, 3, 5), "惊蛰"),
            (datetime.date(2016, 3, 20), "春分"),
            (datetime.date(2016, 4, 4), "清明"),
            (datetime.date(2016, 4, 19), "谷雨"),
            (datetime.date(2016, 5, 5), "立夏"),
            (datetime.date(2016, 5, 20), "小满"),
            (datetime.date(2016, 6, 5), "芒种"),
            (datetime.date(2016, 6, 21), "夏至"),
            (datetime.date(2016, 7, 7), "小暑"),
            (datetime.date(2016, 7, 22), "大暑"),
            (datetime.date(2016, 8, 7), "立秋"),
            (datetime.date(2016, 8, 23), "处暑"),
            (datetime.date(2016, 9, 7), "白露"),
            (datetime.date(2016, 9, 22), "秋分"),
            (datetime.date(2016, 10, 8), "寒露"),
            (datetime.date(2016, 10, 23), "霜降"),
            (datetime.date(2016, 11, 7), "立冬"),
            (datetime.date(2016, 11, 22), "小雪"),
            (datetime.date(2016, 12, 7), "大雪"),
            (datetime.date(2016, 12, 21), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2017, 1, 1)
        end = datetime.date(2017, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2017, 1, 5), "小寒"),
            (datetime.date(2017, 1, 20), "大寒"),
            (datetime.date(2017, 2, 3), "立春"),
            (datetime.date(2017, 2, 18), "雨水"),
            (datetime.date(2017, 3, 5), "惊蛰"),
            (datetime.date(2017, 3, 20), "春分"),
            (datetime.date(2017, 4, 4), "清明"),
            (datetime.date(2017, 4, 20), "谷雨"),
            (datetime.date(2017, 5, 5), "立夏"),
            (datetime.date(2017, 5, 21), "小满"),
            (datetime.date(2017, 6, 5), "芒种"),
            (datetime.date(2017, 6, 21), "夏至"),
            (datetime.date(2017, 7, 7), "小暑"),
            (datetime.date(2017, 7, 22), "大暑"),
            (datetime.date(2017, 8, 7), "立秋"),
            (datetime.date(2017, 8, 23), "处暑"),
            (datetime.date(2017, 9, 7), "白露"),
            (datetime.date(2017, 9, 23), "秋分"),
            (datetime.date(2017, 10, 8), "寒露"),
            (datetime.date(2017, 10, 23), "霜降"),
            (datetime.date(2017, 11, 7), "立冬"),
            (datetime.date(2017, 11, 22), "小雪"),
            (datetime.date(2017, 12, 7), "大雪"),
            (datetime.date(2017, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2018, 1, 1)
        end = datetime.date(2018, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2018, 1, 5), "小寒"),
            (datetime.date(2018, 1, 20), "大寒"),
            (datetime.date(2018, 2, 4), "立春"),
            (datetime.date(2018, 2, 19), "雨水"),
            (datetime.date(2018, 3, 5), "惊蛰"),
            (datetime.date(2018, 3, 21), "春分"),
            (datetime.date(2018, 4, 5), "清明"),
            (datetime.date(2018, 4, 20), "谷雨"),
            (datetime.date(2018, 5, 5), "立夏"),
            (datetime.date(2018, 5, 21), "小满"),
            (datetime.date(2018, 6, 6), "芒种"),
            (datetime.date(2018, 6, 21), "夏至"),
            (datetime.date(2018, 7, 7), "小暑"),
            (datetime.date(2018, 7, 23), "大暑"),
            (datetime.date(2018, 8, 7), "立秋"),
            (datetime.date(2018, 8, 23), "处暑"),
            (datetime.date(2018, 9, 8), "白露"),
            (datetime.date(2018, 9, 23), "秋分"),
            (datetime.date(2018, 10, 8), "寒露"),
            (datetime.date(2018, 10, 23), "霜降"),
            (datetime.date(2018, 11, 7), "立冬"),
            (datetime.date(2018, 11, 22), "小雪"),
            (datetime.date(2018, 12, 7), "大雪"),
            (datetime.date(2018, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2019, 1, 1)
        end = datetime.date(2019, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2019, 1, 5), "小寒"),
            (datetime.date(2019, 1, 20), "大寒"),
            (datetime.date(2019, 2, 4), "立春"),
            (datetime.date(2019, 2, 19), "雨水"),
            (datetime.date(2019, 3, 6), "惊蛰"),
            (datetime.date(2019, 3, 21), "春分"),
            (datetime.date(2019, 4, 5), "清明"),
            (datetime.date(2019, 4, 20), "谷雨"),
            (datetime.date(2019, 5, 6), "立夏"),
            (datetime.date(2019, 5, 21), "小满"),
            (datetime.date(2019, 6, 6), "芒种"),
            (datetime.date(2019, 6, 21), "夏至"),
            (datetime.date(2019, 7, 7), "小暑"),
            (datetime.date(2019, 7, 23), "大暑"),
            (datetime.date(2019, 8, 8), "立秋"),
            (datetime.date(2019, 8, 23), "处暑"),
            (datetime.date(2019, 9, 8), "白露"),
            (datetime.date(2019, 9, 23), "秋分"),
            (datetime.date(2019, 10, 8), "寒露"),
            (datetime.date(2019, 10, 24), "霜降"),
            (datetime.date(2019, 11, 8), "立冬"),
            (datetime.date(2019, 11, 22), "小雪"),
            (datetime.date(2019, 12, 7), "大雪"),
            (datetime.date(2019, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2020, 1, 1)
        end = datetime.date(2020, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2020, 1, 6), "小寒"),
            (datetime.date(2020, 1, 20), "大寒"),
            (datetime.date(2020, 2, 4), "立春"),
            (datetime.date(2020, 2, 19), "雨水"),
            (datetime.date(2020, 3, 5), "惊蛰"),
            (datetime.date(2020, 3, 20), "春分"),
            (datetime.date(2020, 4, 4), "清明"),
            (datetime.date(2020, 4, 19), "谷雨"),
            (datetime.date(2020, 5, 5), "立夏"),
            (datetime.date(2020, 5, 20), "小满"),
            (datetime.date(2020, 6, 5), "芒种"),
            (datetime.date(2020, 6, 21), "夏至"),
            (datetime.date(2020, 7, 6), "小暑"),
            (datetime.date(2020, 7, 22), "大暑"),
            (datetime.date(2020, 8, 7), "立秋"),
            (datetime.date(2020, 8, 22), "处暑"),
            (datetime.date(2020, 9, 7), "白露"),
            (datetime.date(2020, 9, 22), "秋分"),
            (datetime.date(2020, 10, 8), "寒露"),
            (datetime.date(2020, 10, 23), "霜降"),
            (datetime.date(2020, 11, 7), "立冬"),
            (datetime.date(2020, 11, 22), "小雪"),
            (datetime.date(2020, 12, 7), "大雪"),
            (datetime.date(2020, 12, 21), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2021, 1, 1)
        end = datetime.date(2021, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2021, 1, 5), "小寒"),
            (datetime.date(2021, 1, 20), "大寒"),
            (datetime.date(2021, 2, 3), "立春"),
            (datetime.date(2021, 2, 18), "雨水"),
            (datetime.date(2021, 3, 5), "惊蛰"),
            (datetime.date(2021, 3, 20), "春分"),
            (datetime.date(2021, 4, 4), "清明"),
            (datetime.date(2021, 4, 20), "谷雨"),
            (datetime.date(2021, 5, 5), "立夏"),
            (datetime.date(2021, 5, 21), "小满"),
            (datetime.date(2021, 6, 5), "芒种"),
            (datetime.date(2021, 6, 21), "夏至"),
            (datetime.date(2021, 7, 7), "小暑"),
            (datetime.date(2021, 7, 22), "大暑"),
            (datetime.date(2021, 8, 7), "立秋"),
            (datetime.date(2021, 8, 23), "处暑"),
            (datetime.date(2021, 9, 7), "白露"),
            (datetime.date(2021, 9, 23), "秋分"),
            (datetime.date(2021, 10, 8), "寒露"),
            (datetime.date(2021, 10, 23), "霜降"),
            (datetime.date(2021, 11, 7), "立冬"),
            (datetime.date(2021, 11, 22), "小雪"),
            (datetime.date(2021, 12, 7), "大雪"),
            (datetime.date(2021, 12, 21), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2022, 1, 1)
        end = datetime.date(2022, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2022, 1, 5), "小寒"),
            (datetime.date(2022, 1, 20), "大寒"),
            (datetime.date(2022, 2, 4), "立春"),
            (datetime.date(2022, 2, 19), "雨水"),
            (datetime.date(2022, 3, 5), "惊蛰"),
            (datetime.date(2022, 3, 20), "春分"),
            (datetime.date(2022, 4, 5), "清明"),
            (datetime.date(2022, 4, 20), "谷雨"),
            (datetime.date(2022, 5, 5), "立夏"),
            (datetime.date(2022, 5, 21), "小满"),
            (datetime.date(2022, 6, 6), "芒种"),
            (datetime.date(2022, 6, 21), "夏至"),
            (datetime.date(2022, 7, 7), "小暑"),
            (datetime.date(2022, 7, 23), "大暑"),
            (datetime.date(2022, 8, 7), "立秋"),
            (datetime.date(2022, 8, 23), "处暑"),
            (datetime.date(2022, 9, 7), "白露"),
            (datetime.date(2022, 9, 23), "秋分"),
            (datetime.date(2022, 10, 8), "寒露"),
            (datetime.date(2022, 10, 23), "霜降"),
            (datetime.date(2022, 11, 7), "立冬"),
            (datetime.date(2022, 11, 22), "小雪"),
            (datetime.date(2022, 12, 7), "大雪"),
            (datetime.date(2022, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2023, 1, 1)
        end = datetime.date(2023, 12, 31)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = [
            (datetime.date(2023, 1, 5), "小寒"),
            (datetime.date(2023, 1, 20), "大寒"),
            (datetime.date(2023, 2, 4), "立春"),
            (datetime.date(2023, 2, 19), "雨水"),
            (datetime.date(2023, 3, 6), "惊蛰"),
            (datetime.date(2023, 3, 21), "春分"),
            (datetime.date(2023, 4, 5), "清明"),
            (datetime.date(2023, 4, 20), "谷雨"),
            (datetime.date(2023, 5, 6), "立夏"),
            (datetime.date(2023, 5, 21), "小满"),
            (datetime.date(2023, 6, 6), "芒种"),
            (datetime.date(2023, 6, 21), "夏至"),
            (datetime.date(2023, 7, 7), "小暑"),
            (datetime.date(2023, 7, 23), "大暑"),
            (datetime.date(2023, 8, 8), "立秋"),
            (datetime.date(2023, 8, 23), "处暑"),
            (datetime.date(2023, 9, 8), "白露"),
            (datetime.date(2023, 9, 23), "秋分"),
            (datetime.date(2023, 10, 8), "寒露"),
            (datetime.date(2023, 10, 24), "霜降"),
            (datetime.date(2023, 11, 8), "立冬"),
            (datetime.date(2023, 11, 22), "小雪"),
            (datetime.date(2023, 12, 7), "大雪"),
            (datetime.date(2023, 12, 22), "冬至"),
        ]
        self.assertEqual(expected, actual)

        start = datetime.date(2023, 1, 6)
        end = datetime.date(2023, 1, 19)
        actual = chinese_calendar.get_solar_terms(start, end)
        expected = []
        self.assertEqual(expected, actual)
