#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of MahewinHubStar.
# https://github.com/hobbestigrou/MahewinHubStar

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Hobbestigrou <hobbestigrou@erakis.eu>

from setuptools import setup, find_packages

setup(
    name='pychargifysimple',
    version='0.4',
    description='Chargify API wrapper.',
    long_description='''
Chargify API wrapper with a web module.
''',
    keywords='chargify, api',
    author='Hobbestigrou',
    author_email='hobbestigrou@erakis.eu',
    url='https://github.com/hobbestigrou/pychargifysimple',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'MechanicalSoup', 'fake-useragent'
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
