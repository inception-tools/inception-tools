"""
architype
~~~~~~~~~

Houses the declaration of :py:class:`architype` along with supporting
classes, functions, and attributes.

Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

from abc import ABC, abstractmethod
from typing import Iterable

from pyincept.architype_parameters import ArchitypeParameters


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
