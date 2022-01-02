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

Hello and welcome to the Inception Tools project!

This project is currently under construction.  Please be patient and check
back periodically to see progress. In the meantime, you can see where the
project is headed by checking out the documentation (also in progress) below.

The goal of this project is to create, foster, and disseminate solid
conventions for Python project structure through the propagation and reuse
of project archetypes, developed and submitted by the community, which can
be used as templates for automatically setting up new Python projects.

Documentation
=============

Incept a new Python project, ready to go, with a single command!

Inception Tools is a command-line application application designed to incept
new software projects (in particular, Python-based projects) using a set of
standardized project archetypes.  It also provides for users to create new
archetype and even install them using standardized packaging tools.

The base ``inception_tools`` package provides:

- Simple command-line invocation for creating shell Python projects,
  parameterized through a configuration file.
- A set of standard archetypes for common Python project types:
    - application
        - Creates a project shell geared toward developing and publishing a
          Python-based command-line application.
    - library
        - Creates a project shell geared specifically toward developing and
          publishing a Python library
    - archetype
        - Creates a project shell geared specifically toward developing and
          publishing a new ``inception-tools`` archetype library.
- Each standard archetype creates a shell project structure with files,
  directories, class and function stubs, completely set up and ready to
  publication to PyPI using a standardized set of Makefile targets.
- An API which makes it easy to create, store, package and publish archetypes
  to suite your own needs.  You can either keep your own archetypes local or
  publish them for community use.

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

If you'd like to use the set of extended archetypes, you can also download and
install the ``inception-tools-archetypes`` package:

::

    pip install inception-tools-archetypes

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
            main.py
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

        it my_package

    Example `installing to a directory called my_project in the user's home
    directory`::

        it my_package ~/my_project

The following options are also available:

``--author_name`` (optional)
    The name of the package author, e.g. 'Jane Doe'.

``--author_email`` (optional)
    The email address of the author, e.g. 'jane.doe@inception-tools.org'.

``--org_name`` (optional)
    The name of the organization sponsoring development for the project, e.g.
    'inception-tools'.

License
=======

``inception-tools`` is released under the Apache Software License - see the files
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
    Inception Tools code should adhere to the `PEP 8`_ guidelines.

.. _`PEP 8`: https://www.python.org/dev/peps/pep-0008/

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
:date: 2020-06-29
