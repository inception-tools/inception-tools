"""
test_template_archetype
~~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`template_archetype` module.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

import os

from hamcrest import assert_that, is_

from pyincept.template_archetype import TemplateArchetype
from tests.archetype_output_test_base import (
    _ArchetypeTestOutput,
    ArchetypeOutputTestBase,
)

import os

from hamcrest import assert_that, is_

from pyincept.template_archetype import TemplateArchetype
from tests.archetype_output_test_base import (
    _ArchetypeTestOutput,
    ArchetypeOutputTestBase,
)


class TestTemplateArchetype(ArchetypeOutputTestBase):
    """
    Unit test cases for :py:class:`TemplateArchetype`.
    """

    ##############################
    # Class attributes

    # See superclass declaration to understand the use of this attribute.
    _OVERWRITE_EXPECTED_FILE = False

    _ARCHETYPE_NAME = 'pyincept-archetype-unit_test_template_archetype-1.0'

    _TEST_RESOURCE_PATH = os.path.abspath(
        os.path.join(
            __file__,
            os.pardir,
            'data',
            'test_template_archetype'
        )
    )

    _EXPECTED_OUTPUT = (
        _ArchetypeTestOutput('tests', None),
        _ArchetypeTestOutput(
            'some_package_name.py',
            os.path.join(_TEST_RESOURCE_PATH, 'some_package_name.py')
        ),
    )

    ##############################
    # Class / static methods

    def setup(self):
        """
        Called before each method in this class with a name of the form
        test_*().
        """
        super(TestTemplateArchetype, self).setup()
        dir_path = os.path.join(self._TEST_RESOURCE_PATH, self._ARCHETYPE_NAME)
        self._archetype = TemplateArchetype(dir_path)

    ##############################
    # Instance methods

    # Test cases

    def test_output_files(self):
        """
        Unit test case for :py:method:`TemplateArchetype.output_files`.
        """
        actual = self._archetype.output_files(self._ROOT_DIR, self._PARAMS)
        expected = tuple(
            os.path.join(self._ROOT_DIR, p.subpath)
            for p in self._EXPECTED_OUTPUT
        )
        assert_that(sorted(actual), is_(sorted(expected)))

    def test_build(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        self._archetype.build(self._ROOT_DIR, self._PARAMS)
        self._validate_archetype_output(self._ROOT_DIR, self._EXPECTED_OUTPUT)
