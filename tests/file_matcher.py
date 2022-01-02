"""
matcher
~~~~~~~

Houses the declaration of :py:class:`Matchers` along with supporting
classes, functions, and attributes.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os

from hamcrest.core.base_matcher import BaseMatcher


class PathExists(BaseMatcher):
    """
    A :py:mod:`hamcrest.core.Matcher` that matches if a path exists.
    """

    def __init__(self, should_exist: bool) -> None:
        super().__init__()
        self._should_exist = should_exist

    def _matches(self, item):
        return self._should_exist == os.path.exists(item)

    def describe_to(self, description):
        msg = (
            "A path that exists:"
            if self._should_exist
            else "A path that does not exist:"
        )
        description.append_description_of(msg)


def exists():
    return PathExists(True)


def not_exists():
    return PathExists(False)


class IsFile(BaseMatcher):
    """
    A :py:mod:`hamcrest.core.Matcher` that matches if path represents a file.
    """

    def __init__(self, should_exist: bool) -> None:
        super().__init__()
        self._should_exist = should_exist

    def _matches(self, item):
        return self._should_exist == os.path.isfile(item)

    def describe_to(self, description):
        msg = (
            "A path that represents an existing file:"
            if self._should_exist
            else "A path that does not represent an existing file:"
        )
        description.append_description_of(msg)


def is_file():
    return IsFile(True)


def is_not_file():
    return IsFile(False)


class IsDir(BaseMatcher):
    """
    A :py:mod:`hamcrest.core.Matcher` that matches if path represents a
    directory.
    """

    def __init__(self, should_exist: bool) -> None:
        super().__init__()
        self._should_exist = should_exist

    def _matches(self, item):
        return self._should_exist == os.path.isdir(item)

    def describe_to(self, description):
        msg = (
            "A path that represents an existing directory:"
            if self._should_exist
            else "A path that does not represent an existing directory:"
        )
        description.append_description_of(msg)


def is_dir():
    return IsDir(True)


def is_not_dir():
    return IsDir(False)
