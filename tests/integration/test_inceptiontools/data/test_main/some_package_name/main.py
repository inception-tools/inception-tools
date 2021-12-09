"""
main
~~~~

Main entry point commend line script for the some_package_name project.

Command line syntax:

    some_package_name <message>
"""

__author__ = "some_author"
__copyright__ = "Unpublished Copyright (c) 2000 some_author. All Rights Reserved."
__license__ = "Apache Software License 2.0"

from logging import getLogger
from logging.config import fileConfig

import click


@click.command()
@click.argument("message")
def log_test(message):
    fileConfig("log.cfg", disable_existing_loggers=False)
    getLogger(__file__).debug("Logged with DEBUG: {}".format(message))
    getLogger(__file__).info("Logged with INFO: {}".format(message))
    getLogger(__file__).warning("Logged with WARNING: {}".format(message))
    getLogger(__file__).error("Logged with ERROR: {}".format(message))
    getLogger(__file__).critical("Logged with CRITICAL: {}".format(message))


@click.group()
def cli():
    # Nothing to do.  This function provides a shell for grouping commands for
    # the main command-line entry point.
    pass


cli.add_command(log_test)
