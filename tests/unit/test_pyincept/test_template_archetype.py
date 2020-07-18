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
from typing import Tuple

from pyincept.archetype import Archetype
from pyincept.template_archetype import TemplateArchetype
from tests.archetype_test_base import _TestOutput, ArchetypeTestBase


class TestTemplateArchetype(ArchetypeTestBase):
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

    ##############################
    # Class / static methods

    @classmethod
    def _get_resource_path(cls, *subpath):
        pass

    ##############################
    # Instance methods

    @property
    def _archetype(self) -> Archetype:
        dir_path = os.path.join(self._TEST_RESOURCE_PATH, self._ARCHETYPE_NAME)
        return TemplateArchetype(dir_path)

    @property
    def _expected_output(self) -> Tuple:
        return (
            _TestOutput('tests', None),
            _TestOutput(
                'some_package_name.py',
                os.path.join(self._TEST_RESOURCE_PATH, 'some_package_name.py')
            ),
        )
