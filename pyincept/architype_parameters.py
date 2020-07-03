"""
    architype_parameters
    ~~~~~~~~~~~~~~~~~~~~~~~
    Houses the declaration of :py:class:`ArchitypeParameters` along with
    supporting classes, functions, and attributes.
    ~~~~~~~~~~~~~~~~~~~~~~~
    Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

from datetime import datetime
from typing import NamedTuple


# Python >= 3.6
class ArchitypeParameters(NamedTuple):
    """
    The 'container class' defines and encapsulates the set of parameters which
    can be used to render and save an :py:class:`Architype`.  Instances of this
    class are intended to be immutable.
    """
    package_name: str
    author: str
    author_email: str
    date: datetime.date
