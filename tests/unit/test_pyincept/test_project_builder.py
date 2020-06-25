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
from datetime import datetime

from hamcrest import assert_that, is_

from pyincept.project_builder import ProjectBuilder


class TestProjectBuilder(object):
    """
    Unit test for class :py:class:`ProjectBuilder`.
    """

    ##############################
    # Class attributes

    # This can be temporarily set to `True` in order to automatically
    # regenerated and overwrite the expected output files for test results.
    # This makes it easy to ensure that changes to the Jinja template files
    # are propagated without the need to spend a bunch of time making sure
    # the expected output matches the new template changes.  Any changes in
    # output are easy to manually compare and validate before committing
    # using your IDE's source control integration. Note that this file should
    # never be committed with a value of True, as it will make any pass/fail
    # test results meaningless.  See also,
    # :py:meth:`test_overwrite_expected_files_is_false`.
    _OVERWRITE_EXPECTED_FILE = False

    _PACKAGE_NAME = 'some_test_package_name'
    _AUTHOR = 'some_test_author'
    _AUTHOR_EMAIL = 'some_test_author_email'
    _PROJECT_ROOT = 'some_test_project_root'
    _DATE = datetime(2020, 1, 1)

    ##############################
    # Class / static methods

    @classmethod
    def _get_test_resource(cls, resource_name):
        resource_path = cls._get_resource_path(resource_name)
        with open(resource_path) as f:
            return f.read()

    @classmethod
    def _put_test_resource(cls, resource_name, content):
        resource_path = cls._get_resource_path(resource_name)
        with open(resource_path, 'w') as f:
            return f.write(content)

    @classmethod
    def _get_resource_path(cls, resource_name):
        return os.path.abspath(
            os.path.join(
                __file__,
                os.pardir,
                '_resources',
                'test_project_builder',
                resource_name
            )
        )

    ##############################
    # Instance methods

    def _validate_project_root_absent(self):
        assert_that(
            not os.path.exists(self._builder.project_root),
            'Directory should be empty: {}'.format(self._builder.project_root)
        )

    def _validate_output_file_created(self, output_file_name):
        self._builder.build()
        actual_path = os.path.join(
            self._builder.project_root,
            output_file_name
        )
        with open(actual_path) as expected_file:
            actual_content = expected_file.read()

        if self._OVERWRITE_EXPECTED_FILE:
            self._put_test_resource(output_file_name, actual_content)

        expected_content = self._get_test_resource(output_file_name)

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
            self._PROJECT_ROOT,
            self._DATE
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

    def test_overwrite_expected_files_is_false(self):
        """
        This 'test case' validates that the value of
        `self._OVERWRITE_EXPECTED_FILE` is `False`, ensuring that the unit
        test suite will be unable to pass if it is accidentally committed
        with a `True` value.  See inline comments of
        `self._OVERWRITE_EXPECTED_FILE` a more detailed explanation of how
        that attribute is used.
        """
        assert_that(
            not self._OVERWRITE_EXPECTED_FILE,
            'The following value should always be False: '
            'self._OVERWRITE_EXPECTED_FILE={}'.format(
                self._OVERWRITE_EXPECTED_FILE
            )
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

    def test_build_creates_readme_file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_created('README.rst')

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

    def test_build_creates_tests___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join('tests', '__init__.py')
        self._validate_output_file_created(file_path)

    def test_build_creates_unit_tests___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join('tests', 'unit', '__init__.py')
        self._validate_output_file_created(file_path)

    def test_build_creates_integration_tests___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join('tests', 'integration', '__init__.py')
        self._validate_output_file_created(file_path)

    def test_build_creates_end_to_end_tests___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join('tests', 'end_to_end', '__init__.py')
        self._validate_output_file_created(file_path)

    def test_build_creates_unit_tests_package___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join(
            'tests',
            'unit',
            'some_test_package_name',
            '__init__.py'
        )
        self._validate_output_file_created(file_path)

    def test_build_creates_integration_tests_package___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join(
            'tests',
            'integration',
            'some_test_package_name',
            '__init__.py'
        )
        self._validate_output_file_created(file_path)

    def test_build_creates_end_to_end_tests_package___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join(
            'tests',
            'end_to_end',
            'some_test_package_name',
            '__init__.py'
        )
        self._validate_output_file_created(file_path)
