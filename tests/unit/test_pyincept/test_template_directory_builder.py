"""
test_template_directory_builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`template_directory_builder` module.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

import datetime
import os

from hamcrest import assert_that, is_
from jinja2 import Template

from pyincept.archetype_parameters import ArchetypeParameters
from pyincept.template_directory_builder import TemplateDirectoryBuilder


class TestTemplateDirectoryBuilder(object):
    """
    Unit test cases for :py:class:`TemplateDirectoryBuilder`.
    """

    ##############################
    # Class attributes

    _PARAMS = ArchetypeParameters(
        'some_package_name',
        'some_author',
        'some_author_email',
        datetime.date(2000, 1, 1)
    )

    _SUBPATH = Template(
        '{{package_name}}/{{author}}/{{author_email}}/{{date.year}}/'
    )

    _BUILDER = TemplateDirectoryBuilder(_SUBPATH)

    ##############################
    # Instance methods

    # Test cases

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
