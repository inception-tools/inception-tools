"""
    test_main
    ~~~~~~~~~

    Unit test cases for the :py:mod:`inceptiontools.main` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import logging
import os
from contextlib import closing
from io import StringIO
from logging import StreamHandler
from unittest import mock

from click.testing import CliRunner
from hamcrest import assert_that, contains_string, is_, starts_with

from inceptiontools import main
from tests.archetype_output_test_base import ArchetypeOutputTestBase


class TestIncept(ArchetypeOutputTestBase):
    """
    Unit test for the function :py:func:`inceptiontools.main.incept`.
    """

    ##############################
    # Class attributes

    # See superclass declaration to understand the use of this attribute.
    _OVERWRITE_EXPECTED_FILE = False

    _ROOT_DIR = ArchetypeOutputTestBase._PACKAGE_NAME

    _EXCEPTION = ValueError("Some test exception.")

    ##############################
    # Instance methods

    # Instance set up / tear down

    # TODO: Something changed here. Two arguments are now requires where before, only
    #  one was.  Need to understand why this is and come up with a better pattern.
    @mock.patch("inceptiontools.main.datetime")
    def setup(self, _, mock_datetime):
        """
        Called before each method in this class with a name of the form
        test_*().
        """
        super(TestIncept, self).setup()

        mock_datetime.now.return_value = self._DATE

        self._runner = CliRunner()
        self._result = self._runner.invoke(
            main.incept, (self._PACKAGE_NAME, self._AUTHOR, self._AUTHOR_EMAIL)
        )

    # Test cases

    def test_incept_emits_nothing_on_successful_execution(self):
        """
        Unit test case for :py:func:`inceptiontools.main.incept`.
        """
        assert_that(self._result.stdout_bytes, is_(b""))
        assert_that(self._result.stderr_bytes, is_(None))

    @mock.patch("inceptiontools.main._incept")
    def test_incept_emits_nothing_for_unhandled_exception(self, mock__main):
        """
        Unit test case for :py:func:`inceptiontools.main.incept`.
        """
        mock__main.side_effect = self._EXCEPTION

        result = self._runner.invoke(
            main.incept, (self._PACKAGE_NAME, self._AUTHOR, self._AUTHOR_EMAIL)
        )

        assert_that(result.stdout_bytes, is_(b""))
        assert_that(result.stderr_bytes, is_(None))

    def test_incept_maps_project_root(self):
        """
        Unit test case for :py:func:`inceptiontools.main.incept`.
        """
        dir_path = self._PACKAGE_NAME
        assert_that(os.path.isdir(dir_path), "Directory not found: {}".format(dir_path))

    def test_incept_maps_package_name(self):
        """
        Unit test case for :py:func:`inceptiontools.main.incept`.
        """
        dir_path = os.path.join(self._PACKAGE_NAME, "setup.py")
        content = self._get_file_content(dir_path)
        substring = "Package distribution file for the {} library.".format(
            self._PACKAGE_NAME
        )
        assert_that(content, contains_string(substring))

    def test_incept_maps_author_name(self):
        """
        Unit test case for :py:func:`inceptiontools.main.incept`.
        """
        dir_path = os.path.join(self._PACKAGE_NAME, "setup.py")
        content = self._get_file_content(dir_path)
        substring = "__author__ = '{}'".format(self._AUTHOR)
        assert_that(content, contains_string(substring))

    def test_incept_maps_author_email(self):
        """
        Unit test case for :py:func:`inceptiontools.main.incept`.
        """
        dir_path = os.path.join(self._PACKAGE_NAME, "setup.cfg")
        content = self._get_file_content(dir_path)
        substring = "author_email = {}".format(self._AUTHOR_EMAIL)
        assert_that(content, contains_string(substring))

    def test_incept_maps_date(self):
        """
        Unit test case for :py:func:`inceptiontools.main.incept`.
        """
        dir_path = os.path.join(self._PACKAGE_NAME, "setup.py")
        content = self._get_file_content(dir_path)
        substring = "Copyright (c) {}".format(self._DATE.year)
        assert_that(content, contains_string(substring))

    def test_incept_leaves_exit_status_0_on_success(self):
        """
        Unit test case for :py:func:`inceptiontools.main.incept`.
        """
        assert_that(self._result.exit_code, is_(0))

    @mock.patch("inceptiontools.main._incept")
    def test_incept_leaves_exit_status_1_on_unhandled_error(self, mock__main):
        """
        Unit test case for :py:func:`inceptiontools.main.incept`.
        """
        mock__main.side_effect = self._EXCEPTION

        result = self._runner.invoke(
            main.incept, (self._PACKAGE_NAME, self._AUTHOR, self._AUTHOR_EMAIL)
        )

        assert_that(result.exit_code, is_(1))

    @mock.patch("inceptiontools.main._logger")
    @mock.patch("inceptiontools.main._incept")
    def test_incept_logs_unhandled_errors(self, mock__main, mock__logger):
        """
        Unit test case for :py:func:`inceptiontools.main.incept`.
        """
        mock__main.side_effect = self._EXCEPTION

        with closing(StringIO()) as sio:
            stream_handler = StreamHandler(sio)
            logger = logging.getLogger("test_inceptiontools_mock_logger")
            logger.addHandler(stream_handler)
            mock__logger.return_value = logger
            self._runner.invoke(
                main.incept, (self._PACKAGE_NAME, self._AUTHOR, self._AUTHOR_EMAIL)
            )

            actual = sio.getvalue()

        expected = (
            "Unexpected exception: package_name=some_package_name, "
            "author=some_author, author_email=some_author_email\n"
        )

        assert_that(actual, starts_with(expected))
