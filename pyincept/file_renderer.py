"""
file_renderer
~~~~~~~~~~~~~

Houses the declaration of :py:class:`FileRenderer` along with supporting
classes, functions, and attributes.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

from abc import ABC, abstractmethod

from pyincept.archetype_parameters import ArchetypeParameters
from pyincept.archetype_resource_builder import ArchetypeResourceBuilder
from pyincept.constants import UNIMPLEMENTED_ABSTRACT_METHOD_ERROR


class FileRenderer(ArchetypeResourceBuilder, ABC):
    """
    This abstract base class determines the interfaces by which files built
    by this project should be rendered and saved.
    """

    @abstractmethod
    def subpath(self, params: ArchetypeParameters) -> str:
        """
        Returns the subpath, under the root directory, of the file to be
        saved by :py:meth:`build`.
        :param params: the :py:class:`ArchetypeParameters` to use as context
        when creating the subpath, e.g., when storing files whose sub-path
        might be determined by the package name.
        :return: the path
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR

    @abstractmethod
    def render(self, params: ArchetypeParameters) -> str:
        """
        Returns the content of the file to be saved by
        :py:meth:`build`.
        :param params: the :py:class:`ArchetypeParameters` to use as context
        when building the content
        :return: the content of the file to be saved by
        :py:meth:`build`
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR
