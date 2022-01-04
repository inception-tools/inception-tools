"""
main
~~~~~

Main entry point commend line script.  See :py:func:`cli` for details of how to
invoke this script.
"""

import logging
import pathlib
from datetime import datetime
from logging.config import fileConfig

import click

from inception_tools.archetype_parameters import ArchetypeParameters
from inception_tools.exception import LoggingConfigError
from inception_tools.standard_archetype import StandardArchetype

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"


def _logger() -> logging.Logger:
    return logging.getLogger(__file__)


def _incept(
    package_name: str,
    project_root: str,
    author: str,
    author_email: str,
    archetype_name: str,
) -> None:
    archetype = StandardArchetype.from_string(archetype_name)
    params = ArchetypeParameters(
        package_name=package_name,
        author=author,
        author_email=author_email,
        date=datetime.now(),
    )
    root_dir = project_root or package_name
    archetype.build(root_dir=root_dir, params=params)


@click.command()
@click.argument("package_name")
@click.argument(
    "project_root",
    type=click.Path(file_okay=False),
    default=None,
    required=False,
)
@click.option(
    "--author-name",
    type=str,
    default="[insert-author-name]",
    help="The name of the package author. Depending on the archetype selected, this "
    "may be used in copyright notices, setup.py package metadata, and for "
    "__author__ assignments in Python stub files.",
)
@click.option(
    "--author-email",
    type=str,
    default="[insert-author-email]",
    help="The email of the package author. Depending on the archetype selected, "
    "this bay be used in setup.py package metadata and in the auto-generated "
    "boilerplate text of README.rst file.",
)
@click.option(
    "--archetype",
    default=StandardArchetype.CLI.canonical_name,
    type=click.Choice(StandardArchetype.canonical_names(), case_sensitive=False),
)
def incept(
    package_name: str,
    project_root: str,
    author_name: str,
    author_email: str,
    archetype: str,
) -> None:
    """
    Builds a new project structure with the given package name.  Command line
    syntax:

        it incept <package-name>

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

    where many of the files are parameterized with the package name, author name,
    author email, etc.

    PACKAGE_NAME: the name of the package to be created.  This should be the package
    name, as you would expect it to appear in code references ( e.g. 'my_package' and
    not 'my-package'

    PROJECT_ROOT (optional - defaults to PACKAGE_NAME): the directory under which the
    new project should be created. If the directory does not already exist, it
    will be created automatically. Any preexisting files and/or subdirectories matching
    those created by this command will be overwritten.
    """
    try:
        _incept(package_name, project_root, author_name, author_email, archetype)
    except Exception:
        msg = (
            f"Unexpected exception: "
            f"package_name={package_name!r}, project_root={project_root!r}, "
            f"author_name={author_name!r}, author_email={author_email!r}"
        )
        _logger().exception(msg)
        raise


@click.group()
@click.option(
    "-l", "--logging-config", default=None, type=click.Path(exists=True, dir_okay=False)
)
def cli(logging_config: str) -> None:
    """
    Main command-line application for the inception_tools package.  This application
    can be used to access various commands listed below.  For example to incept a new
    project called 'my_package', use the following command:

        it incept my_package

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
