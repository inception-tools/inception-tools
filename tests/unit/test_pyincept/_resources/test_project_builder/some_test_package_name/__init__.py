"""
    __init__.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    The :py:mod:`some_test_package_name` package contains the root-level
    distributable source code for the `some_test_package_name` project.

    ~~~~~~~~~~~~~~~~~~~~~~~

    Unpublished Copyright 2020 some_test_author. All Rights Reserved.

"""

__author__ = 'some_test_author'

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('some_test_package_name').version
except DistributionNotFound:
    __version__ = 'unknown'
