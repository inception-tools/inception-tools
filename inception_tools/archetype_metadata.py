"""
archetype_metadata
~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`ArchetypeMetadata` along with supporting
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


class ArchetypeMetadata(
    namedtuple(
        "ArchetypeMetadataBase",
        (
            "group_id",
            "archetype_id",
            "version_id",
        ),
    ),
    JsonSerializable,
):
    """
    Instances of this class encapsulate and group metadata that pertains to an
    :py:class:`archetype.Archetype`.  :py:class:`Archetype` instances are uniquely
    identified by the combination of a group identifier (e.g., 'inception_tools'),
    which determines a name space, an architype identifier ( e.g., standard),
    and a version identifier ( e.g., '1.2.3').  The combination of architype and
    version identifier is assumed to be unique within the name space of the group
    identifier. :ivar str group_id: the group identifier :ivar str archetype_id: the
    architype identifier :ivar str version_id: the architype version identifier
    """

    # Make instances of this class immutable
    __slots__ = ()

    JSON_SCHEMA = {
        "type": "object",
        "properties": {
            "group_id": {"type": "string"},
            "archetype_id": {"type": "string"},
            "version_id": {"type": "string"},
        },
    }
    """
    The Python `JSON schema`_ that :py:meth:`serialize_json` and
    :py:meth:`deserialize_json` must adhere to.

    .. _`JSON schema`: https://json-schema.org/
    """

    @classmethod
    def _validate_json(cls, json_obj: JSON_OBJ_TYPE) -> None:
        try:
            validate(json_obj, cls.JSON_SCHEMA)
        except ValidationError as e:
            to_raise = JsonSerializationError(f"Invalid JSON format: {json_obj}")
            raise to_raise from e

    @classmethod
    def from_json(cls, json_obj: JSON_OBJ_TYPE):
        """
        Creates a new :py:class:`ArchetypeMetadata` from a JSON-like Python object of
        the form:

        .. code-block::

            {
                'group_id': <group-id-string>,
                'archetype_id': <archetype-id-string>,
                'version_id': <version-id-string>,
            }
        """
        cls._validate_json(json_obj)

        if isinstance(json_obj, dict):
            return ArchetypeMetadata(
                group_id=json_obj["group_id"],
                archetype_id=json_obj["archetype_id"],
                version_id=json_obj["version_id"],
            )

        raise RuntimeError(
            f"Expected an object of type 'dict' but received: {json_obj!r}"
        )

    def to_json(self) -> dict:
        """
        Returns a JSON-like Python object of the form:

        .. code-block::

            {
                'group_id': <group-id-string>,
                'archetype_id': <archetype-id-string>,
                'version_id': <version-id-string>,
            }
        """
        json_obj = self._asdict()
        self._validate_json(json_obj)
        return json_obj
