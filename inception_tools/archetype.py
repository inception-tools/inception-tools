"""
archetype
~~~~~~~~~

Houses the declaration of :py:class:`archetype` along with supporting classes,
functions, and attributes. """

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from abc import ABC, abstractmethod
from typing import Iterable

from inception_tools.archetype_parameters import ArchetypeParameters
from inception_tools.constants import UNIMPLEMENTED_ABSTRACT_METHOD_ERROR


class Archetype(ABC):
    """
    Instances of this class provide a canonical template project structure and are
    capable of building particular project structures under a specified root
    directory using a set of parameters to determine the specifics of directory
    structure and file paths and content.
    """

    @abstractmethod
    def file_paths(self, root_path: str, params: ArchetypeParameters) -> Iterable[str]:
        """
        The paths of every file that will be created by :py:meth:`Archetype.build`.

        :param root_path: the root directory of the project structure to be
        created
        :param params: the :py:class:`ArchetypeParameters` to use as context
        for the project to be built
        :return: :py:const:`None`
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR

    @abstractmethod
    def dir_paths(self, root_path: str, params: ArchetypeParameters) -> Iterable[str]:
        """
        The paths of every directory that will be explicitly created by
        :py:meth:`Archetype.build`.

        :param root_path: the root directory of the project structure to be
        created
        :param params: the :py:class:`ArchetypeParameters` to use as context
        for the project to be built
        :return: :py:const:`None`
        .. note::
           Intermediary directories in the paths listed by
           :py:meth:`file_paths` may also be create even though they are not
           listed under this method.
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR

    @abstractmethod
    def build(self, root_dir: str, params: ArchetypeParameters) -> None:
        """
        Builds the project structure for this instance.  See the class-level
        documentation of :py:class:`Archetype` for more information.

        :param root_dir: the root directory of the project structure to be
        created
        :param params: the :py:class:`ArchetypeParameters` to use as context
        for the project to be built
        :return: :py:const:`None`
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR
