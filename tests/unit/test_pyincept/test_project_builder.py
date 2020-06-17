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

    _PACKAGE_NAME = 'some_test_package_name'
    _AUTHOR = 'some_test_author'
    _AUTHOR_EMAIL = 'some_test_author_email'
    _PROJECT_ROOT = 'some_test_project_root'

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

    def _validate_output_file_created(self, output_file_name):
        self._builder.build()
        expected_content = self.get_test_resource(output_file_name)
        actual_path = os.path.join(
            self._builder.project_root,
            output_file_name
        )
        with open(actual_path) as expected_file:
            actual_content = expected_file.read()
        assert_that(actual_content, is_(expected_content))

    # Instance set up / tear down

    def setup(self):
        """
        Called before each method in this class with a name of the form
        test_*().
        """
        self._builder = ProjectBuilder(
            self._PACKAGE_NAME,
            self._AUTHOR,
            self._AUTHOR_EMAIL,
            self._PROJECT_ROOT
        )

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
            ProjectBuilder(
                self._PACKAGE_NAME,
                self._AUTHOR,
                self._AUTHOR_EMAIL,
                'some*path'
            )

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
        self._validate_output_file_created('LICENSE')

    def test_build_creates_setup_cfg(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_created('setup.cfg')

    def test_build_creates_setup_py(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_created('setup.py')

    def test_build_creates_log_cfg(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_created('log.cfg')

    def test_build_creates_makefile(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_created('Makefile')

    def test_build_creates_pipfile(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_created('Pipfile')

    def test_build_creates_entry_point_file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join(
            self._PACKAGE_NAME,
            '{}.py'.format(self._PACKAGE_NAME)
        )
        self._validate_output_file_created(file_path)

    def test_build_creates_package___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join(self._PACKAGE_NAME, '__init__.py')
        self._validate_output_file_created(file_path)
