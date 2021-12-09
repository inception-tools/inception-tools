"""
    __init__.py
    ~~~~~~~~~~~

    The :py:mod:`inceptiontools` package contains the root-level distributable
    source code for the `inceptiontools` project.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("inceptiontools").version
except pkg_resources.DistributionNotFound:
    __version__ = "unknown"
