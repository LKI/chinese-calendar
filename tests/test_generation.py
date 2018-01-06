# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from chinese_calendar.scripts import generate_constants, get_constants_file_path


class GenerationTests(unittest.TestCase):
    def test_generate_constants(self):
        file_path = get_constants_file_path()
        with open(file_path, 'rb') as f:
            before = f.read()
        generate_constants()
        with open(file_path, 'rb') as f:
            after = f.read()
        self.assertEqual(before, after)
