"""
    incept
    ~~~~~~~~~~~~~~~~~~~~~~~

    Main entry point commend line script.  Command line syntax:

        incept <project_root_dir>

    ~~~~~~~~~~~~~~~~~~~~~~~

    Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

import click
from pathvalidate.click import validate_filepath_arg

from pyincept.project_builder import ProjectBuilder


@click.command()
@click.argument('project_root', callback=validate_filepath_arg)
def main(project_root):
    return ProjectBuilder(project_root).build()
