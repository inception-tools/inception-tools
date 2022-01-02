"""
archetype_parameters
~~~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`ArchetypeParameters` along with supporting
classes, functions, and attributes. """

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from collections import namedtuple


class ArchetypeParameters(
    namedtuple(
        "ArchetypeParametersBase", ("package_name", "author", "author_email", "date")
    )
):
    """
    A container class that responsible for grouping the parameters used to create a
    project directory structure from an :py:class:`archetype.Archetype`.

    Instances of this class are immutable.

    :ivar str package_name: the name of the package to be created
    :ivar str author: the package author name
    :ivar str author_email: the author's email address
    :ivar str date: the inception date of the project
    """

    def as_dict(self) -> dict:
        """
        Returns a dictionary representation of this instance, wherein each named
        attribute is a key in the dictionary returned.
        :return: the dictionary representing this instance
        """
        return self._asdict()
