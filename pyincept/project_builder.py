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

import datetime
import errno
import os
from enum import Enum

from jinja2 import Template

_TEMPLATE_PATH = os.path.abspath(
    os.path.join(__file__, os.pardir, '_resources', 'templates')
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
            date: datetime.date,
    ) -> None:
        super().__init__()
        self._package_name = package_name
        self._author = author
        self._author_email = author_email
        self._project_root = project_root
        self._date = date

    @property
    def package_name(self) -> str:
        """
        :return: the value of `package_name` given to the class initializer
        """
        return self._package_name

    @property
    def author(self) -> str:
        """
        :return: the value of `author` given to the class initializer
        """
        return self._author

    @property
    def author_email(self) -> str:
        """
        :return: the value of `author_email` given to the class initializer
        """
        return self._author_email

    @property
    def date(self) -> datetime.date:
        """
        :return: the value of `date` given to the class initializer
        """
        return self._date

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
            f.render_and_save(self)


class _ProjectFile(Enum):
    ENTRY_POINT = (
        'entry_point.py.jinja',
        lambda b: os.path.join(b.package_name, '{}.py'.format(b.package_name))
    )

    INIT_PACKAGE = (
        '__init___package.py.jinja',
        lambda b: os.path.join(b.package_name, '__init__.py')
    )

    INIT_TESTS = (
        '__init___tests.py.jinja',
        lambda b: os.path.join('tests', '__init__.py')
    )

    INIT_TESTS_END_TO_END = (
        '__init___tests_end_to_end.py.jinja',
        lambda b: os.path.join('tests', 'end_to_end', '__init__.py')
    )

    INIT_TESTS_END_TO_END_PACKAGE = (
        '__init___tests_end_to_end_package.py.jinja',
        lambda b: os.path.join(
            'tests',
            'end_to_end',
            'test_{}'.format(b.package_name),
            '__init__.py'
        )
    )

    INIT_TESTS_INTEGRATION = (
        '__init___tests_integration.py.jinja',
        lambda b: os.path.join('tests', 'integration', '__init__.py')
    )

    INIT_TESTS_INTEGRATION_PACKAGE = (
        '__init___tests_integration_package.py.jinja',
        lambda b: os.path.join(
            'tests',
            'integration',
            'test_{}'.format(b.package_name),
            '__init__.py'
        )
    )

    INIT_TESTS_UNIT = (
        '__init___tests_unit.py.jinja',
        lambda b: os.path.join('tests', 'unit', '__init__.py')
    )

    INIT_TESTS_UNIT_PACKAGE = (
        '__init___tests_unit_package.py.jinja',
        lambda b: os.path.join(
            'tests',
            'unit',
            'test_{}'.format(b.package_name),
            '__init__.py'
        )
    )

    LICENSE = ('LICENSE.apache.jinja', lambda b: 'LICENSE')

    LOG_CFG = ('log.cfg.jinja', lambda b: 'log.cfg')

    MAKEFILE = ('Makefile.jinja', lambda b: 'Makefile')

    PIPFILE = ('Pipfile.jinja', lambda b: 'Pipfile')

    README_RST = ('README.rst.jinja', lambda b: 'README.rst')

    SETUP_CFG = ('setup.cfg.jinja', lambda b: 'setup.cfg')

    SETUP_PY = ('setup.py.jinja', lambda b: 'setup.py')

    def __init__(self, template_name, file_path_function) -> None:
        self._template_name = template_name
        self._file_path = file_path_function

    def _get_template(self) -> Template:
        template_path = os.path.join(_TEMPLATE_PATH, self._template_name)
        with open(template_path) as f:
            content = f.read()
            return Template(content, keep_trailing_newline=True)

    def _save_content(self, content: str, builder: ProjectBuilder) -> None:
        path_ = os.path.join(builder.project_root, self._file_path(builder))

        try:
            os.makedirs(os.path.dirname(path_))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

        with open(path_, 'w') as f:
            f.write(content)

    def render_and_save(self, builder: ProjectBuilder) -> None:
        t = self._get_template()
        content = t.render(
            package_name=builder.package_name,
            author=builder.author,
            author_email=builder.author_email,
            project_root=builder.project_root,
            date=builder.date,
        )
        self._save_content(content, builder)
