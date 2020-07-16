"""
    test_archetype_parameters
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Unit test cases for the :py:mod:`archetype_parameters` module.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'


import datetime

from hamcrest import assert_that, is_

from pyincept.archetype_parameters import ArchetypeParameters


class TestArchetypeParameters(object):
    """
    Unit test for class :py:class:`ArchetypeParameters`.
    """

    _PACKAGE_NAME = 'some_package'
    _AUTHOR = 'some_author'
    _AUTHOR_EMAIL = 'some_author'
    _DATE = datetime.date(2000, 1, 1)

    _PARAMS = ArchetypeParameters(
        _PACKAGE_NAME,
        _AUTHOR,
        _AUTHOR_EMAIL,
        _DATE
    )

    # Test cases

    def test_package_name(self):
        """
        Unit test case for :py:method:`ArchetypeParameters.package_name`.
        """
        actual = self._PACKAGE_NAME
        expected = self._PARAMS.package_name
        assert_that(actual, is_(expected))

    def test_author(self):
        """
        Unit test case for :py:method:`ArchetypeParameters.author`.
        """
        actual = self._AUTHOR
        expected = self._PARAMS.author
        assert_that(actual, is_(expected))

    def test_author_email(self):
        """
        Unit test case for :py:method:`ArchetypeParameters.author_email`.
        """
        actual = self._AUTHOR_EMAIL
        expected = self._PARAMS.author_email
        assert_that(actual, is_(expected))

    def test_date(self):
        """
        Unit test case for :py:method:`ArchetypeParameters.date`.
        """
        actual = self._DATE
        expected = self._PARAMS.date
        assert_that(actual, is_(expected))
