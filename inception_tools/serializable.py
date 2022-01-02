"""
serializable
~~~~~~~~~~~~

Houses the declaration of :py:class:`Serializable` along with supporting classes,
functions, and attributes. """

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from abc import ABC, abstractmethod
from contextlib import closing
from io import StringIO, TextIOBase
from typing import Union

from inception_tools.constants import UNIMPLEMENTED_ABSTRACT_METHOD_ERROR

TEXT_IO_TYPE = Union[TextIOBase, StringIO]


class SerializationError(Exception):
    """
    A common exception type for subclasses of :py:class:`Serializable` may raise to
    indicate an error.
    """


class Serializable(ABC):
    """
    Defines the common interface by which objects are serialized and deserialized
    within the :py:mod:`inception_tools` package.
    """

    ##############################
    # Static / class methods

    @classmethod
    @abstractmethod
    def from_text_io(cls, file_obj: TEXT_IO_TYPE):
        """
        Deserializes a new ``cls`` instance from a text-based input stream.
        :param file_obj: the file-like object
        :return: a new instance of type ``cls``
        :raises SerializationError: if a problem occurs during execution of this method
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR

    @classmethod
    def from_string(cls, s):
        """
        Deserializes a new ``cls`` instance from a ``str``.
        :param s: the ``str``
        :return: a new instance of type ``cls``
        :raises SerializationError: if a problem occurs during execution of this method
        """
        with closing(StringIO(s)) as f:
            return cls.from_text_io(f)

    ##############################
    # Instance methods

    @abstractmethod
    def to_text_io(self, file_obj: TEXT_IO_TYPE):
        """
        Serializes this instance to a text-based output stream.
        :param file_obj: the input stream
        :raises SerializationError: if a problem occurs during execution of this method
        """
        raise UNIMPLEMENTED_ABSTRACT_METHOD_ERROR

    def to_string(self) -> str:
        """
        Serializes this instance to a ``str``.
        :return: the ``str``
        :raises SerializationError: if a problem occurs during execution of this method
        """
        with closing(StringIO()) as f:
            self.to_text_io(f)
            return f.getvalue()
