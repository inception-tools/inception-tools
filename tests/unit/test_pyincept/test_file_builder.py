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
from datetime import datetime

from hamcrest import assert_that, is_

from pyincept.archetype_parameters import ArchetypeParameters
from pyincept.file_builder import FileBuilder
from tests.pyincept_test_base import PyinceptTestBase


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

    _PROJECT_ROOT = 'some_project_root'
    _PARAMS = ArchetypeParameters(
        'some_package_name',
        'some_author',
        'some_author_email',
        datetime(2000, 1, 1)
    )

    ##############################
    # Instance methods

    # Instance set up / tear down

    def setup(self):
        """
        Called before each method in this class with a name of the form
        test_*().
        """
        PyinceptTestBase._validate_path_doesnt_exist(self._PROJECT_ROOT)

        self._file_builder = _MockFileBuilder('some_subpath', 'some_content')

    def teardown(self):
        """
        Called after each method in this class with a name of the form
        test_*().
        """
        if os.path.exists(self._PROJECT_ROOT):
            shutil.rmtree(self._PROJECT_ROOT)

        PyinceptTestBase._validate_path_doesnt_exist(self._PROJECT_ROOT)

    # Test cases

    def test_path(self):
        """
        Unit test case for :py:method:`FileBuilder.path`.
        """
        actual = self._file_builder.path(self._PROJECT_ROOT, self._PARAMS)
        expected = os.path.join('some_project_root', 'some_subpath')
        assert_that(actual, is_(expected))

    def test_build(self):
        """
        Unit test case for :py:method:`FileBuilder.build`.
        """
        self._file_builder.build(self._PROJECT_ROOT, self._PARAMS)

        with open(os.path.join('some_project_root', 'some_subpath')) as f:
            actual = f.read()

        expected = 'some_content'

        assert_that(actual, is_(expected))
