#!/usr/bin/env python
"""
    setup.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    Package distribution file for the test_package_name library.

    ~~~~~~~~~~~~~~~~~~~~~~~

    Unpublished Copyright 1900 test_author. All Rights Reserved.
"""

__author__ = 'test_author'

import os

import setuptools


def _read_file(file_path):
    with open(file_path) as f:
        return f.read()


_dir = os.path.abspath(os.path.join(__file__, os.pardir))

setup_params = dict(
    name='test_package_name',
    version='0.0.0',
    packages=setuptools.find_packages(exclude=['tests*']),
    entry_points={
        # If you will have command line entry points that will be installed,
        # you can uncomment the lines below to make them available through
        # the distribution.
        "console_scripts": [
            "test_package_name = test_package_name.test_package_name:main",
        ],
    },
    scripts=[],
    install_requires=(
        'click',
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
    author='test_author',
    author_email='test_author_email',
    license="Apache Software License",
    description='A lightweight package for creating Python project templates.',
    long_description=open('README.rst').read(),
    extras_require={},
    classifiers=(
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        # Prevents upload to PyPI, because it is not one of the known
        # classifiers.  This can and should be removed if you will
        # be distributing you package to PyPI.
        'Private :: Do Not Upload',
    ),
)

if __name__ == '__main__':
    # allow setup.py to run from another directory
    os.chdir(_dir)
    setuptools.setup(**setup_params)
