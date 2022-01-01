"""
some_package_name
~~~~~~~~~~~~~~~~

Main entry point commend line script for the some_package_name project.

    This sample application logs a message to console at all logging levels.

Command line syntax:

    python some_package_name.py <message>
"""

__author__ = 'some_author'
__copyright__ = \
    'Unpublished Copyright (c) 2000 some_author. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

import argparse
import logging
from logging import getLogger, basicConfig

if __name__ == '__main__':

    # Set up logging

    basicConfig(level=logging.DEBUG)

    # Set up basic command-line argument parsing

    parser = argparse.ArgumentParser()
    parser.add_argument('message')
    args = parser.parse_args()

    # Test logging

    getLogger(__file__).debug(f'Logged with DEBUG: {args.message}')
    getLogger(__file__).info(f'Logged with INFO: {args.message}')
    getLogger(__file__).warning(f'Logged with WARNING: {args.message}')
    getLogger(__file__).error(f'Logged with ERROR: {args.message}')
    getLogger(__file__).critical(f'Logged with CRITICAL: {args.message}')
