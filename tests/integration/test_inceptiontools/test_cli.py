"""
    test_cli
    ~~~~~~~~~

    Unit test cases for the :py:mod:`inceptiontools.cli` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os
from unittest import mock

from click.testing import CliRunner

from inceptiontools import cli
from tests.archetype_output_test_base import (
    _OutputDir,
    _OutputFile,
    ArchetypeOutputTestBase,
)


class TestIncept(ArchetypeOutputTestBase):
    """
    Unit test for the function :py:func:`inceptiontools.cli.incept`.
    """

    ##############################
    # Class attributes

    # See superclass declaration to understand the use of this attribute.
    _OVERWRITE_EXPECTED_FILE = False

    _PACKAGE_NAME = ArchetypeOutputTestBase._PACKAGE_NAME
    _ROOT_DIR = _PACKAGE_NAME

    _TEST_RESOURCE_PATH = os.path.abspath(
        os.path.join(
            __file__,
            os.pardir,
            "data",
            "test_main",
        )
    )

    _EXPECTED_DIRS = ("scripts", "docs")

    _EXPECTED_FILES = (
        ("LICENSE",),
        ("README.rst",),
        ("setup.cfg",),
        ("setup.py",),
        ("log.cfg",),
        ("Makefile",),
        ("Pipfile",),
        (_PACKAGE_NAME, "__init__.py"),
        (_PACKAGE_NAME, "cli.py"),
        ("tests", "__init__.py"),
        ("tests", "end_to_end", "__init__.py"),
        ("tests", "integration", "__init__.py"),
        ("tests", "unit", "__init__.py"),
    )

    ##############################
    # Class / static methods

    @classmethod
    def _expected_files(cls):
        return tuple(
            _OutputFile(os.path.join(*s), os.path.join(cls._TEST_RESOURCE_PATH, *s))
            for s in cls._EXPECTED_FILES
        )

    @classmethod
    def _expected_dirs(cls):
        return tuple(_OutputDir(s) for s in cls._EXPECTED_DIRS)

    ##############################
    # Instance methods

    # Test cases

    @mock.patch("inceptiontools.cli.datetime")
    def test_incept_builds_standard_archetype(self, mock_datetime):
        """
        Unit test case for :py:func:`inceptiontools.cli.incept`.
        """
        mock_datetime.now.return_value = self._DATE
        CliRunner().invoke(
            cli.cli, ("incept", self._PACKAGE_NAME, self._AUTHOR, self._AUTHOR_EMAIL)
        )
        self._validate_archetype_files(self._ROOT_DIR, self._expected_files())
        self._validate_archetype_dirs(self._ROOT_DIR, self._expected_dirs())
