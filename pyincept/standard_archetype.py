"""
standard_archetype
~~~~~~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`StandardArchetype` along with
supporting classes, functions, and attributes.
"""

__author__ = 'Andrew van Herick'

import os
from abc import ABCMeta
from enum import Enum, EnumMeta
from typing import Iterable

from pyincept.archetype import Archetype
from pyincept.archetype_base import ArchetypeBase
from pyincept.archetype_descriptor import ArchetypeDescriptor
from pyincept.archetype_metadata import ArchetypeMetadata
from pyincept.archetype_parameters import ArchetypeParameters
from pyincept.template_directory_builder import TemplateDirectoryBuilder
from pyincept.template_file_builder import TemplateFileBuilder

ARCHITYPE_DIR = os.path.abspath(
    os.path.join(
        __file__,
        os.pardir,
        'data',
        'archetypes'
    )
)


class StandardArchetype(ArchetypeBase):
    """
    Enumerates the standard :py:class:`Archetype` instances available
    across the system.
    """

    _METADATA_FILE_NAME = 'archetype-metadata.json'
    _DESCRIPTOR_FILE_NAME = 'archetype-descriptor.json'

    def __init__(self, metadata, resource_builders) -> None:
        super().__init__(resource_builders)
        self._metadata = metadata

    @classmethod
    def _get_resource_builders(cls, dir_path, descriptor):
        result = []
        for f in descriptor.files:
            f_path = os.path.join(dir_path, f.prototype)
            with open(f_path) as fin:
                prototype_content = fin.read()
            fb = TemplateFileBuilder.from_strings(f.subpath, prototype_content)
            result.append(fb)
        for d in descriptor.directories:
            dd = TemplateDirectoryBuilder.from_string(d.subpath)
            result.append(dd)
        return tuple(result)

    @classmethod
    def from_directory(cls, dir_path: str) -> Archetype:
        """
        Factory method for creating a new :py:class:`Archetype` instance
        from an directory assumed to contain an
        :py:class:`ArchetypeMetadata` JSON file,
        a :py:class:`ArchetypeDescriptor` file, and any prototypes
        referenced through the descriptor.

        :param dir_path: the path to the directory containing the
        :py:class:`Archetype` files
        :return: the :py:class:`Archetype` instance
        """
        with open(cls._metadata_path(dir_path)) as metadata_f:
            metadata = ArchetypeMetadata.from_text_io(metadata_f)

        with open(cls._descriptor_path(dir_path)) as descriptor_f:
            descriptor = ArchetypeDescriptor.from_text_io(descriptor_f)

        resource_builders = cls._get_resource_builders(dir_path, descriptor)
        return cls(metadata, resource_builders)

    @classmethod
    def _metadata_path(cls, dir_path):
        return os.path.join(dir_path, cls._METADATA_FILE_NAME)

    @classmethod
    def _descriptor_path(cls, dir_path):
        return os.path.join(dir_path, cls._DESCRIPTOR_FILE_NAME)


class _ABCEnumMeta(ABCMeta, EnumMeta):
    # Enables Enums to inherit from abstract base classes
    pass


class DefaultArchetype(Archetype, Enum, metaclass=_ABCEnumMeta):
    """
    Enumerates the standard :py:class:`Archetype` instances available
    across the system.
    """

    #: The :py:meth:`build` method of this :py:class:`Archetype` will create a
    # directory/file tree with the following structure:
    #:
    #: ::
    #:
    #:     root_dir/
    #:         my_package/
    #:             __init__.py
    #:             my_package.py
    #:         tests/
    #:             __init__.py
    #:             end-to-end/
    #:                 __init__.py
    #:                 test_my_package/
    #:                     __init__.py
    #:             integration/
    #:                 __init__.py
    #:                 test_my_package/
    #:                     __init__.py
    #:             unit/
    #:                 __init__.py
    #:                 test_my_package/
    #:                     __init__.py
    #:         LICENSE
    #:         Makefile
    #:         Pipfile
    #:         README.rst
    #:         setup.cfg
    #:         setup.py
    #:
    #: where 'root_dir' is the `root_dir argument and 'my_package' is the
    # `package_name` attribute of the params argument.
    PROJECT_ROOT = ('pyincept-archetype-standard',)

    def __init__(self, architype_resource_id) -> None:
        # Referencing ArchetypeBase directly for the sake of supporting Python
        # 3.5, which does not seem to handle call to super() in the context of
        # multiple inheritance as gracefully as the later versions do.
        dir_path = os.path.join(ARCHITYPE_DIR, architype_resource_id)
        self._delegate = StandardArchetype.from_directory(dir_path)

    def output_files(
            self,
            root_path: str,
            params: ArchetypeParameters
    ) -> Iterable[str]:
        return self._delegate.output_files(root_path, params)

    def build(self, root_dir: str, params: ArchetypeParameters) -> None:
        return self._delegate.build(root_dir, params)
