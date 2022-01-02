"""
test_matchers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`matchers` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os

from hamcrest import assert_that, is_
from hamcrest.core.string_description import StringDescription
from pytest import raises

from tests.file_matcher import (
    exists,
    is_file,
    is_not_file,
    IsDir,
    IsFile,
    not_exists,
    PathExists,
)

_REAL_FILE = __file__
_REAL_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
_FAKE_PATH = "some_fake_path"


class TestPathExists(object):
    """
    Unit test for class :py:class:`PathExists`.
    """

    _EXISTS = PathExists(True)
    _NOT_EXISTS = PathExists(False)

    # Test cases

    def test__matches_should_match_true(self):
        """
        Unit test case for :py:method:`PathExists._matches`.
        """
        assert_that(self._EXISTS._matches(_REAL_FILE), is_(True))
        assert_that(self._EXISTS._matches(_REAL_DIR), is_(True))
        assert_that(self._EXISTS._matches(_FAKE_PATH), is_(False))

    def test__matches_should_match_false(self):
        """
        Unit test case for :py:method:`PathExists._matches`.
        """
        assert_that(self._NOT_EXISTS._matches(_REAL_FILE), is_(False))
        assert_that(self._NOT_EXISTS._matches(_REAL_DIR), is_(False))
        assert_that(self._NOT_EXISTS._matches(_FAKE_PATH), is_(True))

    def test_describe_to_should_match_true(self):
        """
        Unit test case for :py:method:`PathExists.describe_to`.
        """
        description = StringDescription()
        self._EXISTS.describe_to(description)
        actual = str(description)
        expected = "'A path that exists:'"
        assert_that(actual, is_(expected))

    def test_describe_to_should_match_false(self):
        """
        Unit test case for :py:method:`PathExists.describe_to`.
        """
        description = StringDescription()
        self._NOT_EXISTS.describe_to(description)
        actual = str(description)
        expected = "'A path that does not exist:'"
        assert_that(actual, is_(expected))


class TestIsFile(object):
    """
    Unit test for class :py:class:`IsFile`.
    """

    _IS_FILE = IsFile(True)
    _IS_NOT_FILE = IsFile(False)

    # Test cases

    def test__matches_should_match_true(self):
        """
        Unit test case for :py:method:`IsFile._matches`.
        """
        assert_that(self._IS_FILE._matches(_REAL_FILE), is_(True))
        assert_that(self._IS_FILE._matches(_REAL_DIR), is_(False))
        assert_that(self._IS_FILE._matches(_FAKE_PATH), is_(False))

    def test__matches_should_match_false(self):
        """
        Unit test case for :py:method:`IsFile._matches`.
        """
        assert_that(self._IS_NOT_FILE._matches(_REAL_FILE), is_(False))
        assert_that(self._IS_NOT_FILE._matches(_REAL_DIR), is_(True))
        assert_that(self._IS_NOT_FILE._matches(_FAKE_PATH), is_(True))

    def test_describe_to_should_match_true(self):
        """
        Unit test case for :py:method:`IsFile.describe_to`.
        """
        description = StringDescription()
        self._IS_FILE.describe_to(description)
        actual = str(description)
        expected = "'A path that represents an existing file:'"
        assert_that(actual, is_(expected))

    def test_describe_to_should_match_false(self):
        """
        Unit test case for :py:method:`IsFile.describe_to`.
        """
        description = StringDescription()
        self._IS_NOT_FILE.describe_to(description)
        actual = str(description)
        expected = "'A path that does not represent an existing file:'"
        assert_that(actual, is_(expected))


class TestIsDir(object):
    """
    Unit test for class :py:class:`IsDir`.
    """

    _IS_DIR = IsDir(True)
    _IS_NOT_DIR = IsDir(False)

    # Test cases

    def test__matches_should_match_true(self):
        """
        Unit test case for :py:method:`IsDir._matches`.
        """
        assert_that(self._IS_DIR._matches(_REAL_FILE), is_(False))
        assert_that(self._IS_DIR._matches(_REAL_DIR), is_(True))
        assert_that(self._IS_DIR._matches(_FAKE_PATH), is_(False))

    def test__matches_should_match_false(self):
        """
        Unit test case for :py:method:`IsDir._matches`.
        """
        assert_that(self._IS_NOT_DIR._matches(_REAL_FILE), is_(True))
        assert_that(self._IS_NOT_DIR._matches(_REAL_DIR), is_(False))
        assert_that(self._IS_NOT_DIR._matches(_FAKE_PATH), is_(True))

    def test_describe_to_should_match_true(self):
        """
        Unit test case for :py:method:`IsDir.describe_to`.
        """
        description = StringDescription()
        self._IS_DIR.describe_to(description)
        actual = str(description)
        expected = "'A path that represents an existing directory:'"
        assert_that(actual, is_(expected))

    def test_describe_to_should_match_false(self):
        """
        Unit test case for :py:method:`IsDir.describe_to`.
        """
        description = StringDescription()
        self._IS_NOT_DIR.describe_to(description)
        actual = str(description)
        expected = "'A path that does not represent an existing directory:'"
        assert_that(actual, is_(expected))


class TestFileMatcher(object):
    """
    Unit test for module-level functions of :py:mod:`file_matcher`.
    """

    # Test cases

    def test_exists(self):
        """
        Unit test case for :py:func:`file_matcher.exists`.
        """
        assert_that(_REAL_FILE, exists())
        assert_that(_REAL_DIR, exists())
        with raises(AssertionError):
            assert_that(_FAKE_PATH, exists())

    def test_not_exists(self):
        """
        Unit test case for :py:func:`file_matcher.not_exists`.
        """
        with raises(AssertionError):
            assert_that(_REAL_FILE, not_exists())
        with raises(AssertionError):
            assert_that(_REAL_DIR, not_exists())
        assert_that(_FAKE_PATH, not_exists())

    def test_is_file(self):
        """
        Unit test case for :py:func:`file_matcher.is_file`.
        """
        assert_that(_REAL_FILE, is_file())
        with raises(AssertionError):
            assert_that(_REAL_DIR, is_file())
        with raises(AssertionError):
            assert_that(_FAKE_PATH, is_file())

    def test_is_not_file(self):
        """
        Unit test case for :py:func:`file_matcher.is_not_file`.
        """
        with raises(AssertionError):
            assert_that(_REAL_FILE, is_not_file())
        assert_that(_REAL_DIR, is_not_file())
        assert_that(_FAKE_PATH, is_not_file())
