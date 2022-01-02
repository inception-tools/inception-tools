"""
json_serializable
~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`JsonSerializable` along with supporting classes,
functions, and attributes. """

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import json
from abc import ABC, abstractmethod
from io import TextIOBase
from typing import Union

from inception_tools.constants import UNIMPLEMENTED_ABSTRACT_METHOD_ERROR
from inception_tools.serializable import Serializable, SerializationError

JSON_OBJ_TYPE = Union[dict, list, str, int, float, bool]
"""
The type definition for the ``fp`` argument in
:py:meth:`JsonSerializable.from_json` and
:py:meth:`JsonSerializable.to_json`.
"""


class JsonSerializationError(SerializationError):
    """
    A common exception raised by subclasses of :py:class:`JsonSerializable`.
    """


class JsonSerializable(Serializable, ABC):
    """
    Provides an interface by which classes can make themselves
    :py:class:`Serializable` by providing a way to marshal and unmarshal themselves
    from and to a JSON-like Python object representation.  The JSON-like Python
    object representation can be anything accepted by the :py:func:`json.dump` or
    produced by :py:func:`json.load`, i.e., a composition of objects of the following
    types:

    - ``dict``
    - ``list``
    - ``str``
    - ``bool``
    - ``int``
    - ``float``
    - ``None``
    """

    ##############################
    # Static / class methods

    @classmethod
    def from_text_io(cls, fp: TextIOBase):
        """
        Deserializes a JSON-formatted text-based input stream by first converting it
        to a JSON-like Python object using the :py:mod:`json` package and delegating
        responsibility for unmarshalling the JSON representation to
        :py:meth:`from_json`.
        """
        json_obj = json.load(fp)
        return cls.from_json(json_obj)

    @classmethod
    @abstractmethod
    def from_json(cls, json_obj: JSON_OBJ_TYPE):
        """
        Unmarshals a new ``cls`` instance from JSON-like Python object.
        :param json_obj: the JSON-like Python object
        :return: the new ``cls`` instance
        :raises SerializationError: if a problem occurs during execution of this method
        .. seealso:: modules :py:class:`JsonSerializable`
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR

    ##############################
    # Static / class methods

    def to_text_io(self, fp: TextIOBase):
        """
        Serializes this instance to a JSON-formatted text-based output stream by
        first converting it to a JSON-like Python object using the :py:mod:`json`
        package and delegating responsibility for serializing the JSON representation
        to the :py:mod:`json` package.
        """
        json_obj = self.to_json()
        return json.dump(json_obj, fp)

    def to_json(self) -> JSON_OBJ_TYPE:
        """
        Marshals a new ``cls`` instance to JSON-like Python object.
        :return: the JSON-like Python object
        :raises SerializationError: if a problem occurs during execution of this method
        .. seealso:: modules :py:class:`JsonSerializable`
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR
