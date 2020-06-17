"""
    some_test_package_name.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    Main entry point commend line script for the some_test_package_name project.

    Command line syntax:

        some_test_package_name <message>

    ~~~~~~~~~~~~~~~~~~~~~~~

    Unpublished Copyright 2020 some_test_author. All Rights Reserved.
"""

__author__ = 'some_test_author'

from logging import getLogger
from logging.config import fileConfig

import click

fileConfig('log.cfg', disable_existing_loggers=False)


@click.command()
@click.argument('message')
def main(message):
    getLogger(__file__).debug('Logged with DEBUG: {}'.format(message))
    getLogger(__file__).info('Logged with INFO: {}'.format(message))
    getLogger(__file__).warning('Logged with WARNING: {}'.format(message))
    getLogger(__file__).error('Logged with ERROR: {}'.format(message))
    getLogger(__file__).critical('Logged with CRITICAL: {}'.format(message))
