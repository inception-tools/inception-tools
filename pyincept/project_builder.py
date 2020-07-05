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

from pyincept.architype_parameters import ArchitypeParameters
from pyincept.architype import BaseArchitype
from pyincept.standard_file_renderer import StandardFileRenderer


class ProjectBuilder(object):
    """
    This class is responsible for building the file directory structure for a
    newly incepted project.  It encapsulates and makes testable the bulk of
    behavior provided by the :py:func:`pyincept.incept.main` function.
    """

    def __init__(
            self,
            root_dir: str,
            params: ArchitypeParameters
    ) -> None:
        """
        Class initializer method.

        :param root_dir: the root directory under which all files will be
        saved.

        :param params: the parameters that will be used to create parameterized
        content of generated files
        """
        super().__init__()
        self._architype = BaseArchitype(tuple(StandardFileRenderer))
        self._params = params
        self._project_root = root_dir

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
        """
        This method is responsible for building the project file and directory
        structure used to 'incept' a new project.  It uses data passed to the
        class initializer to create a directory/file tree with the following
        structure:

        ::

            root_dir/
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

        where each of the files above has content customized according to the
        parameters held by this instance.
        """
        for f in StandardFileRenderer:
            f.render_and_save(self._project_root, self._params)
