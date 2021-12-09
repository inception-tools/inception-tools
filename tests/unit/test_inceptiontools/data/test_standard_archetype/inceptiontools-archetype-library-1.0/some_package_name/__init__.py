"""
some_package_name
~~~~~~~~~~~~~~~~~

The :py:mod:`some_package_name` package contains the root-level distributable
source code for the `some_package_name` project.
"""

__author__ = "some_author"
__copyright__ = "Unpublished Copyright (c) 2000 some_author. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution("some_package_name").version
except DistributionNotFound:
    __version__ = "unknown"
