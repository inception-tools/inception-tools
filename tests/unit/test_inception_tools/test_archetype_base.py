"""
    test_archetype_base
    ~~~~~~~~~~~~~~~~~~~

    Unit test cases for the :py:mod:`archetype_base` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os
import shutil

from hamcrest import assert_that, is_

from inception_tools.archetype_base import ArchetypeBase
from inception_tools.archetype_parameters import ArchetypeParameters
from inception_tools.directory_builder import DirectoryBuilder
from inception_tools.file_builder import FileBuilder
from tests.archetype_output_test_base import ArchetypeOutputTestBase
from tests.file_matcher import exists, is_dir, is_file


class _MockFileBuilder(FileBuilder):
    def __init__(self, subpath, render_content) -> None:
        super().__init__()
        self.subpath_value = subpath
        self.render_value = render_content

    def subpath(self, params: ArchetypeParameters) -> str:
        return self.subpath_value

    def render(self, params: ArchetypeParameters) -> str:
        return self.render_value


class _MockDirBuilder(DirectoryBuilder):
    def __init__(self, subpath) -> None:
        super().__init__()
        self.subpath_value = subpath

    def subpath(self, params: ArchetypeParameters) -> str:
        return self.subpath_value


class TestArchetypeBase(object):
    """
    Unit test for class :py:class:`ArchetypeBase`.
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

        self._archetype = ArchetypeBase(
            (
                _MockFileBuilder("some_file", "some_content"),
                _MockFileBuilder("some_other_file", "some_other_content"),
            ),
            (
                _MockDirBuilder("some_dir"),
                _MockDirBuilder("some_other_dir"),
            ),
        )

    def teardown(self):
        """
        Called after each method in this class with a name of the form
        test_*().
        """
        if os.path.exists(self._ROOT_DIR):
            shutil.rmtree(self._ROOT_DIR)

        ArchetypeOutputTestBase._validate_path_doesnt_exist(self._ROOT_DIR)

    # Test cases

    def test_build_creates_files(self):
        """
        Unit test case for :py:method:`ArchetypeBase.build`.
        """
        self._archetype.build(self._ROOT_DIR, self._PARAMS)

        file_paths = (
            os.path.join("some_root_dir", "some_file"),
            os.path.join("some_root_dir", "some_other_file"),
        )
        contents = ("some_content", "some_other_content")
        for path, expected in zip(file_paths, contents):
            assert_that(path, exists())
            assert_that(path, is_file())
            with open(path) as f:
                actual = f.read()
            assert_that(actual, is_(expected))

    def test_build_creates_directories(self):
        """
        Unit test case for :py:method:`ArchetypeBase.build`.
        """
        self._archetype.build(self._ROOT_DIR, self._PARAMS)

        file_paths = (
            os.path.join("some_root_dir", "some_dir"),
            os.path.join("some_root_dir", "some_other_dir"),
        )
        for path in file_paths:
            assert_that(path, exists())
            assert_that(path, is_dir())

    def test_file_paths(self):
        """
        Unit test case for :py:method:`ArchetypeBase.file_paths`.
        """
        actual = self._archetype.file_paths(self._ROOT_DIR, self._PARAMS)
        expected = (
            os.path.join("some_root_dir", "some_file"),
            os.path.join("some_root_dir", "some_other_file"),
        )
        assert_that(actual, is_(expected))

    def test_dir_paths(self):
        """
        Unit test case for :py:method:`ArchetypeBase.dir_paths`.
        """
        actual = self._archetype.dir_paths(self._ROOT_DIR, self._PARAMS)
        expected = (
            os.path.join("some_root_dir", "some_dir"),
            os.path.join("some_root_dir", "some_other_dir"),
        )
        assert_that(actual, is_(expected))
