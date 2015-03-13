#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="django-adminlink",
    version="0.1.0",
    license='MIT',
    author="Dmitry Kozhedubov",
    author_email="hiisi13@gmail.com",
    packages=[
        "adminlink",
    ],
    install_requires=[
        "Django==1.7.4",
    ],
)
