"""
architype_parameters
~~~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`ArchitypeParameters` along with
supporting classes, functions, and attributes.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

from collections import namedtuple


class ArchitypeParameters(
    namedtuple(
        'ArchitypeParametersBase',
        ('package_name', 'author', 'author_email', 'date')
    )
):
    """
    A container class that responsible for grouping the parameters used to
    create a project directory structure from an :py:class:`Architype`.

    Instances of this class are immutable.
    """

    def as_dict(self) -> dict:
        """
        Returns a dictionary representation of this instance, wherein each
        named attribute is a key in the dictionary returned.
        :return: the dictionary representing this instance
        """
        return self._asdict()
