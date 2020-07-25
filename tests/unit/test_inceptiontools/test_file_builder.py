"""
    test_file_builder
    ~~~~~~~~~~~~~~~~~

    Unit test cases for the :py:mod:`file_builder` module.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

import os
import shutil

from hamcrest import assert_that, is_

from inceptiontools.archetype_parameters import ArchetypeParameters
from inceptiontools.file_builder import FileBuilder
from tests.archetype_output_test_base import ArchetypeOutputTestBase


class _MockFileBuilder(FileBuilder):

    def __init__(self, subpath, render_content) -> None:
        super().__init__()
        self.subpath_value = subpath
        self.render_value = render_content

    def subpath(self, params: ArchetypeParameters) -> str:
        return self.subpath_value

    def render(self, params: ArchetypeParameters) -> str:
        return self.render_value


class TestFileRenderer(object):
    """
    Unit test for class :py:class:`FileBuilder`.
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

        self._builder = _MockFileBuilder('some_subpath', 'some_content')

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
        Unit test case for :py:method:`FileBuilder.path`.
        """
        actual = self._builder.path(self._ROOT_DIR, self._PARAMS)
        expected = os.path.join('some_root_dir', 'some_subpath')
        assert_that(actual, is_(expected))

    def test_build(self):
        """
        Unit test case for :py:method:`FileBuilder.build`.
        """
        self._builder.build(self._ROOT_DIR, self._PARAMS)

        with open(os.path.join('some_root_dir', 'some_subpath')) as f:
            actual = f.read()

        expected = 'some_content'

        assert_that(actual, is_(expected))
