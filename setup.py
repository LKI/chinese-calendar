# -*- coding: utf-8 -*-
import pypandoc
from setuptools import setup

with open('requirements.txt') as f:
    requirements = [_.strip() for _ in f.readlines() if _]

setup(
    name='chinesecalendar',
    version='1.0.3',
    description='check if some day is holiday in China',
    long_description=pypandoc.convert('README.md', 'rst'),
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/LKI/chinese-calendar',
    license='MIT License',
    packages=['chinese_calendar'],
    install_requires=requirements,
)
