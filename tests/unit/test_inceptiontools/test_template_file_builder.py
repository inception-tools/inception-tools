"""
test_template_file_builder
~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`template_file_builder` module.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

import os

from hamcrest import assert_that, is_
from jinja2 import Template

from inceptiontools.template_file_builder import TemplateFileBuilder
from tests.archetype_output_test_base import ArchetypeOutputTestBase


class TestTemplateFileBuilder(object):
    """
    Unit test for :py:class:`TemplateFileBuilder`.
    """

    ##############################
    # Class attributes

    _PARAMS = ArchetypeOutputTestBase._PARAMS

    _SUBPATH_SOURCE = \
        '{{package_name}}/{{author}}/{{author_email}}/{{date.year}}/'
    _SUBPATH = Template(_SUBPATH_SOURCE)

    _PROTOTYPE_SOURCE = \
        'package_name={{package_name}},\n' \
        'author={{author}},\n' \
        'author_email={{author_email}},\n' \
        'year={{date.year}},\n'
    _PROTOTYPE = Template(_PROTOTYPE_SOURCE, keep_trailing_newline=True)

    _BUILDER = TemplateFileBuilder(_SUBPATH, _PROTOTYPE)

    ##############################
    # Instance methods

    # Test cases

    def test_from_strings(self):
        """
        Unit test case for
        :py:method:`TemplateFileBuilder.from_strings`.
        """
        actual = TemplateFileBuilder.from_strings(
            self._SUBPATH_SOURCE,
            self._PROTOTYPE_SOURCE
        )
        expected = self._BUILDER
        assert_that(
            actual.subpath(self._PARAMS),
            is_(expected.subpath(self._PARAMS))
        )
        assert_that(
            actual.render(self._PARAMS),
            is_(expected.render(self._PARAMS))
        )

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
            ''
        )
        assert_that(actual, is_(expected))

    def test_render(self):
        """
        Unit test case for :py:method:`TemplateFileBuilder.render`.
        """
        actual = self._BUILDER.render(self._PARAMS)
        expected = \
            'package_name=some_package_name,\n' \
            'author=some_author,\n' \
            'author_email=some_author_email,\n' \
            'year=2000,\n'
        assert_that(actual, is_(expected))
