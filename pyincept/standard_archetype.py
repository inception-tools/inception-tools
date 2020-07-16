"""
standard_archetype
~~~~~~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`StandardArchetype` along with
supporting classes, functions, and attributes.
"""

__author__ = 'Andrew van Herick'

import os
from abc import ABCMeta
from enum import Enum, EnumMeta
from typing import Iterable

from jinja2 import Template

from pyincept.archetype_base import ArchetypeBase
from pyincept.archetype_parameters import ArchetypeParameters
from pyincept.file_builder import FileBuilder

_ARCHITYPE_DIR = os.path.abspath(
    os.path.join(
        __file__,
        os.pardir,
        'data',
        'archetypes',
        'pyincept-archetype-standard'
    )
)


class _ABCEnumMeta(ABCMeta, EnumMeta):
    # Enables Enums to inherit from abstract base classes
    pass


_INIT_FILE_NAME = '__init__.py'
_TEST_PACKAGE_FORMAT = 'test_{}'


class _ProjectRootRenderers(FileBuilder, Enum, metaclass=_ABCEnumMeta):
    # Enumerates the :py:`FileBuilder` instances used by
    # :py:attr:`StandardArchetype.PROJECT_ROOT`.

    INIT_PACKAGE = (
        '__init___package.py.jinja',
        lambda b: os.path.join(b.package_name, _INIT_FILE_NAME)
    )

    INIT_TESTS = (
        '__init___tests.py.jinja',
        lambda b: os.path.join('tests', _INIT_FILE_NAME)
    )

    INIT_TESTS_END_TO_END = (
        '__init___tests_end_to_end.py.jinja',
        lambda b: os.path.join('tests', 'end_to_end', _INIT_FILE_NAME)
    )

    INIT_TESTS_END_TO_END_PACKAGE = (
        '__init___tests_end_to_end_package.py.jinja',
        lambda b: os.path.join(
            'tests',
            'end_to_end',
            _TEST_PACKAGE_FORMAT.format(b.package_name),
            _INIT_FILE_NAME
        )
    )

    INIT_TESTS_INTEGRATION = (
        '__init___tests_integration.py.jinja',
        lambda b: os.path.join('tests', 'integration', _INIT_FILE_NAME)
    )

    INIT_TESTS_INTEGRATION_PACKAGE = (
        '__init___tests_integration_package.py.jinja',
        lambda b: os.path.join(
            'tests',
            'integration',
            _TEST_PACKAGE_FORMAT.format(b.package_name),
            _INIT_FILE_NAME
        )
    )

    INIT_TESTS_UNIT = (
        '__init___tests_unit.py.jinja',
        lambda b: os.path.join('tests', 'unit', _INIT_FILE_NAME)
    )

    INIT_TESTS_UNIT_PACKAGE = (
        '__init___tests_unit_package.py.jinja',
        lambda b: os.path.join(
            'tests',
            'unit',
            _TEST_PACKAGE_FORMAT.format(b.package_name),
            _INIT_FILE_NAME
        )
    )

    LICENSE = ('LICENSE.apache.jinja', lambda b: 'LICENSE')

    LOG_CFG = ('log.cfg.jinja', lambda b: 'log.cfg')

    MAIN = ('main.py.jinja', lambda b: os.path.join(b.package_name, 'main.py'))

    MAKEFILE = ('Makefile.jinja', lambda b: 'Makefile')

    PIPFILE = ('Pipfile.jinja', lambda b: 'Pipfile')

    README_RST = ('README.rst.jinja', lambda b: 'README.rst')

    SETUP_CFG = ('setup.cfg.jinja', lambda b: 'setup.cfg')

    SETUP_PY = ('setup.py.jinja', lambda b: 'setup.py')

    @classmethod
    def _get_template(cls, template_name) -> Template:
        template_path = os.path.join(_ARCHITYPE_DIR, template_name)
        with open(template_path) as f:
            content = f.read()
            return Template(content, keep_trailing_newline=True)

    def __init__(self, template_name, subpath_function) -> None:
        self._template = self._get_template(template_name)
        self._subpath = subpath_function

    def subpath(self, params: ArchetypeParameters) -> str:
        return self._subpath(params)

    def render(self, params):
        return self._template.render(**params.as_dict())


class StandardArchetype(ArchetypeBase, Enum, metaclass=_ABCEnumMeta):
    """
    Enumerates the standard :py:class:`Archetype` instances available
    across the system.
    """

    #: The :py:meth:`build` method of this :py:class:`Archetype` will create a
    # directory/file tree with the following structure:
    #:
    #: ::
    #:
    #:     root_dir/
    #:         my_package/
    #:             __init__.py
    #:             my_package.py
    #:         tests/
    #:             __init__.py
    #:             end-to-end/
    #:                 __init__.py
    #:                 test_my_package/
    #:                     __init__.py
    #:             integration/
    #:                 __init__.py
    #:                 test_my_package/
    #:                     __init__.py
    #:             unit/
    #:                 __init__.py
    #:                 test_my_package/
    #:                     __init__.py
    #:         LICENSE
    #:         Makefile
    #:         Pipfile
    #:         README.rst
    #:         setup.cfg
    #:         setup.py
    #:
    #: where 'root_dir' is the `root_dir argument and 'my_package' is the
    # `package_name` attribute of the params argument.
    PROJECT_ROOT = (_ProjectRootRenderers,)

    def __init__(self, resource_builders: Iterable[FileBuilder]) -> None:
        # Referencing ArchetypeBase directly for the sake of supporting Python
        # 3.5, which does not seem to handle call to super() in the context of
        # multiple inheritance as gracefully as the later versions do.
        ArchetypeBase.__init__(self, resource_builders)
