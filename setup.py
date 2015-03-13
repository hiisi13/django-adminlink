#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='django-adminlink',
    version='0.1.0',
    description="""Simple template tag that allows you to create links to your model's change form directly from template""",
    author='Dmitry Kozhedubov',
    author_email='dmitry-kozhedubov@yandex.ru',
    url='https://github.com/hiisi13/django-adminlink',
    packages=[
        'adminlink',
    ],
    include_package_data=True,
    install_requires=[
        'Django==1.7.4',
    ],
    license="MIT",
    zip_safe=False,
    keywords='django-management-audit',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
