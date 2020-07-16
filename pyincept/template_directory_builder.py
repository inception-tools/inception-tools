"""
template_directory_builder
~~~~~~~~~~~~~~~~~~~~~~~~~~

Houses the declaration of :py:class:`TemplateDirectoryBuilder` along with
supporting classes, functions, and attributes.
"""

__author__ = 'Andrew van Herick'
__copyright__ = \
    'Unpublished Copyright (c) 2020 Andrew van Herick. All Rights Reserved.'
__license__ = 'Apache Software License 2.0'

from jinja2 import Template

from pyincept.archetype_parameters import ArchetypeParameters
from pyincept.directory_builder import DirectoryBuilder


class TemplateDirectoryBuilder(DirectoryBuilder):
    """
    An implementation of :py:class:`pyincept.DirectoryBuilder` which uses a
    :py:class:`jinja2.Template` to create the subpath for the directory to
    be built.
    """

    def __init__(self, template: Template) -> None:
        """
        Initializes a new :py:class:`TemplateDirectoryBuilder` instance.
        :param template: a :py:class:`jinja2.Template` to be used with the
        ``params`` argument of :py:meth:`subpath`.
        """
        self._template = template

    def subpath(self, params: ArchetypeParameters) -> str:
        """
        Renders the template held by using ``params`` dictionary
        representation.
        """
        return self._template.render(params.as_dict())
