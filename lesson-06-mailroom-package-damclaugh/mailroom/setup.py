
#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name = 'mailroom',
    packages = ['mailroom'],
    entry_points = {'console_scripts': ['mailroom=mailroom.cli:main']},)
