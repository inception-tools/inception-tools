"""
template_archetype
~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`TemplateArchetype` along with
supporting classes, functions, and attributes.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os

from inception_tools.archetype_base import ArchetypeBase
from inception_tools.archetype_descriptor import ArchetypeDescriptor
from inception_tools.archetype_metadata import ArchetypeMetadata
from inception_tools.template_directory_builder import TemplateDirectoryBuilder
from inception_tools.template_file_builder import TemplateFileBuilder


class TemplateArchetype(ArchetypeBase):
    """
    An :py:class:`Archetype` subclass that uses a set of :py:class:`jinja2` template
    files and descriptor files, all contained within a single directory, to create
    and initial project structure.  At a minimum the directory must contain two JSON
    files

    - :py:attr:`METADATA_FILE_NAME` and
    _ :py:attr:`DESCRIPTOR_FILE_NAME`

    any 'prototype' template files referenced by the descriptor JSON must also be
    present in the directory, at the subpath specified by the descriptor.

    Variables available to the template are the fields of
    :py:class:`ArchetypeParameters`.  Each field of :py:class:`Archetype` parameters
    is available as an unscoped variable.  For example, to reference the fields
    :py:attr:`ArchetypeParameters.author`, you would simply use the variable name
    'author' directly using double curly braces like so: ``{{author}}``.
    """

    METADATA_FILE_NAME = "archetype-metadata.json"
    """
    The name of the JSON file containing :py:class:`ArchetypeMetadata`. This file is
    used to determine what the canonical name of the archetype.
    """

    DESCRIPTOR_FILE_NAME = "archetype-descriptor.json"
    """
    The name of the JSON file containing :py:class:`ArchetypeDescriptor` data. This
    file contains all of the information for mapping template files to sub-paths
    within the projects created by ``inception_tools``.
    """

    def __init__(self, dir_path: str) -> None:
        """
        Initializes a new :py:class:`Archetype` instance from an directory assumed to
        contain an :py:class:`ArchetypeMetadata` JSON file,
        a :py:class:`ArchetypeDescriptor` file, and any prototypes referenced through
        the descriptor.

        :param dir_path: the path to the directory containing the :py:class:`Archetype`
        files
        """
        self._dir_path = dir_path

        with open(self._metadata_path(dir_path)) as metadata_f:
            metadata = ArchetypeMetadata.from_text_io(metadata_f)
        self._metadata = metadata

        with open(self._descriptor_path(dir_path)) as descriptor_f:
            descriptor = ArchetypeDescriptor.from_text_io(descriptor_f)
        self._descriptor = descriptor

        file_builders = self._get_file_builders(dir_path, descriptor)
        dir_builders = self._get_directory_builders(dir_path, descriptor)

        super().__init__(file_builders, dir_builders)

    @classmethod
    def _get_file_builders(cls, dir_path, descriptor):

        file_builders = []
        for f in descriptor.files:
            f_path = os.path.join(dir_path, f.prototype)
            with open(f_path) as fin:
                prototype_content = fin.read()
            fb = TemplateFileBuilder.from_strings(f.subpath, prototype_content)
            file_builders.append(fb)

        return tuple(file_builders)

    @classmethod
    def _get_directory_builders(cls, dir_path, descriptor):
        result = []
        for d in descriptor.directories:
            dd = TemplateDirectoryBuilder.from_string(d.subpath)
            result.append(dd)

        return tuple(result)

    @classmethod
    def _metadata_path(cls, dir_path):
        return os.path.join(dir_path, cls.METADATA_FILE_NAME)

    @classmethod
    def _descriptor_path(cls, dir_path):
        return os.path.join(dir_path, cls.DESCRIPTOR_FILE_NAME)
