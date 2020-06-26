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
from abc import abstractmethod
from datetime import datetime

from hamcrest import assert_that, is_

from pyincept.project_builder import ProjectBuilder


class PyinceptTestBase(object):
    """
    Common base test class for test cases that validate the content of
    templated files.
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

    ##############################
    # Class / static methods

    @classmethod
    @abstractmethod
    def _get_resource_path(cls, resource_name):
        """
        This method returns the path of a given resource name.

        :param resource_name:
        :return:
        """
        raise NotImplemented('This method must be implemented by subclasses.')

    @classmethod
    def _get_file_content(cls, resource_path):
        with open(resource_path) as f:
            return f.read()

    @classmethod
    def _put_file_content(cls, resource_path, content):
        with open(resource_path, 'w') as f:
            return f.write(content)

    @classmethod
    def _validate_path_doesnt_exist(cls, path_):
        assert_that(
            not os.path.exists(path_),
            'Directory/file should be absent: {}'.format(path_)
        )

    @classmethod
    def _assert_matching_file_content(cls, actual_path, expected_path):
        actual_content = cls._get_file_content(actual_path)

        if cls._OVERWRITE_EXPECTED_FILE:
            cls._put_file_content(expected_path, actual_content)
        expected_content = cls._get_file_content(expected_path)

        assert_that(actual_content, is_(expected_content))

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


class TestProjectBuilder(PyinceptTestBase):
    """
    Unit test for class :py:class:`ProjectBuilder`.
    """

    ##############################
    # Class attributes

    # See superclass declaration to understand the use of this attribute.
    _OVERWRITE_EXPECTED_FILE = False

    _PACKAGE_NAME = 'test_package_name'
    _AUTHOR = 'test_author'
    _AUTHOR_EMAIL = 'test_author_email'
    _PROJECT_ROOT = 'test_project_root'
    _DATE = datetime(2020, 1, 1)

    ##############################
    # Class / static methods

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

    @classmethod
    def _validate_output_file_created(cls, output_file_name):
        actual_path = os.path.join(cls._PROJECT_ROOT, output_file_name)
        expected_path = cls._get_resource_path(output_file_name)
        cls._assert_matching_file_content(actual_path, expected_path)

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
        self._validate_path_doesnt_exist(self._PROJECT_ROOT)

        self._builder.build()

    def teardown(self):
        """
        Called after each method in this class with a name of the form
        test_*().
        """
        if os.path.exists(self._PROJECT_ROOT):
            shutil.rmtree(self._PROJECT_ROOT)

        self._validate_path_doesnt_exist(self._PROJECT_ROOT)

    # Test cases

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
            'test_package_name',
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
            'test_package_name',
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
            'test_package_name',
            '__init__.py'
        )
        self._validate_output_file_created(file_path)
