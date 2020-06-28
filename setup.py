#!/usr/bin/env python
"""
    setup.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    Package distribution file for the pyincept library.

    ~~~~~~~~~~~~~~~~~~~~~~~

    Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

import os

import setuptools


if __name__ == '__main__':
    # allow setup.py to run from another directory
    dir_ = os.path.abspath(os.path.join(__file__, os.pardir))
    os.chdir(dir_)
    setuptools.setup()
