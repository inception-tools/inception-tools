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
from tests.archetype_output_test_base import (
    _OutputDir, _OutputFile,
    ArchetypeOutputTestBase,
)


class TestStandardArchetype(ArchetypeOutputTestBase):
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

    _PACKAGE_NAME = ArchetypeOutputTestBase._PACKAGE_NAME

    _EXPECTED_DIRS = ('scripts', 'docs')

    _EXPECTED_FILES = (
        ('LICENSE',),
        ('README.rst',),
        ('setup.cfg',),
        ('setup.py',),
        ('log.cfg',),
        ('Makefile',),
        ('Pipfile',),
        (_PACKAGE_NAME, '__init__.py'),
        (_PACKAGE_NAME, 'main.py'),
        ('tests', '__init__.py'),
        ('tests', 'end_to_end', '__init__.py'),
        ('tests', 'integration', '__init__.py'),
        ('tests', 'unit', '__init__.py'),
        ('tests', 'end_to_end', 'test_' + _PACKAGE_NAME, '__init__.py'),
        ('tests', 'integration', 'test_' + _PACKAGE_NAME, '__init__.py'),
        ('tests', 'unit', 'test_' + _PACKAGE_NAME, '__init__.py'),
    )

    @classmethod
    def _expected_files(cls):
        return tuple(
            _OutputFile(
                os.path.join(*s),
                os.path.join(cls._TEST_RESOURCE_PATH, *s)
            )
            for s in cls._EXPECTED_FILES
        )

    @classmethod
    def _expected_dirs(cls):
        return tuple(_OutputDir(s) for s in cls._EXPECTED_DIRS)

    def test_file_paths(self):
        """
        Unit test case for :py:method:`StandardArchetype.APPLICATION
        .file_paths`.
        """
        expected = (
            os.path.join(self._ROOT_DIR, j.subpath)
            for j in self._expected_files()
        )
        actual = StandardArchetype.APPLICATION.file_paths(
            self._ROOT_DIR,
            self._PARAMS
        )
        assert_that(sorted(actual), is_(sorted(expected)))

    def test_dir_paths(self):
        """
        Unit test case for :py:method:`StandardArchetype.APPLICATION
        .file_paths`.
        """
        expected = (
            os.path.join(self._ROOT_DIR, j.subpath)
            for j in self._expected_dirs()
        )
        actual = StandardArchetype.APPLICATION.dir_paths(
            self._ROOT_DIR,
            self._PARAMS
        )
        assert_that(sorted(actual), is_(sorted(expected)))

    def test_build(self):
        """
        Unit test case for :py:method:`StandardArchetype.APPLICATION.build`.
        """
        StandardArchetype.APPLICATION.build(self._ROOT_DIR, self._PARAMS)
        self._validate_archetype_files(self._ROOT_DIR, self._expected_files())
        self._validate_archetype_dirs(self._ROOT_DIR, self._expected_dirs())
