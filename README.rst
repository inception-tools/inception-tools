===============
inception-tools
===============

.. image:: https://github.com/inception-tools/inception-tools/workflows/Release%20Build/badge.svg
  :target: https://github.com/inception-tools/inception-tools/actions?query=workflow%3A%22Release+Build%22

.. image:: https://github.com/inception-tools/inception-tools/workflows/Nightly%20Development%20Build/badge.svg
  :target: https://github.com/inception-tools/inception-tools/actions?query=workflow%3A%22Nightly+Development+Build%22

.. image:: https://github.com/inception-tools/inception-tools/workflows/Development%20Test%20Suite/badge.svg
  :target: https://github.com/inception-tools/inception-tools/actions?query=workflow%3A%22Development+Test+Suite%22

Under Construction
==================

Hello and welcome to the `inception-tools` project!

The goal of this project is to create, foster, and disseminate solid conventions for
Python project structure through the propagation and reuse of project archetypes,
developed and submitted by the community, which can be used as templates for
automatically setting up new Python projects.

This project is currently under construction. This documentation describes current
state of application functionality.  The application currently supports a set of
standard archetypes

- simple - a basic project shell
- cli - for creating command-line interface projects
- lib - for developing and publishing a Python libraries

Support for user-defined archetypes is coming. Please check back periodically to
see what's new.

If you would like to see updates or additions to the standard archetypes, the templates
are located in the `archetypes`_ directory and are made available to the CLI through
the `StandardArchetype`_ class. Please submit a PR for review using the instructions in
the `Bugs, Contribution, and Feedback`_  section, or reach out to the author's email
listed at the bottom of this document.

.. _`archetypes`: https://github.com/inception-tools/inception-tools/tree/develop/inception_tools/data/archetypes/
.. _`StandardArchetype`: https://github.com/inception-tools/inception-tools/blob/develop/inception_tools/standard_archetype.py

Documentation
=============

Create a new Python project, ready to go, with a single command!

Inception-tools is a command-line application designed to create new software
projects (in particular, Python-based projects) using a set of standardized project
archetypes.

The base ``inception-tools`` package provides:

- Simple command-line invocation for creating "stubbed-out" Python projects,
  parameterized through the command-line call.
- A set of standard archetypes for common Python project types:
    - simple
        - Creates a basic project shell.
    - cli
        - Creates a project shell geared toward developing and publishing a
          Python-based command-line application.
    - lib
        - Creates a project shell geared specifically toward developing and
          publishing a Python library
- Each standard archetype creates a shell project structure with files,
  directories, class and function stubs, completely set up and ready for
  publication to PyPI using a standardized set of Makefile targets.

Python Package Index:

https://pypi.org/project/inception-tools/

GitHub Repository:

https://github.com/inception-tools/inception-tools

Installation
============

Download and install the latest version of this application from the Python
package index (PyPI) as follows:

::

    pip install inception-tools

Note that ``inception-tools`` has dependencies on the following packages:

- ``click``
- ``jinja2``

These should be automatically installed by ``pip`` using the command-line
above.

Usage
=====

Once Inception Tools has been installed, you can create a new project shell
as follows\:

::

    it incept package_name [project_root]

This will create a new project (using the standard ``application``
archetype) under the directory ``project_root`` using additional parameters
stored in file ``inception-tools.cfg``\:

::

    <project_root>/
        docs/
        <package_name>/
            __init__.py
            cli.py
        scripts/
        tests/
            __init__.py
            end-to-end/
                __init__.py
            integration/
                __init__.py
            unit/
                __init__.py
        LICENSE
        Makefile
        Pipfile
        README.rst
        setup.cfg
        setup.py

``package_name`` (required)
    The package name that will used for your new project, e.g.
    ``inception_tools``. This will be used to create for the name of the
    package, for the name of a stub entry point files, and in the names of
    test modules. It will also be used as the relative path for the
    ``project_root`` argument in the event that it is omitted (see below).

``[project_root]`` (optional) default: package_name
    The path to the directory under which your project should be installed,
    e.g. ``inception-tools``.

    Example `installing to a directory my_package in the current working
    directory`::

        it incept my_package

    Example `installing to a directory called my_project in the user's home
    directory`::

        it incept my_package ~/my_project

The following options are also available:

``--author-name`` (optional)
    The name of the package author, e.g. 'Jane Doe'.  Defaults to '[author-name]'.

``--author-email`` (optional)
    The email address of the author, e.g. 'jane.doe@inception-tools.org'.

``--org-name`` (optional)
    The name of the organization sponsoring development for the project, e.g.
    'inception-tools'.

``--archetype`` (optional)
    Determines the archetype used to create the stub project. Defaults to 'cli'. Must be
    one of the following:

    - simple
        - Creates a basic project shell.
    - cli
        - Creates a project shell geared toward developing and publishing a
          Python-based command-line application.
    - lib
        - Creates a project shell geared specifically toward developing and
          publishing a Python library

License
=======

``inception-tools`` is released under the Apache Software License v2.0 - see the files
``LICENSE`` for further details.

Bugs, Contribution, and Feedback
================================

Contributions and feedback are welcome.  Contributions can be made by opening
a pull request at the ``inception-tools`` `repository`_ and tagging `@avanherick` for
review.  Please see the `Development` section of this document for code style
and branching guidelines.

.. _`repository`: https://github.com/inception-tools/inception-tools/

This project was created to fill what looked like a lack of standardized
conventions practices for structuring Python projects, and out of the desire
to avoid the need to manually create the same directory and file structures
over and over again.

If you come across this project and know of other project which accomplish
similar goals, or of documented standards around Python project structure,
we would welcome hearing about them.

Please submit feedback, bugs, feature requests, and code changes using GitHub
at:
http://github.com/inception-tools/inception-tools

Development
===========

Repository Management:
    Inception Tools manages its repository using the `GitFlow`_ model.

.. _`GitFlow`: https://nvie.com/posts/a-successful-git-branching-model/

Code style:
    Inception Tools code should adhere to the `PEP 8`_ guidelines with the exception
    of maximum line length, which instead uses `black`_'s default of 88.

.. _`PEP 8`: https://www.python.org/dev/peps/pep-0008/
.. _`black`: https://github.com/psf/black

Versioning:
    Inception Tools uses semantic versioning and adheres to the guidelines
    specified `here`_.

.. _`here`: https://semver.org/

CI/CD:
    - All builds are automated through GitHub actions.
    - Development builds are executed against the ``develop`` branch.
    - Beta builds are executed with each push to the ``master`` branch.
    - Release builds are triggered by the creation of a release through GitHub.

Changes
=======

**v0.1.0**

- Initial public version

:author: Andrew van Herick
:email: avanherick@gmail.com
:date: 2022-01-03
