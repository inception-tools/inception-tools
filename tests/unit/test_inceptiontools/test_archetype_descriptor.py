"""
test_archetype_descriptor
~~~~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`archetype_descriptor` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from hamcrest import assert_that, is_

from inceptiontools.archetype_descriptor import (
    ArchetypeDescriptor,
    DirectoryDescriptor,
    FileDescriptor,
)


class TestArchetypeDescriptor(object):
    """
    Unit test cases for :py:class:`ArchetypeDescriptor`.
    """

    ##############################
    # Class attributes

    _JSON_OBJ = {
        "files": [
            {
                "subpath": "some_file_subpath_1",
                "prototype": "some_prototype_1",
            },
            {
                "subpath": "some_file_subpath_2",
                "prototype": "some_prototype_2",
            },
        ],
        "directories": [
            {"subpath": "some_directory_subpath_1"},
            {"subpath": "some_directory_subpath_2"},
        ],
    }

    _ARCHETYPE_DESCRIPTOR = ArchetypeDescriptor(
        (
            FileDescriptor("some_file_subpath_1", "some_prototype_1"),
            FileDescriptor("some_file_subpath_2", "some_prototype_2"),
        ),
        (
            DirectoryDescriptor("some_directory_subpath_1"),
            DirectoryDescriptor("some_directory_subpath_2"),
        ),
    )

    ##############################
    # Instance methods

    # Test cases

    def test_from_json(self):
        """
        Unit test case for :py:method:`ArchetypeDescriptor.from_json`.
        """
        actual = ArchetypeDescriptor.from_json(self._JSON_OBJ)
        expected = self._ARCHETYPE_DESCRIPTOR
        assert_that(actual, is_(expected))

    def test_to_json(self):
        """
        Unit test case for :py:method:`ArchetypeDescriptor.to_json`.
        """
        actual = self._ARCHETYPE_DESCRIPTOR.to_json()
        expected = self._JSON_OBJ
        assert_that(actual, is_(expected))
