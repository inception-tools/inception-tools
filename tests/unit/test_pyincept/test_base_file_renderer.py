"""
    test_base_file_renderer
    ~~~~~~~~~~~~~~~~~~~~~~~

    Unit test cases for the :py:mod:`base_file_renderer` module.

    ~~~~~~~~~~~~~~~~~~~~~~~

    Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

import os
import shutil
from datetime import datetime

from hamcrest import assert_that, is_

from pyincept.architype_parameters import ArchitypeParameters
from pyincept.base_file_renderer import BaseFileRenderer
from tests.pyincept_test_base import PyinceptTestBase


class _MockFileRenderer(BaseFileRenderer):

    def __init__(self, subpath, render_content) -> None:
        super().__init__()
        self.subpath_value = subpath
        self.render_value = render_content

    def subpath(self, params: ArchitypeParameters) -> str:
        return self.subpath_value

    def render(self, params: ArchitypeParameters) -> str:
        return self.render_value


class TestBaseFileRenderer(object):
    """
    Unit test for class :py:class:`BaseFileRenderer`.
    """

    ##############################
    # Class attributes

    _PROJECT_ROOT = 'some_project_root'
    _PARAMS = ArchitypeParameters(
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

        self._file_renderer = _MockFileRenderer('some_subpath', 'some_content')

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
        Unit test case for :py:method:`BaseFileRenderer.path`.
        """
        actual = self._file_renderer.path(self._PROJECT_ROOT, self._PARAMS)
        expected = os.path.join('some_project_root', 'some_subpath')
        assert_that(actual, is_(expected))

    def test_render_and_save(self):
        """
        Unit test case for :py:method:`BaseFileRenderer.render_and_save`.
        """
        self._file_renderer.render_and_save(self._PROJECT_ROOT, self._PARAMS)

        with open(os.path.join('some_project_root', 'some_subpath')) as f:
            actual = f.read()

        expected = 'some_content'

        assert_that(actual, is_(expected))
