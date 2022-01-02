"""
test_template_directory_builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`template_directory_builder` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os

from hamcrest import assert_that, is_
from jinja2 import Template

from inception_tools.template_directory_builder import TemplateDirectoryBuilder
from tests.archetype_output_test_base import ArchetypeOutputTestBase


class TestTemplateDirectoryBuilder(object):
    """
    Unit test cases for :py:class:`TemplateDirectoryBuilder`.
    """

    ##############################
    # Class attributes

    _PARAMS = ArchetypeOutputTestBase._PARAMS

    _SUBPATH_SOURCE = "{{package_name}}/{{author}}/{{author_email}}/{{date.year}}/"
    _SUBPATH = Template(_SUBPATH_SOURCE)

    _BUILDER = TemplateDirectoryBuilder(_SUBPATH)

    ##############################
    # Instance methods

    # Test cases

    def test_from_string(self):
        """
        Unit test case for
        :py:method:`TemplateDirectoryBuilder.from_string`.
        """
        actual = TemplateDirectoryBuilder.from_string(self._SUBPATH_SOURCE)
        expected = self._BUILDER
        assert_that(actual.subpath(self._PARAMS), is_(expected.subpath(self._PARAMS)))

    def test_subpath(self):
        """
        Unit test case for :py:method:`TemplateFileBuilder.subpath`.
        """
        actual = self._BUILDER.subpath(self._PARAMS)
        expected = os.path.join(
            self._PARAMS.package_name,
            self._PARAMS.author,
            self._PARAMS.author_email,
            str(self._PARAMS.date.year),
            "",
        )
        assert_that(actual, is_(expected))
