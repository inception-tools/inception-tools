"""
resource_builder
~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`ArchetypeResourceBuilder` along with
supporting classes, functions, and attributes.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from abc import ABC

from inception_tools.archetype_parameters import ArchetypeParameters
from inception_tools.constants import UNIMPLEMENTED_ABSTRACT_METHOD_ERROR


class ArchetypeResourceBuilder(ABC):
    """
    Provides the common interface by which all
    :py:class:`inception_tools.Archetype` resources are created.
    """

    def path(self, root_dir: str, params: ArchetypeParameters) -> str:
        """
        Returns the full path (possibly non-absolute) to the resource that will be
        created by :py:meth:`build`.
        :param root_dir: the root directory argument for :py:meth:`build`
        :param params: the parameters argument for :py:meth:`build`
        :return: the path
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR

    def build(self, root_dir: str, params: ArchetypeParameters) -> None:
        """
        Builds the resource and stores it under the root directory.  The content of
        the resource as well as the subpath under the root directory may be,
        but need-not be, determined by the parameters argument.
        :param root_dir: the root directory under which the resource
        should be stored
        :param params: the parameters used to determine the resource's
        content and possibly the subpath under the root directory
        :return: :py:const:`None`
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR
