"""
    architype
    ~~~~~~~~~~~~~~~~~~~~~~~
    Houses the declaration of :py:class:`architype` along with
    supporting classes, functions, and attributes.
    ~~~~~~~~~~~~~~~~~~~~~~~
    Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

from abc import ABC, abstractmethod
from typing import Iterable

from pyincept.architype_parameters import ArchitypeParameters
from pyincept.file_renderer import FileRenderer


class Architype(ABC):
    """
    Instances of this class provide a canonical template project structure
    and are capable of building particular project structures under a
    specified root directory using a set of parameters to determine the
    specifics of directory structure and file paths and content.
    """

    @abstractmethod
    def output_files(
            self,
            root_path: str,
            params: ArchitypeParameters
    ) -> Iterable[str]:
        """
        The paths of every file that will be created by :py:class:`build`.

        :param root_path: the root directory of the project structure to be
        created

        :param params: the :py:class:`ArchitypeParameters` to use as context
        for the project to be built

        :return: :py:const:`None`
        """
        raise NotImplementedError()

    @abstractmethod
    def build(self, root_path: str, params: ArchitypeParameters) -> None:
        """
        Builds the project structure for this instance.  See the class-level
        documentation of :py:class:`Architype` for more information.

        :param root_path: the root directory of the project structure to be
        created

        :param params: the :py:class:`ArchitypeParameters` to use as context
        for the project to be built

        :return: :py:const:`None`
        """
        raise NotImplementedError()


class BaseArchitype(Architype):
    """
    A base implementation of :py:class:`Architype` that provides basic
    implementations of :py:meth:`Architype.build` and
    :py:meth:`Architype.output_files`.
    """

    def __init__(self, file_renderers: Iterable[FileRenderer]) -> None:
        """
        Class initializer.

        :param file_renderers: a set of :py:class:`FileRenderer` instances
        used by :py:class:`build` to create project structure.
        """
        super().__init__()
        self._file_renderers = file_renderers

    def output_files(
            self,
            root_path: str,
            params: ArchitypeParameters
    ) -> Iterable[str]:
        return tuple(r.path(root_path, params) for r in self._file_renderers)

    def build(self, root_path: str, params: ArchitypeParameters) -> None:
        """
        Builds the project structure using the :py:class:`FileRenderer`
        instances held by this instance.

        :param root_path: the root directory of the project structure to be
        created

        :param params: the :py:class:`ArchitypeParameters` to use as context
        for the project to be built

        :return: :py:const:`None`
        """
        for r in self._file_renderers:
            r.render_and_save(root_path, params)
