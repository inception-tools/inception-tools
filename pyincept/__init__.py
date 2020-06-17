"""
    __init__.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    The :py:mod:`pyincept` package contains the root-level distributable
    source code for the `pyincept` project.
    ~~~~~~~~~~~~~~~~~~~~~~~
    Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
"""
import os

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('pyincept').version
except pkg_resources.DistributionNotFound:
    __version__ = 'unknown'

