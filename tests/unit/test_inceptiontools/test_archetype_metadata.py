"""
test_archetype_metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`archetype_metadata` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from hamcrest import assert_that, is_
from pytest import raises

from inceptiontools.archetype_metadata import ArchetypeMetadata
from inceptiontools.json_serializable import JsonSerializationError


class TestArchetypeMetadata(object):
    """
    Unit test cases for :py:class:`ArchetypeMetadata`.
    """

    ##############################
    # Class attributes

    _JSON_OBJ = {
        "group_id": "some_group_id",
        "archetype_id": "some_archetype_id",
        "version_id": "some_version_id",
    }

    _ARCHETYPE_METADATA = ArchetypeMetadata(
        "some_group_id", "some_archetype_id", "some_version_id"
    )

    ##############################
    # Instance methods

    # Test cases

    def test_from_json_raises_for_json_type(self):
        """
        Unit test case for :py:method:`ArchetypeMetadata.from_json`.
        """
        json_obj = dict(self._JSON_OBJ)
        json_obj["archetype_id"] = 5
        with raises(JsonSerializationError):
            ArchetypeMetadata.from_json(json_obj)

    def test_from_json_allows_additional_keys(self):
        """
        Unit test case for :py:method:`ArchetypeMetadata.from_json`.
        """
        json_obj = dict(self._JSON_OBJ)
        json_obj["foo"] = "bar"
        actual = ArchetypeMetadata.from_json(json_obj)
        expected = self._ARCHETYPE_METADATA
        assert_that(actual, is_(expected))

    def test_from_json_creates_correct_object(self):
        """
        Unit test case for :py:method:`ArchetypeMetadata.from_json`.
        """
        actual = ArchetypeMetadata.from_json(self._JSON_OBJ)
        expected = self._ARCHETYPE_METADATA
        assert_that(actual, is_(expected))

    def test_to_json(self):
        """
        Unit test case for :py:method:`ArchetypeMetadata.to_json`.
        """
        actual = self._ARCHETYPE_METADATA.to_json()
        expected = self._JSON_OBJ
        assert_that(actual, is_(expected))
