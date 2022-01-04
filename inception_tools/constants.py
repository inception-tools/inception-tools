"""
constants
~~~~~~~~~

Houses the declaration of constants used throughout the :py:mod:`inception_tools`
package. """

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

UNIMPLEMENTED_ABSTRACT_METHOD_ERROR = NotImplementedError(
    "Method to be implemented by subclasses."
)
"""
The error raised by unimplemented abstract methods declared in :py:class:`ABC`
subclasses.
"""
