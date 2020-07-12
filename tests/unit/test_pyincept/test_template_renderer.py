"""
test_template_renderer
~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`template_renderer` module.
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
from pyincept.template_renderer import TemplateRenderer


class TestTemplateRenderer(object):
    """
    Unit test for :py:class:`TemplateRenderer`.
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
        '{{package_name}}/'
        '{{author}}/'
        '{{author_email}}/'
        '{{date.year}}/'
    )

    _PROTOTYPE = Template(
        'package_name={{package_name}},\n'
        'author={{author}},\n'
        'author_email={{author_email}},\n'
        'year={{date.year}},\n',
        keep_trailing_newline=True
    )

    _RENDERER = TemplateRenderer(_SUBPATH, _PROTOTYPE)

    ##############################
    # Instance methods

    # Test cases

    def test_subpath(self):
        """
        Unit test case for :py:method:`TemplateRenderer.subpath`.
        """
        actual = self._RENDERER.subpath(self._PARAMS)
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
        Unit test case for :py:method:`TemplateRenderer.render`.
        """
        actual = self._RENDERER.render(self._PARAMS)
        expected = \
            'package_name=some_package_name,\n' \
            'author=some_author,\n' \
            'author_email=some_author_email,\n' \
            'year=2000,\n'
        assert_that(actual, is_(expected))
