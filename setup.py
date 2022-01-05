#!/usr/bin/env python
"""
    setup.py
    ~~~~~~~~

    Package distribution file for the inception_tools library.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os

import setuptools

if __name__ == "__main__":
    # allow setup.py to run from another directory
    dir_ = os.path.abspath(os.path.join(__file__, os.pardir))
    os.chdir(dir_)
    setuptools.setup()
