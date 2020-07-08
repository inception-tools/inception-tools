"""
architype_parameters
~~~~~~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`ArchitypeParameters` along with
supporting classes, functions, and attributes.

Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

from collections import namedtuple

ArchitypeParameters = namedtuple(
    'ArchitypeParameters',
    ('package_name', 'author', 'author_email', 'date')
)
"""
A container class that responsible for grouping the parameters used to create a
project directory structure from an :py:class:`Architype`.

Instances of this class are immutable.
"""
