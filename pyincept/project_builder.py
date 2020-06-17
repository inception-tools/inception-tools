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

import os
from enum import Enum

from jinja2 import Template
from pathvalidate import validate_filepath

_TEMPLATE_PATH = os.path.abspath(
    os.path.join(__file__, os.pardir, '_resources', 'templates')
)


class _Templates(Enum):
    LICENSE = 'LICENSE.apache.jinja'

    def get(self) -> Template:
        template_path = os.path.join(_TEMPLATE_PATH, self.value)
        with open(template_path) as f:
            content = f.read()
            return Template(content)

    def render(self, *args, **kwargs) -> str:
        return self.get().render(*args, **kwargs)


class _Files(Enum):
    LICENSE = 'LICENSE'

    def put(self, content: str, root_dir: str) -> None:
        file_path = os.path.join(root_dir, self.value)
        with open(file_path, 'w') as f:
            f.write(content)


class ProjectBuilder(object):
    """
    This class is responsible for building the file directory structure for a
    newly incepted project.  It encapsulates and makes testable the bulk of
    behavior provided by the :py:func:`pyincept.incept.main` function.
    """

    def __init__(self, project_root: str) -> None:
        super().__init__()
        validate_filepath(project_root)
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
        self._build_root_dir()
        self._build_package_dir()
        # self._build_license_file()
        # self._build_setup_files()
        # self._build_pip_files()
        # self._build_test_dir()

    def _build_root_dir(self) -> None:
        os.mkdir(self._project_root)

    def _build_package_dir(self) -> None:
        content = _Templates.LICENSE.render()
        _Files.LICENSE.put(content, self._project_root)

    # def _build_license_file(self) -> None:
    #     pass
    #
    # def _build_setup_files(self) -> None:
    #     pass
    #
    # def _build_pip_files(self) -> None:
    #     pass
    #
    # def _build_test_dir(self) -> None:
    #     pass
