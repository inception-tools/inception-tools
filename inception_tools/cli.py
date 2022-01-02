"""
main
~~~~~

Main entry point commend line script.  See :py:func:`cli` for details of how to
invoke this script. """

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import logging
import pathlib
from datetime import datetime
from logging.config import fileConfig

import click

from inception_tools.archetype_parameters import ArchetypeParameters
from inception_tools.exception import LoggingConfigError
from inception_tools.standard_archetype import StandardArchetype


def _logger():
    return logging.getLogger(__file__)


def _incept(package_name, author, author_email, archetype_name):
    params = ArchetypeParameters(
        package_name=package_name,
        author=author,
        author_email=author_email,
        date=datetime.now(),
    )
    archetype = StandardArchetype.from_string(archetype_name)
    archetype.build(root_dir=package_name, params=params)


@click.command()
@click.argument("package_name")
@click.argument("author")
@click.argument("author_email")
@click.option(
    "-a",
    "--archetype",
    default=StandardArchetype.CLI.canonical_name,
    type=click.Choice(StandardArchetype.canonical_names(), case_sensitive=False)
)
def incept(package_name, author, author_email, archetype):
    """
    Builds a new project structure with the given package name.  Command line
    syntax:

        it incept <package-name> <author-name> <author-email>

    Invoking the command line above will _result in the creation of a directory with
    the following structure:

    \b
        <working-dir>/
            my_package/
                my_package/
                    __init__.py
                    my_package.py
                tests/
                    __init__.py
                    end-to-end/
                        __init__.py
                        test_my_package/
                            __init__.py
                    integration/
                        __init__.py
                        test_my_package/
                            __init__.py
                    unit/
                        __init__.py
                        test_my_package/
                            __init__.py
                LICENSE
                Makefile
                Pipfile
                README.rst
                setup.cfg
                setup.py

    where many of the files are parameterize with the package name, author name,
    author email, etc.

    PACKAGE_NAME: the name of the package to be incepted.  This should be the package
    name, as you would expect it to appear in code references ( e.g. 'my_package' and
    not 'my-package'

    AUTHOR: the name of the package author.  This string is used in copyright
    notices, setup.py package metadata, and for __author__ assignments in Python stub
    files.

    AUTHOR_EMAIL: the email of the package author.  This is used in setup.py package
    metadata and in the auto-generated boiler-plate text of README.rst file.
    """
    try:
        _incept(package_name, author, author_email, archetype)
    except Exception:
        msg = (
            "Unexpected exception: "
            f"package_name={package_name}, author={author}, author_email={author_email}"
        )
        _logger().exception(msg)
        raise


@click.group()
@click.option(
    "-l", "--logging-config", default=None, type=click.Path(exists=True, dir_okay=False)
)
def cli(logging_config):
    """
    Main command-line application for the inception_tools package.  This application
    can be used to access various commands listed below.  For example to incept a new
    project called 'my_package', use the following command:

        it incept <package-name> <author-name> <author-email>

    For additional help using any command, use the help for the command as follows

        it <command> --help
    """
    logging_config = logging_config or "log.cfg"
    if pathlib.Path(logging_config).is_file():
        try:
            fileConfig(logging_config, disable_existing_loggers=False)
        except Exception:
            raise LoggingConfigError(
                f"Could not parse the logging config file: {logging_config!r}"
            )
    else:
        logging.basicConfig(level=logging.INFO)
        _logger().warning(
            f"Logging config file not found: {logging_config!r}."
            "All logs will be directed to a basic console logger."
        )
    _logger().debug("Successfully set up logging.")


cli.add_command(incept)

if __name__ == "__main__":
    cli()
