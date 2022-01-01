"""
cli
~~~~

Main entry point commend line script for the some_package_name project.

Command line syntax:

    some_package_name <message>
"""

__author__ = 'some_author'
__copyright__ = \
    'Unpublished Copyright (c) 2000 some_author. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

from logging import getLogger
from logging.config import fileConfig

import click


@click.command()
@click.argument('message')
def log_test(message):
    fileConfig('log.cfg', disable_existing_loggers=False)
    getLogger(__file__).debug(f'Logged with DEBUG: {message}')
    getLogger(__file__).info(f'Logged with INFO: {message}')
    getLogger(__file__).warning(f'Logged with WARNING: {message}')
    getLogger(__file__).error(f'Logged with ERROR: {message}')
    getLogger(__file__).critical(f'Logged with CRITICAL: {message}')


@click.group()
def cli():
    # Nothing to do.  This function provides a shell for grouping commands for
    # the main command-line entry point.
    pass


cli.add_command(log_test)