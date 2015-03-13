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
    include_package_data=True,
    install_requires=[
        "Django==1.7.4",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
    ]
)
