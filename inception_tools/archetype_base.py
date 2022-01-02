"""
archetype_base
~~~~~~~~~~~~~~

Houses the declaration of :py:class:`ArchetypeBase` along with supporting classes,
functions, and attributes. """

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from typing import Iterable

from inception_tools.archetype import Archetype
from inception_tools.archetype_parameters import ArchetypeParameters
from inception_tools.directory_builder import DirectoryBuilder
from inception_tools.file_builder import FileBuilder


class ArchetypeBase(Archetype):
    """
    A base implementation of :py:class:`Archetype` that provides basic
    implementations of :py:meth:`Archetype.build` and :py:meth:`Archetype.file_paths`.
    """

    def __init__(
        self,
        file_builders: Iterable[FileBuilder],
        dir_builders: Iterable[DirectoryBuilder],
    ) -> None:
        """
        Class initializer.
        :param file_builders: a set of
        :py:class:`inception_tools.ArchetypeResourceBuilder` instances used by
        :py:meth:`build` to create the project structure.
        """
        super().__init__()
        self._file_builders = file_builders
        self._dir_builders = dir_builders

    def file_paths(self, root_path: str, params: ArchetypeParameters) -> Iterable[str]:
        return tuple(r.path(root_path, params) for r in self._file_builders)

    def dir_paths(self, root_path: str, params: ArchetypeParameters) -> Iterable[str]:
        return tuple(r.path(root_path, params) for r in self._dir_builders)

    def build(self, root_dir: str, params: ArchetypeParameters) -> None:
        """
        Builds the project structure using the :py:class:`FileBuilder` instances held
        by this instance.
        :param root_dir: the root directory of the project structure to be
        created
        :param params: the :py:class:`ArchetypeParameters` to use as context
        for the project to be built
        :return: :py:const:`None`
        """
        for r in self._file_builders:
            r.build(root_dir, params)
        for r in self._dir_builders:
            r.build(root_dir, params)
