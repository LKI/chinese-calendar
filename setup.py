# -*- coding: utf-8 -*-
from setuptools import setup

with open('requirements.txt') as f:
    requirements = [_.strip() for _ in f.readlines() if _]

long_description = 'check if some day is holiday in China'
try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    pass

setup(
    name='chinesecalendar',
    version='1.2.2',
    description='check if some day is holiday in China',
    long_description=long_description,
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/LKI/chinese-calendar',
    license='MIT License',
    packages=['chinese_calendar'],
    install_requires=requirements,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
