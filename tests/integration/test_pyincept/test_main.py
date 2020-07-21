"""
    test_main
    ~~~~~~~~~

    Unit test cases for the :py:mod:`pyincept.main` module.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

import os
from unittest import mock

from click.testing import CliRunner
from hamcrest import assert_that

from pyincept import main
from tests.archetype_output_test_base import ArchetypeOutputTestBase


class TestMain(ArchetypeOutputTestBase):
    """
    Unit test for class :py:mod:`pyincept`.
    """

    ##############################
    # Class attributes

    # See superclass declaration to understand the use of this attribute.
    _OVERWRITE_EXPECTED_FILE = False

    _ROOT_DIR = ArchetypeOutputTestBase._PACKAGE_NAME

    ##############################
    # Class / static methods

    @classmethod
    def _get_resource_path(cls, resource_name):
        return os.path.abspath(
            os.path.join(
                __file__,
                os.pardir,
                'data',
                'test_main',
                resource_name
            )
        )

    ##############################
    # Instance methods

    # Instance set up / tear down

    @mock.patch('pyincept.main.datetime')
    def setup(self, mock_datetime):
        """
        Called before each method in this class with a name of the form
        test_*().
        """
        super(TestMain, self).setup()

        mock_datetime.now.return_value = self._DATE

        runner = CliRunner()
        self.result = runner.invoke(
            main.cli,
            ('build', self._PACKAGE_NAME, self._AUTHOR, self._AUTHOR_EMAIL)
        )

    # Test cases

    def test_main_creates_root_directory(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        assert_that(
            os.path.isdir(self._PACKAGE_NAME),
            'Directory not found: {}'.format(self._PACKAGE_NAME)
        )

    def test_main_creates_license_file(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        self._validate_output_file_correct(self._PACKAGE_NAME, 'LICENSE')

    def test_main_creates_readme_file(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        self._validate_output_file_correct(self._PACKAGE_NAME, 'README.rst')

    def test_main_creates_setup_cfg(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        self._validate_output_file_correct(self._PACKAGE_NAME, 'setup.cfg')

    def test_main_creates_setup_py(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        self._validate_output_file_correct(self._PACKAGE_NAME, 'setup.py')

    def test_main_creates_log_cfg(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        self._validate_output_file_correct(self._PACKAGE_NAME, 'log.cfg')

    def test_main_creates_makefile(self):
        """
        Unit test case for :py:method:`pyincept.main.build`.
        """
        self._validate_output_file_correct(self._PACKAGE_NAME, 'Makefile')

    def test_main_creates_pipfile(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        self._validate_output_file_correct(self._PACKAGE_NAME, 'Pipfile')

    def test_main_creates_entry_point_file(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        file_path = os.path.join(self._PACKAGE_NAME, 'main.py')
        self._validate_output_file_correct(self._PACKAGE_NAME, file_path)

    def test_main_creates_package___init___file(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        file_path = os.path.join(self._PACKAGE_NAME, '__init__.py')
        self._validate_output_file_correct(self._PACKAGE_NAME, file_path)

    def test_main_creates_tests___init___file(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        file_path = os.path.join('tests', '__init__.py')
        self._validate_output_file_correct(self._PACKAGE_NAME, file_path)

    def test_main_creates_unit_tests___init___file(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        file_path = os.path.join('tests', 'unit', '__init__.py')
        self._validate_output_file_correct(self._PACKAGE_NAME, file_path)

    def test_main_creates_integration_tests___init___file(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        file_path = os.path.join('tests', 'integration', '__init__.py')
        self._validate_output_file_correct(self._PACKAGE_NAME, file_path)

    def test_main_creates_end_to_end_tests___init___file(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        file_path = os.path.join('tests', 'end_to_end', '__init__.py')
        self._validate_output_file_correct(self._PACKAGE_NAME, file_path)

    def test_main_creates_unit_tests_package___init___file(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        file_path = os.path.join(
            'tests',
            'unit',
            'test_some_package_name',
            '__init__.py'
        )
        self._validate_output_file_correct(self._PACKAGE_NAME, file_path)

    def test_main_creates_integration_tests_package___init___file(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        file_path = os.path.join(
            'tests',
            'integration',
            'test_some_package_name',
            '__init__.py'
        )
        self._validate_output_file_correct(self._PACKAGE_NAME, file_path)

    def test_main_creates_end_to_end_tests_package___init___file(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        file_path = os.path.join(
            'tests',
            'end_to_end',
            'test_some_package_name',
            '__init__.py'
        )
        self._validate_output_file_correct(self._PACKAGE_NAME, file_path)
