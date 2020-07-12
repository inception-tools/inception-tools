from __future__ import annotations

"""
serializable
~~~~~~~~~~~~

Houses the declaration of :py:class:`Serializable` along with
supporting classes, functions, and attributes.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

from typing import Union

from abc import ABC, abstractmethod
from contextlib import closing
from io import StringIO, TextIOBase

TEXT_IO_TYPE = Union[TextIOBase, StringIO]


class Serializable(ABC):
    """
    Defines the common interface by which objects are serialized and
    deserialized within the :py:mod:`pyincept` package.
    """

    ##############################
    # Static / class methods

    @classmethod
    @abstractmethod
    def from_text_io(cls, file_obj: TEXT_IO_TYPE) -> Serializable:
        """
        Deserializes a new ``cls`` instance from a text-based input stream.
        :param file_obj: the file-like object
        :return: a new instance of type ``cls``
        """
        raise NotImplementedError('Method to be implemented by subclasses')

    @classmethod
    def from_string(cls, s):
        """
        Deserializes a new ``cls`` instance from a ``str``.
        :param s: the ``str``
        :return: a new instance of type ``cls``
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
        """
        raise NotImplementedError('Method to be implemented by subclasses')

    def to_string(self) -> str:
        """
        Serializes this instance to a ``str``.
        :return: the ``str``
        """
        with closing(StringIO()) as f:
            self.to_text_io(f)
            return f.getvalue()
