"""
    __init__.py
    ~~~~~~~~~~~

    The :py:mod:`inception_tools` package contains the root-level distributable
    source code for the `inception_tools` project.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("inception_tools").version
except pkg_resources.DistributionNotFound:
    __version__ = "unknown"
