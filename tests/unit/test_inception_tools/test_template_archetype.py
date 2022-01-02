"""
test_template_archetype
~~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`template_archetype` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os

from hamcrest import assert_that, is_

from inception_tools.template_archetype import TemplateArchetype
from tests.archetype_output_test_base import (
    _OutputFile,
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

    _ARCHETYPE_NAME = "inceptiontools-archetype-test_template_archetype-1.0"

    _TEST_RESOURCE_PATH = os.path.abspath(
        os.path.join(__file__, os.pardir, "data", "test_template_archetype")
    )

    _OUTPUT_DIRS = (_OutputFile("tests", None),)

    _OUTPUT_FILES = (
        _OutputFile(
            "some_package_name.py",
            os.path.join(_TEST_RESOURCE_PATH, "some_package_name.py"),
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

    def test_file_paths(self):
        """
        Unit test case for :py:method:`TemplateArchetype.file_paths`.
        """
        actual = self._archetype.file_paths(self._ROOT_DIR, self._PARAMS)
        expected = tuple(
            os.path.join(self._ROOT_DIR, p.subpath) for p in self._OUTPUT_FILES
        )
        assert_that(sorted(actual), is_(sorted(expected)))

    def test_dir_paths(self):
        """
        Unit test case for :py:method:`TemplateArchetype.dir_paths`.
        """
        actual = self._archetype.dir_paths(self._ROOT_DIR, self._PARAMS)
        expected = tuple(
            os.path.join(self._ROOT_DIR, p.subpath) for p in self._OUTPUT_DIRS
        )
        assert_that(sorted(actual), is_(sorted(expected)))

    def test_build(self):
        """
        Unit test case for :py:method:`TemplateArchetype.build`.
        """
        self._archetype.build(self._ROOT_DIR, self._PARAMS)
        self._validate_archetype_files(self._ROOT_DIR, self._OUTPUT_FILES)
        self._validate_archetype_dirs(self._ROOT_DIR, self._OUTPUT_DIRS)
