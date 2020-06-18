"""
    incept
    ~~~~~~~~~~~~~~~~~~~~~~~

    Main entry point commend line script.  Command line syntax:

        incept <project_root_dir>

    ~~~~~~~~~~~~~~~~~~~~~~~

    Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

from datetime import datetime

import click

from pyincept.project_builder import ProjectBuilder


@click.command()
@click.argument('package_name')
@click.argument('author')
@click.argument('author_email')
def main(package_name, author, author_email):
    now = datetime.now()
    builder = ProjectBuilder(
        package_name=package_name,
        author=author,
        author_email=author_email,
        project_root=package_name,
        year=now.year
    )
    builder.build()
