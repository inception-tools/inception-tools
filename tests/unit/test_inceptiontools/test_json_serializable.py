"""
test_json_serializable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unit test cases for the :py:mod:`json_serializable` module.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from contextlib import closing
from io import StringIO

from hamcrest import assert_that, is_

from inceptiontools.json_serializable import JSON_OBJ_TYPE, JsonSerializable


class _MockJsonSerializable(JsonSerializable):
    def __init__(self, json_obj) -> None:
        super().__init__()
        self.json_obj = json_obj

    @classmethod
    def from_json(cls, json_obj: JSON_OBJ_TYPE) -> JsonSerializable:
        return cls(json_obj)

    def to_json(self) -> JSON_OBJ_TYPE:
        return self.json_obj


class TestJsonSerializable(object):
    """
    Unit test for :py:class:`JsonSerializable`.
    """

    ##############################
    # Class attributes

    _JSON_STR = '{"foo": "bar", "baz": "qux"}'
    _SERIALIZABLE = _MockJsonSerializable({"foo": "bar", "baz": "qux"})

    ##############################
    # Instance methods

    # Test cases

    def test_from_text_io(self):
        """
        Unit test case for :py:method:`JsonSerializable.from_text_io`.
        """
        with closing(StringIO(self._JSON_STR)) as fp:
            actual = _MockJsonSerializable.from_text_io(fp)

        expected = self._SERIALIZABLE

        assert_that(actual.json_obj, is_(expected.json_obj))

    def test_to_text_io(self):
        """
        Unit test case for :py:method:`JsonSerializable.to_text_io`.
        """
        with closing(StringIO()) as fp:
            self._SERIALIZABLE.to_text_io(fp)
            actual = fp.getvalue()

        expected = self._JSON_STR

        assert_that(actual, is_(expected))
