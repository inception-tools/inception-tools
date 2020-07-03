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

from hamcrest import assert_that

from pyincept.architype_parameters import ArchitypeParameters
from pyincept.project_builder import ProjectBuilder
from tests.pyincept_test_base import PyinceptTestBase


class TestProjectBuilder(PyinceptTestBase):
    """
    Unit test for class :py:class:`ProjectBuilder`.
    """

    ##############################
    # Class attributes

    # See superclass declaration to understand the use of this attribute.
    _OVERWRITE_EXPECTED_FILE = False

    _PROJECT_ROOT = 'some_project_root'
    _PARAMS = ArchitypeParameters(
        'some_package_name',
        'some_author',
        'some_author_email',
        datetime(2020, 1, 1)
    )

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

    # Instance set up / tear down

    def setup(self):
        """
        Called before each method in this class with a name of the form
        test_*().
        """
        self._builder = ProjectBuilder(self._PROJECT_ROOT, self._PARAMS)

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
        assert_that(
            os.path.isdir(self._PROJECT_ROOT),
            'Directory not found: {}'.format(self._PROJECT_ROOT)
        )

    def test_build_creates_license_file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_correct(self._PROJECT_ROOT, 'LICENSE')

    def test_build_creates_readme_file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_correct(self._PROJECT_ROOT, 'README.rst')

    def test_build_creates_setup_cfg(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_correct(self._PROJECT_ROOT, 'setup.cfg')

    def test_build_creates_setup_py(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_correct(self._PROJECT_ROOT, 'setup.py')

    def test_build_creates_log_cfg(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_correct(self._PROJECT_ROOT, 'log.cfg')

    def test_build_creates_makefile(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_correct(self._PROJECT_ROOT, 'Makefile')

    def test_build_creates_pipfile(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        self._validate_output_file_correct(self._PROJECT_ROOT, 'Pipfile')

    def test_build_creates_entry_point_file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join(
            self._PARAMS.package_name,
            '{}.py'.format(self._PARAMS.package_name)
        )
        self._validate_output_file_correct(self._PROJECT_ROOT, file_path)

    def test_build_creates_package___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join(self._PARAMS.package_name, '__init__.py')
        self._validate_output_file_correct(self._PROJECT_ROOT, file_path)

    def test_build_creates_tests___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join('tests', '__init__.py')
        self._validate_output_file_correct(self._PROJECT_ROOT, file_path)

    def test_build_creates_unit_tests___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join('tests', 'unit', '__init__.py')
        self._validate_output_file_correct(self._PROJECT_ROOT, file_path)

    def test_build_creates_integration_tests___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join('tests', 'integration', '__init__.py')
        self._validate_output_file_correct(self._PROJECT_ROOT, file_path)

    def test_build_creates_end_to_end_tests___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join('tests', 'end_to_end', '__init__.py')
        self._validate_output_file_correct(self._PROJECT_ROOT, file_path)

    def test_build_creates_unit_tests_package___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join(
            'tests',
            'unit',
            'test_some_package_name',
            '__init__.py'
        )
        self._validate_output_file_correct(self._PROJECT_ROOT, file_path)

    def test_build_creates_integration_tests_package___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join(
            'tests',
            'integration',
            'test_some_package_name',
            '__init__.py'
        )
        self._validate_output_file_correct(self._PROJECT_ROOT, file_path)

    def test_build_creates_end_to_end_tests_package___init___file(self):
        """
        Unit test case for :py:method:`ProjectBuilder.build`.
        """
        file_path = os.path.join(
            'tests',
            'end_to_end',
            'test_some_package_name',
            '__init__.py'
        )
        self._validate_output_file_correct(self._PROJECT_ROOT, file_path)
