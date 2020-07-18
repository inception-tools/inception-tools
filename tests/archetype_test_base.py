"""
archetype_test_base
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`ArchetypeTestBase` along with
supporting classes, functions, and attributes.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

import os
import shutil
from abc import ABC, abstractmethod
from collections import namedtuple
from typing import Iterable

from hamcrest import assert_that, is_

from pyincept.archetype import Archetype
from pyincept.constants import UNIMPLEMENTED_ABSTRACT_METHOD_ERROR
from tests.file_matcher import exists, is_dir, is_file, not_exists
from tests.pyincept_test_base import PyinceptTestBase

_TestOutput = namedtuple(
    '_TestOutput',
    ('subpath', 'expected_output_path')
)
"""
TODO: Add docstring comments
"""


class ArchetypeTestBase(PyinceptTestBase, ABC):
    """
    TODO: Add docstring comments
    """

    ##############################
    # Instance methods

    @property
    @abstractmethod
    def _archetype(self) -> Archetype:
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR

    @property
    @abstractmethod
    def _expected_output(self) -> Iterable[_TestOutput]:
        """
        Returns a list of :py:class:`
        :return:
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR

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

    def test_output_files(self):
        """
        Unit test case for :py:method:`TemplateArchetype.output_files`.
        """
        actual = self._archetype.output_files(self._ROOT_DIR, self._PARAMS)
        expected = tuple(
            os.path.join(self._ROOT_DIR, p.subpath)
            for p in self._expected_output
        )
        assert_that(sorted(actual), is_(sorted(expected)))

    def test_build(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        self._archetype.build(self._ROOT_DIR, self._PARAMS)
        for test_output in self._expected_output:
            actual_path = os.path.join(self._ROOT_DIR, test_output.subpath)
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
