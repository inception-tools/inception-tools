"""
directory_builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`DirectoryBuilder` along with supporting classes,
functions, and attributes. """

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import errno
import os
from abc import ABC, abstractmethod

from inception_tools.archetype_parameters import ArchetypeParameters
from inception_tools.archetype_resource_builder import ArchetypeResourceBuilder
from inception_tools.constants import UNIMPLEMENTED_ABSTRACT_METHOD_ERROR


class DirectoryBuilder(ArchetypeResourceBuilder, ABC):
    """
    An :py:class:`inception_tools.ArchetypeResourceBuilder` implementation which
    builds an empty directory at it's :py:meth:`path`.  This class provides a
    'template-method' implementation of :py:meth:`path` and :py:meth`build`,
    which delegate responsibility for determining the subpath under ``root_dir`` to a
    method called :py:class:`subpath`.
    """

    def _path(self, root_dir: str, params: ArchetypeParameters) -> str:
        return os.path.join(root_dir, self.subpath(params))

    def path(self, root_dir: str, params: ArchetypeParameters) -> str:
        """
        Returns the path to the directory that will be created by
        :py:meth:`build`.
        """
        return self._path(root_dir, params)

    def build(self, root_dir: str, params: ArchetypeParameters) -> None:
        """
        Creates a directory under ``root_dir`` determined by the _result of
        :py:meth:`subpath`.
        :param root_dir: the root directory to which :py:meth:`subpath`
        should be appended
        :param params: the parameters used to determine the subpath
        :return: :py:const:`None`
        ..:note: this method has dependencies on the implementations of
        :py:meth:`subpath`
        """
        p = self._path(root_dir, params)
        try:
            os.makedirs(p)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    @abstractmethod
    def subpath(self, params: ArchetypeParameters) -> str:
        """
        Subclasses are required to implement this method.  Implementations of this
        method should return the subpath, under the root directory, of the directory
        to be created by :py:meth:`build`.
        :param params: the :py:class `ArchetypeParameters` to use as context
        when creating the subpath, e.g., when creating directories whose
        sub-path might be determined by the package name.
        :return: the path
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR
