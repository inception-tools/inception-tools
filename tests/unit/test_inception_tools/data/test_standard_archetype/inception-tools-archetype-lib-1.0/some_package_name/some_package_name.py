"""
some_package_name
~~~~

Houses the declarations of classes and functions supporting the
:py:mod:`some_package_name` package.
"""

__author__ = 'some_author'
__copyright__ = 'Unpublished Copyright (c) 2000 some_author. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

import os
import sys


class MessagePrinter(object):
    """
    A simple example class that prints a message to different output streams.
    """

    def __init__(self, message) -> None:
        """
        Initializes a new :py:class:`HelloWorld` instance.
        """
        super().__init__()
        self._message = message

    def to_file(self, file):
        """
        Prints the message held by this instance to a file-like object.
        """
        file.write(self._message)

    def to_stdout(self):
        """
        Prints the message held by this instance to `stdout`.
        """
        self.to_file(sys.stdout)

    def to_stderr(self):
        """
        Prints the message held by this instance to `stderr`.
        """
        self.to_file(sys.stderr)


if __name__ == '__main__':
    message_printer = MessagePrinter('Hello world!' + os.linesep)
    message_printer.to_stdout()
    message_printer.to_stderr()
