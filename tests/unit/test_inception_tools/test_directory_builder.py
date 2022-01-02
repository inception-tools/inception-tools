"""
test_directory_builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`directory_builder` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os
import shutil

from hamcrest import assert_that, is_

from inception_tools.archetype_parameters import ArchetypeParameters
from inception_tools.directory_builder import DirectoryBuilder
from tests.archetype_output_test_base import ArchetypeOutputTestBase


class _MockDirectoryBuilder(DirectoryBuilder):
    def __init__(self, s: str) -> None:
        self.s = s

    def subpath(self, params: ArchetypeParameters) -> str:
        return self.s


class TestDirectoryBuilder(object):
    """
    Unit test cases for :py:class:`DirectoryBuilder`.
    """

    ##############################
    # Class attributes

    _ROOT_DIR = ArchetypeOutputTestBase._ROOT_DIR
    _PARAMS = ArchetypeOutputTestBase._PARAMS

    ##############################
    # Instance methods

    # Instance set up / tear down

    def setup(self):
        """
        Called before each method in this class with a name of the form
        test_*().
        """
        ArchetypeOutputTestBase._validate_path_doesnt_exist(self._ROOT_DIR)

        self._builder = _MockDirectoryBuilder("some_subpath")

    def teardown(self):
        """
        Called after each method in this class with a name of the form
        test_*().
        """
        if os.path.exists(self._ROOT_DIR):
            shutil.rmtree(self._ROOT_DIR)

        ArchetypeOutputTestBase._validate_path_doesnt_exist(self._ROOT_DIR)

    # Test cases

    def test_path(self):
        """
        Unit test case for :py:method:`DirectoryBuilder.path`.
        """
        actual = self._builder.path(self._ROOT_DIR, self._PARAMS)
        expected = os.path.join("some_root_dir", "some_subpath")
        assert_that(actual, is_(expected))

    def test_build(self):
        """
        Unit test case for :py:method:`DirectoryBuilder.build`.
        """
        expected = os.path.join("some_root_dir", "some_subpath")

        assert_that(not os.path.exists(expected))
        self._builder.build(self._ROOT_DIR, self._PARAMS)
        assert_that(os.path.exists(expected))
        assert_that(os.path.isdir(expected))
