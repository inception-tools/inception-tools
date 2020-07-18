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

from pyincept.standard_archetype import (
    StandardArchetype,
)
from tests.pyincept_test_base import _TestOutput, PyinceptTestBase


class TestStandardArchetype(PyinceptTestBase):
    """
    Unit test for class :py:class:`ProjectBuilder`.
    """

    ##############################
    # Class attributes

    # See superclass declaration to understand the use of this attribute.
    _OVERWRITE_EXPECTED_FILE = False

    _TEST_RESOURCE_PATH = os.path.abspath(
        os.path.join(
            __file__,
            os.pardir,
            'data',
            'test_standard_archetype',
        )
    )

    _EXPECTED_OUTPUT = (
        _TestOutput('scripts', None),
        _TestOutput('docs', None),
        _TestOutput('LICENSE', os.path.join(_TEST_RESOURCE_PATH, 'LICENSE')),
        _TestOutput(
            'README.rst',
            os.path.join(_TEST_RESOURCE_PATH, 'README.rst')
        ),
        _TestOutput(
            'setup.cfg',
            os.path.join(_TEST_RESOURCE_PATH, 'setup.cfg')
        ),
        _TestOutput('setup.py', os.path.join(_TEST_RESOURCE_PATH, 'setup.py')),
        _TestOutput('log.cfg', os.path.join(_TEST_RESOURCE_PATH, 'log.cfg')),
        _TestOutput('Makefile', os.path.join(_TEST_RESOURCE_PATH, 'Makefile')),
        _TestOutput('Pipfile', os.path.join(_TEST_RESOURCE_PATH, 'Pipfile')),
        _TestOutput(
            os.path.join(PyinceptTestBase._PACKAGE_NAME, 'main.py'),
            os.path.join(
                _TEST_RESOURCE_PATH,
                PyinceptTestBase._PACKAGE_NAME,
                'main.py'
            )
        ),
        _TestOutput(
            os.path.join(PyinceptTestBase._PACKAGE_NAME, '__init__.py'),
            os.path.join(
                _TEST_RESOURCE_PATH,
                PyinceptTestBase._PACKAGE_NAME,
                '__init__.py'
            )
        ),
    )

    ##############################
    # Class / static methods

    @classmethod
    def _get_resource_path(cls, resource_name):
        return os.path.join(cls._TEST_RESOURCE_PATH, resource_name)

    ##############################
    # Instance methods

    # Instance set up / tear down

    def setup(self):
        """
        Called before each method in this class with a name of the form
        test_*().
        """
        super(TestStandardArchetype, self).setup()
        StandardArchetype.APPLICATION.build(self._ROOT_DIR, self._PARAMS)

    # Test cases

    def test_build(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        StandardArchetype.APPLICATION.build(self._ROOT_DIR, self._PARAMS)
        self._validate_archetype_output(self._ROOT_DIR, self._EXPECTED_OUTPUT)

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
