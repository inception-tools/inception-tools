"""
    test_cli
    ~~~~~~~~~

    Unit test cases for the :py:mod:`inception_tools.cli` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os
from unittest import mock

from click.testing import CliRunner
from hamcrest import assert_that, is_

from inception_tools import cli
from inception_tools.standard_archetype import StandardArchetype
from tests.archetype_output_test_base import (
    _OutputDir,
    _OutputFile,
    ArchetypeOutputTestBase,
)


class TestIncept(ArchetypeOutputTestBase):
    """
    Unit test for the function :py:func:`inception_tools.cli.incept`.
    """

    ##############################
    # Class attributes

    # See superclass declaration to understand the use of this attribute.
    _OVERWRITE_EXPECTED_FILE = False

    _PACKAGE_NAME = ArchetypeOutputTestBase._PACKAGE_NAME

    _TEST_RESOURCE_PATH = os.path.abspath(
        os.path.join(__file__, os.pardir, "data", "test_cli", "test_incept")
    )

    _LOGGING_CONFIG = os.path.join(_TEST_RESOURCE_PATH, "test_cli_log.cfg")

    _EXPECTED_DIRS = {
        StandardArchetype.CLI: ("scripts", "docs"),
        StandardArchetype.LIB: ("scripts", "docs"),
        StandardArchetype.SIMPLE: (),
    }

    _EXPECTED_FILES = {
        StandardArchetype.CLI: (
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
            ("tests", "integration", "__init__.py"),
            ("tests", "unit", "__init__.py"),
        ),
        StandardArchetype.LIB: (
            ("LICENSE",),
            ("README.rst",),
            ("setup.cfg",),
            ("setup.py",),
            ("log.cfg",),
            ("Makefile",),
            ("Pipfile",),
            (_PACKAGE_NAME, "__init__.py"),
            (_PACKAGE_NAME, f"{ArchetypeOutputTestBase._PACKAGE_NAME}.py"),
            ("tests", "__init__.py"),
            ("tests", "integration", "__init__.py"),
            ("tests", "unit", "__init__.py"),
        ),
        StandardArchetype.SIMPLE: (
            ("LICENSE",),
            ("README.rst",),
            ("setup.cfg",),
            ("setup.py",),
            ("Makefile",),
            ("Pipfile",),
            (f"{_PACKAGE_NAME}.py",),
            ("tests", "__init__.py"),
        ),
    }

    ##############################
    # Class / static methods

    @classmethod
    def _expected_files(cls, a: StandardArchetype):
        return tuple(
            _OutputFile(
                os.path.join(*s),
                os.path.join(cls._TEST_RESOURCE_PATH, a.archetype_resource_id, *s),
            )
            for s in cls._EXPECTED_FILES[a]
        )

    @classmethod
    def _expected_dirs(cls, a: StandardArchetype):
        return tuple(_OutputDir(s) for s in cls._EXPECTED_DIRS[a])

    # Instance methods

    def _validate_incept_for_archetype(self, archetype):
        result = CliRunner().invoke(
            cli.cli,
            (
                "incept",
                self._PACKAGE_NAME,
                self._ROOT_DIR,
                "--author-name",
                self._AUTHOR,
                "--author-email",
                self._AUTHOR_EMAIL,
                "--archetype",
                archetype.canonical_name,
            ),
        )
        assert_that(result.output.strip(), is_(""))
        self._validate_archetype_files(self._ROOT_DIR, self._expected_files(archetype))
        self._validate_archetype_dirs(self._ROOT_DIR, self._expected_dirs(archetype))

    ##############################
    # Test cases

    @mock.patch("inception_tools.cli.datetime")
    def test_incept_builds_standard_archetype_cli(self, mock_datetime):
        """
        Unit test case for :py:func:`inception_tools.cli.incept`.
        """
        mock_datetime.now.return_value = self._DATE
        self._validate_incept_for_archetype(StandardArchetype.CLI)

    @mock.patch("inception_tools.cli.datetime")
    def test_incept_builds_standard_archetype_lib(self, mock_datetime):
        """
        Unit test case for :py:func:`inception_tools.cli.incept`.
        """
        mock_datetime.now.return_value = self._DATE
        self._validate_incept_for_archetype(StandardArchetype.LIB)

    @mock.patch("inception_tools.cli.datetime")
    def test_incept_builds_standard_archetype_simple(self, mock_datetime):
        """
        Unit test case for :py:func:`inception_tools.cli.incept`.
        """
        mock_datetime.now.return_value = self._DATE
        self._validate_incept_for_archetype(StandardArchetype.SIMPLE)

    def test_incept_uses_custom_logging_config(self):
        """
        Unit test case for :py:func:`inception_tools.cli.incept`.
        """
        result = CliRunner().invoke(
            cli.cli,
            (
                "-l",
                self._LOGGING_CONFIG,
                "incept",
                self._PACKAGE_NAME,
                self._ROOT_DIR,
                "--author-name",
                self._AUTHOR,
                "--author-email",
                self._AUTHOR_EMAIL,
            ),
        )

        assert_that(
            result.output.strip(),
            is_("test_cli_log DEBUG    Successfully set up logging."),
        )
