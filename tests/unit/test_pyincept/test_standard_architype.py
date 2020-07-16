"""
    test_standard_archetype
    ~~~~~~~~~~~~~~~~~~~~~~~

    Unit test cases for the :py:mod:`standard_archetype` module.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

import os
import shutil

from hamcrest import assert_that

from pyincept.standard_archetype import (
    DefaultArchetype,
)
from tests.pyincept_test_base import PyinceptTestBase


class TestStandardArchetype(PyinceptTestBase):
    """
    Unit test for class :py:class:`ProjectBuilder`.
    """

    ##############################
    # Class attributes

    # See superclass declaration to understand the use of this attribute.
    _OVERWRITE_EXPECTED_FILE = False

    _ROOT_DIR = PyinceptTestBase._ROOT_DIR
    _PARAMS = PyinceptTestBase._PARAMS

    ##############################
    # Class / static methods

    @classmethod
    def _get_resource_path(cls, resource_name):
        return os.path.abspath(
            os.path.join(
                __file__,
                os.pardir,
                'data',
                'test_standard_archetype',
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
        # The project root directory should not already exist.  If it does,
        # something unexpected has happened, so raise.
        self._validate_path_doesnt_exist(self._ROOT_DIR)

        DefaultArchetype.PROJECT_ROOT.build(self._ROOT_DIR, self._PARAMS)

    def teardown(self):
        """
        Called after each method in this class with a name of the form
        test_*().
        """
        if os.path.exists(self._ROOT_DIR):
            shutil.rmtree(self._ROOT_DIR)

        self._validate_path_doesnt_exist(self._ROOT_DIR)

    # Test cases

    def test_build_creates_root_directory(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        assert_that(
            os.path.isdir(self._ROOT_DIR),
            'Directory not found: {}'.format(self._ROOT_DIR)
        )

    def test_build_creates_license_file(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        self._validate_output_file_correct(self._ROOT_DIR, 'LICENSE')

    def test_build_creates_readme_file(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        self._validate_output_file_correct(self._ROOT_DIR, 'README.rst')

    def test_build_creates_setup_cfg(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        self._validate_output_file_correct(self._ROOT_DIR, 'setup.cfg')

    def test_build_creates_setup_py(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        self._validate_output_file_correct(self._ROOT_DIR, 'setup.py')

    def test_build_creates_log_cfg(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        self._validate_output_file_correct(self._ROOT_DIR, 'log.cfg')

    def test_build_creates_makefile(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        self._validate_output_file_correct(self._ROOT_DIR, 'Makefile')

    def test_build_creates_pipfile(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        self._validate_output_file_correct(self._ROOT_DIR, 'Pipfile')

    def test_build_creates_entry_point_file(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        file_path = os.path.join(self._PARAMS.package_name, 'main.py')
        self._validate_output_file_correct(self._ROOT_DIR, file_path)

    def test_build_creates_package___init___file(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        file_path = os.path.join(self._PARAMS.package_name, '__init__.py')
        self._validate_output_file_correct(self._ROOT_DIR, file_path)

    def test_build_creates_tests___init___file(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        file_path = os.path.join('tests', '__init__.py')
        self._validate_output_file_correct(self._ROOT_DIR, file_path)

    def test_build_creates_unit_tests___init___file(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        file_path = os.path.join('tests', 'unit', '__init__.py')
        self._validate_output_file_correct(self._ROOT_DIR, file_path)

    def test_build_creates_integration_tests___init___file(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        file_path = os.path.join('tests', 'integration', '__init__.py')
        self._validate_output_file_correct(self._ROOT_DIR, file_path)

    def test_build_creates_end_to_end_tests___init___file(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        file_path = os.path.join('tests', 'end_to_end', '__init__.py')
        self._validate_output_file_correct(self._ROOT_DIR, file_path)

    def test_build_creates_unit_tests_package___init___file(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        file_path = os.path.join(
            'tests',
            'unit',
            'test_some_package_name',
            '__init__.py'
        )
        self._validate_output_file_correct(self._ROOT_DIR, file_path)

    def test_build_creates_integration_tests_package___init___file(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        file_path = os.path.join(
            'tests',
            'integration',
            'test_some_package_name',
            '__init__.py'
        )
        self._validate_output_file_correct(self._ROOT_DIR, file_path)

    def test_build_creates_end_to_end_tests_package___init___file(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        file_path = os.path.join(
            'tests',
            'end_to_end',
            'test_some_package_name',
            '__init__.py'
        )
        self._validate_output_file_correct(self._ROOT_DIR, file_path)
