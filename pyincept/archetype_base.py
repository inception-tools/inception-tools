"""
archetype_base
~~~~~~~~~~~~~~

Houses the declaration of :py:class:`ArchetypeBase` along with supporting
classes, functions, and attributes.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

from typing import Iterable

from pyincept.archetype import Archetype
from pyincept.archetype_parameters import ArchetypeParameters
from pyincept.file_builder import FileBuilder


class ArchetypeBase(Archetype):
    """
    A base implementation of :py:class:`Archetype` that provides basic
    implementations of :py:meth:`Archetype.build` and
    :py:meth:`Archetype.file_paths`.
    """

    def __init__(self, resource_builders: Iterable[FileBuilder]) -> None:
        """
        Class initializer.
        :param resource_builders: a set of
        :py:class:`pyincept.ArchetypeResourceBuilder` instances used by
        :py:class:`build` to create the project structure.
        """
        super().__init__()
        self._file_builders = resource_builders

    def file_paths(
            self,
            root_path: str,
            params: ArchetypeParameters
    ) -> Iterable[str]:
        return tuple(r.path(root_path, params) for r in self._file_builders)

    def build(self, root_dir: str, params: ArchetypeParameters) -> None:
        """
        Builds the project structure using the :py:class:`FileBuilder`
        instances held by this instance.
        :param root_dir: the root directory of the project structure to be
        created
        :param params: the :py:class:`ArchetypeParameters` to use as context
        for the project to be built
        :return: :py:const:`None`
        """
        for r in self._file_builders:
            r.build(root_dir, params)
