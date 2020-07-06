"""
    pyincept
    ~~~~~~~~~~~~~~~~~~~~~~~

    Main entry point commend line script.  See :py:func:`main` for details of
    how to invoke this script.

    ~~~~~~~~~~~~~~~~~~~~~~~

    Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

import logging
from datetime import datetime
from logging.config import fileConfig

import click

from pyincept.architype_parameters import ArchitypeParameters
from pyincept.standard_architype import StandardArchitype

fileConfig('log.cfg', disable_existing_loggers=False)


def _logger():
    return logging.getLogger(__file__)


def _main(package_name, author, author_email):
    params = ArchitypeParameters(
        package_name=package_name,
        author=author,
        author_email=author_email,
        date=datetime.now()
    )
    architype = StandardArchitype.PROJECT_ROOT
    architype.build(root_dir=package_name, params=params)


@click.command()
@click.argument('package_name')
@click.argument('author')
@click.argument('author_email')
def main(package_name, author, author_email):
    """
     Main entry point commend line script.  Command line syntax:

        pyincept my_package <author-name> <author-email>

    Invoking the command line above will _result in the creation of a
    directory with the following structure:

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

    where many of the files are parameterize with the package name, author
    name, author email, etc.

    PACKAGE_NAME: the name of the package to be incepted.  This should be
    the package name, as you would expect it to appear in code references (
    e.g. 'my_package' and not 'my-package'

    AUTHOR: the name of the package author.  This string is used in
    copyright notices, setup.py package metadata, and for __author__
    assignments in Python stub files.

    AUTHOR_EMAIL: the email of the package author.  This is used in setup.py
    package metadata and in the auto-generated boiler-plate text of
    README.rst file.
    """
    try:
        _main(package_name, author, author_email)
    except Exception:
        m = 'Unexpected exception: package_name={}, author={}, author_email={}'
        msg = m.format(package_name, author, author_email)
        _logger().exception(msg)
        raise
