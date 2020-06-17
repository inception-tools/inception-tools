"""
    test_project_builder
    ~~~~~~~~~~~~~~~~~~~~~~~
    Unit test cases for the :py:mod:`pyincept.project_builder` module.
    ~~~~~~~~~~~~~~~~~~~~~~~
    Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

import os
import shutil

from hamcrest import assert_that, is_
from pathvalidate import ValidationError
from pytest import raises

from pyincept.project_builder import ProjectBuilder


class TestProjectBuilder(object):
    """
    Unit test for class :py:class:`ProjectBuilder`.
    """

    ##############################
    # Class attributes

    ##############################
    # Class / static methods

    @classmethod
    def get_test_resource(cls, resource_name):
        resource_path = os.path.abspath(
            os.path.join(
                __file__,
                os.pardir,
                '_resources',
                'test_project_builder',
                resource_name
            )
        )
        with open(resource_path) as f:
            return f.read()

    ##############################
    # Instance methods

    def _validate_project_root_absent(self):
        assert_that(
            not os.path.exists(self._builder.project_root),
            'Directory should be empty: {}'.format(self._builder.project_root)
        )

    # Instance set up / tear down

    def setup(self):
        """
        Called before each method in this class with a name of the form
        test_*().
        """
        self._builder = ProjectBuilder('some_test_dir')

        # The project root directory should not already exist.  If it does,
        # something unexpected has happened, so raise.
        self._validate_project_root_absent()

    def teardown(self):
        """
        Called after each method in this class with a name of the form
        test_*().
        """
        if os.path.exists(self._builder.project_root):
            shutil.rmtree(self._builder.project_root)

        self._validate_project_root_absent()

    # Test cases

    def test___init___validates_root_path(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        with raises(ValidationError):
            ProjectBuilder('some*path')

    def test_build_creates_root_directory(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._builder.build()

        assert_that(
            os.path.isdir(self._builder.project_root),
            'Directory not found: {}'.format(self._builder.project_root)
        )

    def test_build_creates_license_file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        output_file_name = 'LICENSE'

        self._builder.build()

        expected_content = self.get_test_resource(output_file_name)

        actual_path = os.path.join(
            self._builder.project_root,
            output_file_name
        )

        with open(actual_path) as expected_file:
            actual_content = expected_file.read()

        assert_that(actual_content, is_(expected_content))
