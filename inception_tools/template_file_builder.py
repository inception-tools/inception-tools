"""
template_file_builder
~~~~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`TemplateFileBuilder` along with
supporting classes, functions, and attributes.
"""

__author__ = "Andrew van Herick"
__copyright__ = "Unpublished Copyright (c) 2022 Andrew van Herick. All Rights Reserved."
__license__ = "Apache Software License 2.0"

import os

from jinja2 import Template

from inception_tools.archetype_parameters import ArchetypeParameters
from inception_tools.file_builder import FileBuilder


class TemplateFileBuilder(FileBuilder):
    """
    This class uses :py:class:jinja2.Template` instances to create both the subpath
    and content of a file.
    """

    PATH_SEP = "/"
    """
    The path separator to use to write ``subpath`` templates. This separator will be
    converted to the OS-specific path separator automatically by :py:meth:`subpath`.
    """

    @classmethod
    def from_strings(cls, subpath: str, prototype: str) -> FileBuilder:
        """
        Factory method that builds a new :py:class:`TemplateDirectoryBuilder`
        instance from :py:class:`jinja2.Template` source ``string``s, which will be
        used to create the return value of :py:meth:`subpath` and :py:meth:`render`
        from the ``params`` argument.
        :param subpath: the subpath template string
        :param prototype: the prototype template string
        :return: the new instance
        .. seealso:: :py:meth:`__init__`
        """
        s = Template(subpath)
        p = Template(prototype, keep_trailing_newline=True)
        return cls(s, p)

    def __init__(self, subpath: Template, prototype: Template) -> None:
        """
        Initializes a new :py:class:`TemplateFileBuilder` instance.
        :param subpath: the template used to produce the return value of
        :py:meth:`subpath`
        :param prototype: the template used to produce the return value of
        :py:meth:`subpath`
        .. seealso:: :py:attr:`PATH_SET`, :py:meth:`subpath`, :py:meth:`render`
        """
        super().__init__()
        self._subpath = subpath
        self._prototype = prototype

    def subpath(self, params: ArchetypeParameters) -> str:
        """
        Creates the subpath using the ``subpath`` :py:class:`jinja2.Template` used to
        initialize this instance, using the named :py:class:`ArchetypeParameters` to
        replace any template variables.  The path, once rendered, is split using
        :py:attr:`PATH_SEP` and rejoined using the OS-specific path separator.
        """
        subpath_raw = self._subpath.render(**params.as_dict())
        subpath_split = subpath_raw.split(self.PATH_SEP)
        return os.path.join(*subpath_split)

    def render(self, params: ArchetypeParameters) -> str:
        """
        Renders the file content using the ``subpath`` :py:class:`jinja2.Template`
        used to initialize this instance, using the named
        :py:class:`ArchetypeParameters` to replace any template variables.
        """
        return self._prototype.render(**params.as_dict())
