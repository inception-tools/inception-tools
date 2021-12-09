"""
test_serializable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`serializable` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from io import TextIOBase

from hamcrest import assert_that, is_

from inceptiontools.serializable import Serializable


class _MockSerializable(Serializable):
    def __init__(self, s: str) -> None:
        super().__init__()
        self.s = s

    @classmethod
    def from_text_io(cls, file_obj: TextIOBase) -> Serializable:
        content = file_obj.read()
        return cls(str(content))

    def to_text_io(self, file_obj: TextIOBase):
        file_obj.write(self.s)


class TestSerializable(object):
    """
    Unit test for :py:class:`Serializable`.
    """

    ##############################
    # Class attributes

    _SERIALIZABLE = _MockSerializable("some test content")

    ##############################
    # Instance methods

    # Test cases

    def test_dumps(self):
        """
        Unit test case for :py:method:`Serializable.to_string`.
        """
        actual = self._SERIALIZABLE.to_string()
        expected = self._SERIALIZABLE.s
        assert_that(actual, is_(expected))

    def test_loads(self):
        """
        Unit test case for :py:method:`Serializable.from_string`.
        """
        actual = self._SERIALIZABLE.from_string(self._SERIALIZABLE.s)
        expected = self._SERIALIZABLE
        assert_that(actual.s, is_(expected.s))
