#!/usr/bin/env python
"""
    setup.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    Package distribution file for the pyincept package.
    ~~~~~~~~~~~~~~~~~~~~~~~
    Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

import os

import setuptools

_dir = os.path.abspath(os.path.dirname(__file__))

setup_params = dict(
    name='pyincept',
    version='0.0.1',
    packages=setuptools.find_packages(exclude=['tests*']),
    entry_points={
        "console_scripts": [
            "incept = pyincept.incept:main",
        ],
    },
    scripts=[],
    install_requires=(
        'click',
        'jinja',
    ),
    tests_require=(
        'pyhamcrest',
        'pytest',
    ),
    setup_requires=(
        'pytest-runner',
        'wheel',
    ),
    package_data={
        '': ['*.txt', '*.rst', '*.cfg'],
    },
    include_package_data=True,
    author='Andrew van Herick',
    author_email='avanherick@gmail.com',
    license="Apache Software License",
    description='A lightweight package for creating Python project templates.',
    long_description=open('README.rst').read(),
    extras_require={},
    classifiers=(
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        # Prevents upload to PyPI, because it is not one of the known
        # classifiers.
        'Private :: Do Not Upload',
    ),
)

if __name__ == '__main__':
    # allow setup.py to run from another directory
    os.chdir(_dir)
    setuptools.setup(**setup_params)
