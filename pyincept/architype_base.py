"""
    architype_base
    ~~~~~~~~~~~~~~~~~~~~~~~

    Houses the declaration of :py:class:`ArchitypeBase` along with
    supporting classes, functions, and attributes.

    Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

from typing import Iterable

from pyincept.architype import Architype
from pyincept.architype_parameters import ArchitypeParameters
from pyincept.file_renderer import FileRenderer


class ArchitypeBase(Architype):
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

    def build(self, root_dir: str, params: ArchitypeParameters) -> None:
        """
        Builds the project structure using the :py:class:`FileRenderer`
        instances held by this instance.

        :param root_dir: the root directory of the project structure to be
        created

        :param params: the :py:class:`ArchitypeParameters` to use as context
        for the project to be built

        :return: :py:const:`None`
        """
        for r in self._file_renderers:
            r.render_and_save(root_dir, params)
