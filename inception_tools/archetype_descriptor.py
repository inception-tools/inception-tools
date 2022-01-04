"""
archetype_descriptor
~~~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`ArchetypeDescriptor` along with supporting
classes, functions, and attributes. """

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from collections import namedtuple

from jsonschema import validate, ValidationError

from inception_tools.json_serializable import (
    JSON_OBJ_TYPE,
    JsonSerializable,
    JsonSerializationError,
)


class _JsonKey(object):
    DIRECTORIES = "directories"
    FILES = "files"
    PROTOTYPE = "prototype"
    SUBPATH = "subpath"


DirectoryDescriptor = namedtuple("DirectoryDescriptor", ("subpath",))
FileDescriptor = namedtuple("FileDescriptor", ("subpath", "prototype"))


class ArchetypeDescriptor(
    namedtuple("_ArchetypeDescriptorBase", ("files", "directories")), JsonSerializable
):
    """
    Describes the files and directories which should be created by an
    :py:class:`Architype`.
    """

    # Make instances of this class immutable
    __slots__ = ()

    JSON_SCHEMA = {
        "type": "object",
        "properties": {
            "directories": {
                "type": "array",
                "items": {"$ref": "#/definitions/directory"},
            },
            "files": {"type": "array", "items": {"$ref": "#/definitions/file"}},
        },
        "definitions": {
            "directory": {
                "type": "object",
                "properties": {
                    "subpath": {"type": "string"},
                },
            },
            "file": {
                "type": "object",
                "properties": {
                    "subpath": {"type": "string"},
                    "prototype": {"type": "string"},
                },
            },
        },
    }
    """
    The Python `JSON schema`_ that :py:meth:`serialize_json` and
    :py:meth:`deserialize_json` must adhere to.

    .. _`JSON schema`: https://json-schema.org/
    """

    @classmethod
    def from_json(cls, json_obj: JSON_OBJ_TYPE):
        """
        Creates a new :py:class:`ArchetypeDescriptor` from a JSON-like Python object
        of the form:

        .. code-block::

            {
                'directories': [
                    {
                        'subpath': <subpath-jinja2-template-string>
                    },
                    ...
                    {
                        'subpath': <subpath-jinja2-template-string>
                    }
                ],
                'files': [
                    {
                        'subpath': <subpath-jinja2-template-string>,
                        'prototype': <subpath-jinja2-template-string>
                    },
                    ...
                    {
                        'subpath': <subpath-jinja2-template-string>,
                        'prototype': <subpath-jinja2-template-string>
                    }
                ]
            }
        """
        cls._validate_json(json_obj)

        if isinstance(json_obj, dict):

            d_json = json_obj[_JsonKey.DIRECTORIES]
            dir_descriptors = tuple(
                DirectoryDescriptor(j[_JsonKey.SUBPATH]) for j in d_json
            )

            f_json = json_obj[_JsonKey.FILES]
            file_descriptors = tuple(
                FileDescriptor(j[_JsonKey.SUBPATH], j[_JsonKey.PROTOTYPE])
                for j in f_json
            )

            return cls(file_descriptors, dir_descriptors)

        raise RuntimeError(
            f"Expected an object of type 'dict' but received: {json_obj!r}"
        )

    @classmethod
    def _validate_json(cls, json_obj: JSON_OBJ_TYPE):
        try:
            validate(json_obj, cls.JSON_SCHEMA)
        except ValidationError as e:
            to_raise = JsonSerializationError(f"Invalid JSON format: {json_obj}")
            raise to_raise from e

    def to_json(self) -> JSON_OBJ_TYPE:
        """
        Returns a JSON-like Python object of the form:

        .. code-block::

            {
                'directories': [
                    {
                        'subpath': <subpath-jinja2-template-string>
                    },
                    ...
                    {
                        'subpath': <subpath-jinja2-template-string>
                    }
                ],
                'files': [
                    {
                        'subpath': <subpath-jinja2-template-string>,
                        'prototype': <subpath-jinja2-template-string>
                    },
                    ...
                    {
                        'subpath': <subpath-jinja2-template-string>,
                        'prototype': <subpath-jinja2-template-string>
                    }
                ]
            }
        """
        # Suppressing protected member inspection because NamedTuple
        # documentation has _asdict as part of its API
        # noinspection PyProtectedMember
        return {
            _JsonKey.DIRECTORIES: [d._asdict() for d in self.directories],
            _JsonKey.FILES: [d._asdict() for d in self.files],
        }
