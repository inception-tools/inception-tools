"""
standard_archetype
~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`StandardArchetype` along with supporting
classes, functions, and attributes.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os
from abc import ABCMeta
from enum import Enum, EnumMeta
from typing import Iterable, Tuple

from inception_tools.archetype import Archetype
from inception_tools.archetype_parameters import ArchetypeParameters
from inception_tools.template_archetype import TemplateArchetype

ARCHETYPE_DIR = os.path.abspath(os.path.join(__file__, os.pardir, "data", "archetypes"))


class _ABCEnumMeta(ABCMeta, EnumMeta):
    # Enables Enums to inherit from abstract base classes
    pass


class StandardArchetype(Archetype, Enum, metaclass=_ABCEnumMeta):
    """
    Enumerates the standard :py:class:`Archetype` instances available across the
    system.
    """

    CLI = ("inception-tools-archetype-cli-1.0",)
    """
    The :py:meth:`build` method of this :py:class:`Archetype` will create a
    directory/file tree with the following structure:

    ::

        root_dir/
            my_package/
                __init__.py
                cli.py
            tests/
                __init__.py
                end-to-end/
                    __init__.py
                integration/
                    __init__.py
                unit/
                    __init__.py
            LICENSE
            Makefile
            Pipfile
            README.rst
            setup.cfg
            setup.py

    where 'root_dir' is the `root_dir argument and 'my_package' is the `package_name`
    attribute of the params argument.
    """

    LIB = ("inception-tools-archetype-lib-1.0",)
    """
    The :py:meth:`build` method of this :py:class:`Archetype` will create a
    directory/file tree with the following structure:

    ::

        root_dir/
            my_package/
                __init__.py
                my_package.py
            tests/
                __init__.py
                end-to-end/
                    __init__.py
                integration/
                    __init__.py
                unit/
                    __init__.py
            LICENSE
            Makefile
            Pipfile
            README.rst
            setup.cfg
            setup.py

    where 'root_dir' is the `root_dir argument and 'my_package' is the `package_name`
    attribute of the params argument.
    """

    SIMPLE = ("inception-tools-archetype-simple-1.0",)
    """
    The :py:meth:`build` method of this :py:class:`Archetype` will create a
    directory/file tree with the following structure:

    ::

        root_dir/
            my_package.py
            tests/
                __init__.py
            LICENSE
            Makefile
            Pipfile
            README.rst
            setup.cfg
            setup.py

    where 'root_dir' is the `root_dir argument and 'my_package' is the `package_name`
    attribute of the params argument.
    """

    def __init__(self, archetype_resource_id) -> None:
        dir_path = os.path.join(ARCHETYPE_DIR, archetype_resource_id)
        self._archetype_resource_id = archetype_resource_id
        self._delegate = TemplateArchetype(dir_path)

    @property
    def archetype_resource_id(self) -> str:
        return self._archetype_resource_id

    @property
    def canonical_name(self) -> str:
        return self.name.lower()

    def file_paths(self, root_path: str, params: ArchetypeParameters) -> Iterable[str]:
        return self._delegate.file_paths(root_path, params)

    def dir_paths(self, root_path: str, params: ArchetypeParameters) -> Iterable[str]:
        return self._delegate.dir_paths(root_path, params)

    def build(self, root_dir: str, params: ArchetypeParameters) -> None:
        return self._delegate.build(root_dir, params)

    @classmethod
    def from_string(cls, s: str):
        return {sa.canonical_name: sa for sa in StandardArchetype}[s.lower()]

    @classmethod
    def canonical_names(cls) -> Tuple[str]:
        return tuple(sa.canonical_name for sa in StandardArchetype)
