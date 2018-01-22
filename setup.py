# -*- coding: utf-8 -*-
import pypandoc
from setuptools import setup

setup(
    name='chinesecalendar',
    version='1.0.1',
    description='check if some day is holiday in China',
    long_description=pypandoc.convert('README.md', 'rst'),
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/LKI/chinese-calendar',
    license='MIT License',
    packages=['chinese_calendar'],
)
