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

from hamcrest import assert_that, is_

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

    _PACKAGE_NAME = PyinceptTestBase._PACKAGE_NAME
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
            os.path.join(_PACKAGE_NAME, 'main.py'),
            os.path.join(_TEST_RESOURCE_PATH, _PACKAGE_NAME, 'main.py')
        ),
        _TestOutput(
            os.path.join(_PACKAGE_NAME, '__init__.py'),
            os.path.join(_TEST_RESOURCE_PATH, _PACKAGE_NAME, '__init__.py')
        ),
        _TestOutput(
            os.path.join('tests', '__init__.py'),
            os.path.join(_TEST_RESOURCE_PATH, 'tests', '__init__.py')
        ),
        _TestOutput(
            os.path.join('tests', 'end_to_end', '__init__.py'),
            os.path.join(
                _TEST_RESOURCE_PATH,
                'tests',
                'end_to_end',
                '__init__.py'
            )
        ),
        _TestOutput(
            os.path.join('tests', 'integration', '__init__.py'),
            os.path.join(
                _TEST_RESOURCE_PATH,
                'tests',
                'integration',
                '__init__.py'
            )
        ),
        _TestOutput(
            os.path.join('tests', 'unit', '__init__.py'),
            os.path.join(_TEST_RESOURCE_PATH, 'tests', 'unit', '__init__.py')
        ),
        _TestOutput(
            os.path.join(
                'tests',
                'end_to_end',
                'test_some_package_name',
                '__init__.py'
            ),
            os.path.join(
                _TEST_RESOURCE_PATH,
                'tests',
                'end_to_end',
                'test_some_package_name',
                '__init__.py'
            )
        ),
        _TestOutput(
            os.path.join(
                'tests',
                'integration',
                'test_some_package_name',
                '__init__.py'
            ),
            os.path.join(
                _TEST_RESOURCE_PATH,
                'tests',
                'integration',
                'test_some_package_name',
                '__init__.py'
            )
        ),
        _TestOutput(
            os.path.join(
                'tests',
                'unit',
                'test_some_package_name',
                '__init__.py'
            ),
            os.path.join(
                _TEST_RESOURCE_PATH,
                'tests',
                'unit',
                'test_some_package_name',
                '__init__.py'
            )
        ),
    )

    ##############################
    # Instance methods

    # Test cases

    def test_output_files(self):
        """
        Unit test case for :py:method:`StandardArchetype.APPLICATION
        .output_files`.
        """
        expected = (
            os.path.join(self._ROOT_DIR, j.subpath)
            for j in self._EXPECTED_OUTPUT
        )
        actual = StandardArchetype.APPLICATION.output_files(
            self._ROOT_DIR,
            self._PARAMS
        )
        assert_that(sorted(actual), is_(sorted(expected)))

    def test_build(self):
        """
        Unit test case for :py:method:`StandardArchetype.APPLICATION.build`.
        """
        StandardArchetype.APPLICATION.build(self._ROOT_DIR, self._PARAMS)
        self._validate_archetype_output(self._ROOT_DIR, self._EXPECTED_OUTPUT)
