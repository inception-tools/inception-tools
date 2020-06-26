"""
    __init__.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    The :py:mod:`test_package_name` package contains the root-level
    distributable source code for the `test_package_name` project.

    ~~~~~~~~~~~~~~~~~~~~~~~

    Unpublished Copyright 1900 test_author. All Rights Reserved.

"""

__author__ = 'test_author'

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('test_package_name').version
except DistributionNotFound:
    __version__ = 'unknown'
