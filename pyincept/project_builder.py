"""
    project_builder
    ~~~~~~~~~~~~~~~~~~~~~~~

    Houses the declaration of
    :py:class:`pyincept.project_builder.ProjectBuilder` along with
    supporting classes, functions, and attributes.

    ~~~~~~~~~~~~~~~~~~~~~~~

    Unpublished Copyright 2020 Andrew van Herick. All Rights Reserved.
"""

__author__ = 'Andrew van Herick'

import errno
import os
from enum import Enum

from jinja2 import Template
from pathvalidate import validate_filepath

_TEMPLATE_PATH = os.path.abspath(
    os.path.join(__file__, os.pardir, '_resources', 'templates')
)


class _ProjectFile(Enum):
    ENTRY_POINT = (
        'entry_point.py.jinja',
        lambda package_name: os.path.join(
            package_name,
            '{}.py'.format(package_name)
        ),
    )
    INIT_PACKAGE = (
        '__init___package.py.jinja',
        lambda package_name: os.path.join(package_name, '__init__.py'),
    )
    INIT_TESTS = (
        '__init___tests.py.jinja',
        lambda package_name: os.path.join('tests', '__init__.py'),
    )
    LICENSE = ('LICENSE.apache.jinja', lambda package_name: 'LICENSE',)
    LOG_CFG = ('log.cfg.jinja', lambda package_name: 'log.cfg',)
    MAKEFILE = ('Makefile.jinja', lambda package_name: 'Makefile',)
    PIPFILE = ('Pipfile.jinja', lambda package_name: 'Pipfile',)
    SETUP_CFG = ('setup.cfg.jinja', lambda package_name: 'setup.cfg',)
    SETUP_PY = ('setup.py.jinja', lambda package_name: 'setup.py',)

    def __init__(self, template_name, file_path_function):
        self._template_name = template_name
        self._file_path = file_path_function

    def _get_template(self) -> Template:
        template_path = os.path.join(_TEMPLATE_PATH, self._template_name)
        with open(template_path) as f:
            content = f.read()
            return Template(content, keep_trailing_newline=True)

    def _save_content(
            self,
            content: str,
            package_name: str,
            author: str,
            author_email: str,
            project_root: str
    ) -> None:
        file_path = os.path.join(project_root, self._file_path(package_name))

        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

        with open(file_path, 'w') as f:
            f.write(content)

    def render_and_save(
            self,
            package_name,
            author,
            author_email,
            project_root
    ):
        t = self._get_template()
        content = t.render(
            package_name=package_name,
            author=author,
            author_email=author_email,
            project_root=project_root
        )
        self._save_content(
            content,
            package_name=package_name,
            author=author,
            author_email=author_email,
            project_root=project_root
        )


class ProjectBuilder(object):
    """
    This class is responsible for building the file directory structure for a
    newly incepted project.  It encapsulates and makes testable the bulk of
    behavior provided by the :py:func:`pyincept.incept.main` function.
    """

    def __init__(
            self,
            package_name: str,
            author: str,
            author_email: str,
            project_root: str,
    ) -> None:
        super().__init__()
        validate_filepath(project_root)
        self._package_name = package_name
        self._author = author
        self._author_email = author_email
        self._project_root = project_root

    @property
    def project_root(self) -> str:
        """
        :return: the path, as supplied to the class initializer, of the
        project root directory
        """
        return os.path.abspath(self._project_root)

    @property
    def project_root_abs(self) -> str:
        """
        :return: the absolute path of the project root directory
        :rtype: str
        """
        return os.path.abspath(self._project_root)

    def build(self) -> None:
        for f in _ProjectFile:
            f.render_and_save(
                package_name=self._package_name,
                author=self._author,
                author_email=self._author_email,
                project_root=self._project_root
            )
