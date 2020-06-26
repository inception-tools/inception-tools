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


def _read_file(file_path):
    with open(file_path) as f:
        return f.read()


_dir = os.path.abspath(os.path.join(__file__, os.pardir))

setup_params = dict(
    name='pyincept',
    version='0.0.1',
    packages=setuptools.find_packages(exclude=['tests*']),
    entry_points={
        "console_scripts": [
            "pyincept = pyincept.pyincept:main",
        ],
    },
    scripts=[],
    install_requires=(
        'click',
        'jinja2',
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
        'pyincept': ['_resources/templates/*.jinja'],
    },
    include_package_data=True,
    author='Andrew van Herick',
    author_email='avanherick@gmail.com',
    license="Apache Software License",
    description='A lightweight package for creating Python project templates.',
    long_description=_read_file('README.rst'),
    extras_require={},
    classifiers=(
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        # Prevents upload to PyPI, because it is not one of the known
        # classifiers.
        # 'Private :: Do Not Upload',
    ),
)

if __name__ == '__main__':
    # allow setup.py to run from another directory
    os.chdir(_dir)
    setuptools.setup(**setup_params)
