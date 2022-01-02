"""
exception
~~~~~~~~~

Houses the custom:py:class:`Exception` classes used by the system.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"


class LoggingConfigError(Exception):
    """
    An exception used to signal an error with the logging configuration.
    """
