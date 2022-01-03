"""
template_directory_builder
~~~~~~~~~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`TemplateDirectoryBuilder` along with supporting
classes, functions, and attributes.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os

from jinja2 import Template

from inception_tools.archetype_parameters import ArchetypeParameters
from inception_tools.directory_builder import DirectoryBuilder


class TemplateDirectoryBuilder(DirectoryBuilder):
    """
    An implementation of :py:class:`inception_tools.DirectoryBuilder` which uses a
    :py:class:`jinja2.Template` to create the subpath for the directory to be built.
    """

    PATH_SEP = "/"
    """
    The path separator to use to write ``subpath`` templates. This separator will be
    converted to the OS-specific path separator automatically by :py:meth:`subpath`.
    """

    @classmethod
    def from_string(cls, subpath: str) -> DirectoryBuilder:
        """
        Factory method that builds a new :py:class:`TemplateDirectoryBuilder`
        instance from a :py:class:`jinja2.Template` source ``string``, which will be
        used to create the return value of :py:meth:`subpath` from the ``params``
        argument.

        :param subpath: the subpath template string
        :return: the new instance
        .. seealso:: :py:meth:`__init__`
        """
        t = Template(subpath)
        return cls(t)

    def __init__(self, template: Template) -> None:
        """
        Initializes a new :py:class:`TemplateDirectoryBuilder` instance. :param
        template: a :py:class:`jinja2.Template` to be used with the ``params``
        argument of :py:meth:`subpath`.
        """
        self._template = template

    def subpath(self, params: ArchetypeParameters) -> str:
        """
        Renders the template held by using ``params`` dictionary representation.
        """
        subpath_raw = self._template.render(**params.as_dict())
        subpath_split = subpath_raw.split(self.PATH_SEP)
        return os.path.join(*subpath_split)
