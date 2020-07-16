"""
test_directory_builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`directory_builder` module.
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
from pyincept.directory_builder import DirectoryBuilder
from tests.pyincept_test_base import PyinceptTestBase


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

        self._builder = _MockDirectoryBuilder('some_subpath')

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
        Unit test case for :py:method:`DirectoryBuilder.path`.
        """
        actual = self._builder.path(self._PROJECT_ROOT, self._PARAMS)
        expected = os.path.join('some_project_root', 'some_subpath')
        assert_that(actual, is_(expected))

    def test_build(self):
        """
        Unit test case for :py:method:`DirectoryBuilder.build`.
        """
        expected = os.path.join('some_project_root', 'some_subpath')

        assert_that(not os.path.exists(expected))
        self._builder.build(self._PROJECT_ROOT, self._PARAMS)
        assert_that(os.path.exists(expected))
        assert_that(os.path.isdir(expected))
