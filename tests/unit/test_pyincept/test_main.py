"""
    test_main
    ~~~~~~~~~

    Unit test cases for the :py:mod:`pyincept.main` module.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

import logging
import os
from contextlib import closing
from io import StringIO
from logging import StreamHandler
from unittest import mock

from click.testing import CliRunner
from hamcrest import assert_that, contains_string, is_, starts_with

from pyincept import main
from tests.pyincept_test_base import PyinceptTestBase


class TestMain(PyinceptTestBase):
    """
    Unit test for class :py:mod:`pyincept`.
    """

    ##############################
    # Class attributes

    # See superclass declaration to understand the use of this attribute.
    _OVERWRITE_EXPECTED_FILE = False

    _ROOT_DIR = PyinceptTestBase._PACKAGE_NAME

    _EXCEPTION = ValueError('Some test exception.')

    ##############################
    # Class / static methods

    @classmethod
    def _get_resource_path(cls, resource_name):
        return os.path.abspath(
            os.path.join(
                __file__,
                os.pardir,
                'data',
                'test_pyincept',
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

        self._runner = CliRunner()
        self._result = self._runner.invoke(
            main.build,
            (self._PACKAGE_NAME, self._AUTHOR, self._AUTHOR_EMAIL)
        )

    # Test cases

    def test_main_emits_nothing_on_successful_execution(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        assert_that(self._result.stdout_bytes, is_(b''))
        assert_that(self._result.stderr_bytes, is_(None))

    @mock.patch('pyincept.main._main')
    def test_main_emits_nothing_for_unhandled_exception(self, mock__main):
        """
        Unit test case for :py:method:`main.build`.
        """
        mock__main.side_effect = self._EXCEPTION

        result = self._runner.invoke(
            main.build,
            (self._PACKAGE_NAME, self._AUTHOR, self._AUTHOR_EMAIL)
        )

        assert_that(result.stdout_bytes, is_(b''))
        assert_that(result.stderr_bytes, is_(None))

    def test_main_maps_project_root(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        dir_path = self._PACKAGE_NAME
        assert_that(
            os.path.isdir(dir_path),
            'Directory not found: {}'.format(dir_path)
        )

    def test_main_maps_package_name(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        dir_path = os.path.join(self._PACKAGE_NAME, 'setup.py')
        content = self._get_file_content(dir_path)
        substring = 'Package distribution file for the {} library.'.format(
            self._PACKAGE_NAME
        )
        assert_that(content, contains_string(substring))

    def test_main_maps_author_name(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        dir_path = os.path.join(self._PACKAGE_NAME, 'setup.py')
        content = self._get_file_content(dir_path)
        substring = "__author__ = '{}'".format(self._AUTHOR)
        assert_that(content, contains_string(substring))

    def test_main_maps_author_email(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        dir_path = os.path.join(self._PACKAGE_NAME, 'setup.cfg')
        content = self._get_file_content(dir_path)
        substring = "author_email = {}".format(self._AUTHOR_EMAIL)
        assert_that(content, contains_string(substring))

    def test_main_maps_date(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        dir_path = os.path.join(self._PACKAGE_NAME, 'setup.py')
        content = self._get_file_content(dir_path)
        substring = 'Copyright (c) {}'.format(self._DATE.year)
        assert_that(content, contains_string(substring))

    def test_main_leaves_exit_status_0_on_success(self):
        """
        Unit test case for :py:method:`main.build`.
        """
        assert_that(self._result.exit_code, is_(0))

    @mock.patch('pyincept.main._main')
    def test_main_leaves_exit_status_1_on_unhandled_error(self, mock__main):
        """
        Unit test case for :py:method:`main.build`.
        """
        mock__main.side_effect = self._EXCEPTION

        result = self._runner.invoke(
            main.build,
            (self._PACKAGE_NAME, self._AUTHOR, self._AUTHOR_EMAIL)
        )

        assert_that(result.exit_code, is_(1))

    @mock.patch('pyincept.main._logger')
    @mock.patch('pyincept.main._main')
    def test_main_logs_unhandled_errors(self, mock__main, mock__logger):
        """
        Unit test case for :py:method:`main.build`.
        """
        mock__main.side_effect = self._EXCEPTION

        with closing(StringIO()) as sio:
            stream_handler = StreamHandler(sio)
            logger = logging.getLogger('test_pyincept_mock_logger')
            logger.addHandler(stream_handler)
            mock__logger.return_value = logger
            self._runner.invoke(
                main.build,
                (self._PACKAGE_NAME, self._AUTHOR, self._AUTHOR_EMAIL)
            )

            actual = sio.getvalue()

        expected = 'Unexpected exception: package_name=some_package_name, ' \
                   'author=some_author, author_email=some_author_email\n'

        assert_that(actual, starts_with(expected))
