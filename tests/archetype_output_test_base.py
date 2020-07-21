"""
    pyincept_test_base
    ~~~~~~~~~~~~~~~~~~

    Houses the declaration of :py:class:`ArchetypeOutputTestBase` along with
    supporting classes, functions, and attributes.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

#  Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.
#

import datetime
import os
import shutil
from abc import abstractmethod
from typing import Union

from hamcrest import assert_that, is_

from pyincept.archetype_parameters import ArchetypeParameters
from pyincept.constants import UNIMPLEMENTED_ABSTRACT_METHOD_ERROR
from tests.file_matcher import exists, is_dir, is_file, not_exists


class _ArchetypeTestOutput(object):
    """
    A container for grouping information used to validate individual
    archetype output files.

    Attributes:
    * ``subpath`` - subpath under the root directory where the file should
    exist
    * ``is_file`` - ``True`` if the subpath represents a file, ``False``
    if it represents a directory
    """

    def __init__(
            self,
            subpath: str,
            expected_output_path: Union[str, None]
    ) -> None:
        self.subpath = subpath
        self.expected_output_path = expected_output_path


class ArchetypeOutputTestBase(object):
    """
    Common base test class for test cases that validate the content of
    template files.
    """

    ##############################
    # Class attributes

    # This can be temporarily set to `True` in order to automatically
    # regenerated and overwrite the expected output files for test results.
    # This makes it easy to ensure that changes to the Jinja template files
    # are propagated without the need to spend a bunch of time making sure
    # the expected output matches the new template changes.  Any changes in
    # output are easy to manually compare and validate before committing
    # using your IDE's source control integration. Note that this file should
    # never be committed with a value of True, as it will make any pass/fail
    # test results meaningless.  See also,
    # :py:meth:`test_overwrite_expected_files_is_false`.
    _OVERWRITE_EXPECTED_FILE = False

    _ROOT_DIR = 'some_root_dir'

    _PACKAGE_NAME = 'some_package_name'
    _AUTHOR = 'some_author'
    _AUTHOR_EMAIL = 'some_author_email'
    _DATE = datetime.date(2000, 1, 1)

    _PARAMS = ArchetypeParameters(_PACKAGE_NAME, _AUTHOR, _AUTHOR_EMAIL, _DATE)

    ##############################
    # Class / static methods

    @classmethod
    @abstractmethod
    def _get_resource_path(cls, resource_name):
        """
        This method returns the path of a given resource name.

        :param resource_name:
        :return:
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR

    @classmethod
    def _get_file_content(cls, resource_path):
        with open(resource_path) as f:
            return f.read()

    @classmethod
    def _put_file_content(cls, resource_path, content):
        with open(resource_path, 'w') as f:
            return f.write(content)

    @classmethod
    def _validate_path_doesnt_exist(cls, path_):
        assert_that(
            not os.path.exists(path_),
            'Directory/file should be absent: {}'.format(path_)
        )

    @classmethod
    def _assert_matching_file_content(cls, actual_path, expected_path):
        actual_content = cls._get_file_content(actual_path)

        if cls._OVERWRITE_EXPECTED_FILE:
            cls._put_file_content(expected_path, actual_content)
        expected_content = cls._get_file_content(expected_path)

        assert_that(actual_content, is_(expected_content))

    @classmethod
    def _validate_output_file_correct(cls, project_root, relative_path):
        actual_path = os.path.join(project_root, relative_path)
        expected_path = cls._get_resource_path(relative_path)
        cls._assert_matching_file_content(actual_path, expected_path)

    ##############################
    # Instance methods

    def _validate_archetype_output(self, actual_root_dir, expected_output):
        for test_output in expected_output:
            actual_path = os.path.join(actual_root_dir, test_output.subpath)
            assert_that(actual_path, exists())

            if test_output.expected_output_path is not None:
                assert_that(actual_path, is_file())
                actual_content = self._get_file_content(actual_path)

                expected_path = test_output.expected_output_path
                if self._OVERWRITE_EXPECTED_FILE:
                    self._put_file_content(expected_path, actual_content)
                assert_that(expected_path, is_file())
                expected_content = self._get_file_content(expected_path)

                assert_that(actual_content, is_(expected_content))
            else:
                assert_that(actual_path, is_dir())

    # Instance set up / tear down

    def setup(self):
        """
        Called before each method in this class with a name of the form
        test_*().
        """
        # The project root directory should not already exist.  If it does,
        # something unexpected has happened, so raise.
        assert_that(self._ROOT_DIR, not_exists())

    def teardown(self):
        """
        Called after each method in this class with a name of the form
        test_*().
        """
        if os.path.exists(self._ROOT_DIR):
            shutil.rmtree(self._ROOT_DIR)

        assert_that(self._ROOT_DIR, not_exists())

    # Test cases

    def test_overwrite_expected_files_is_false(self):
        """
        This 'test case' validates that the value of
        `self._OVERWRITE_EXPECTED_FILE` is `False`, ensuring that the unit
        test suite will be unable to pass if it is accidentally committed
        with a `True` value.  See inline comments of
        `self._OVERWRITE_EXPECTED_FILE` a more detailed explanation of how
        that attribute is used.
        """
        assert_that(
            not self._OVERWRITE_EXPECTED_FILE,
            'The following value should always be False: '
            'self._OVERWRITE_EXPECTED_FILE={}'.format(
                self._OVERWRITE_EXPECTED_FILE
            )
        )
