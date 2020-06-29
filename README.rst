========
pyincept
========

Incept a new Python project, ready to go, with a single command!

A simple Python application designed to incept new Python project by creating
a standardized project structure complete with shell directories and stub
files, with package name, to start the project off.

Features:

- Simple command-line invocation for creating shell Python projects,
  parameterized with project name, package names
- Shell project includes all standard project files including\:
    - setup.py (configured with package name and standard dependencies)
    - Directories for unit, integration, and end-to-end tests
    - Makefile with a smattering of useful targets.
- Sample project files, complete with a sample endpoint.

Python Package Index:

.. image:: https://github.com/avanherick/pyincept/workflows/Release%20Build/badge.svg
  :target: https://test.pypi.org/project/pyincept/

Nightly development build:

.. image:: https://github.com/avanherick/pyincept/workflows/Development%20Build/badge.svg
  :target: https://github.com/avanherick/pyincept/actions?query=workflow%3A%22Development+Build%22

Latest development code:

.. image:: https://github.com/avanherick/pyincept/workflows/Development%20test%20suite/badge.svg
  :target: https://github.com/avanherick/pyincept/tree/develop

Installation
============

Download and install the latest version of this application from the Python
package index (PyPI) as follows:

::

    pip install pyincept

Note that ``pyincept`` has dependencies on the following packages:

- ``click``
- ``jinja2``

These should be automatically installed by ``pip`` using the command-line
above.

Usage
=====

Once ``pyincept`` has been installed, you can create a new project shell as
follows:

::

    pyincept package_name author author email [project_root]

This will create a shell project with the following structure:

::

    <working-dir>/
        project_root/
            package_name/
                __init__.py
                package_name.py
            tests/
                __init__.py
                end-to-end/
                    __init__.py
                    test_package_name/
                        __init__.py
                integration/
                    __init__.py
                    test_package_name/
                        __init__.py
                unit/
                    __init__.py
                    test_package_name/
                        __init__.py
            LICENSE
            Makefile
            Pipfile
            README.rst
            setup.cfg
            setup.py

``package_name`` (required)
    The package name that will used for your new project, e.g. ``pyincept``.
    This will be used to create for the name of the package, for the name of a
    stub entry point files, and in the names of test modules.    It will also
    be used as the relative path for the ``project_root`` argument in the
    event that it is omitted (see below).

``author`` (required)
    The name of the package author, e.g. 'Jane Doe'.  This will be used to fill
    in the ``__author__`` attribute in stub files, and in copyright
    attributions in header file comments.

``author_email`` (required)
    The email address of the author, e.g. 'jane.doe@pyincept.org'.  This will
    be used to fill in various locations in where a contact email is specified
    in the new project files, e.g. the `author_email` property in
    ``setup.cfg``.

``[project_root]`` (optional) default: package_name
    The path to the directory under which your project should be installed,
    e.g. ``pyincept``.

    Example `installing to a directory my_package in the current working
    directory`::

        pyincept my_package my_author my_author_email

    Example `installing to a directory called my_project in the user's home
    directory`::

        pyincept my_package my_author my_author_email ~/my_project

Development
===========

Repository Management:
    ``pyincept`` manages its repository using the `GitFlow`_ model.

.. _`GitFlow`: https://nvie.com/posts/a-successful-git-branching-model/

Code style:
    ``pyincept`` code should adhere to the `PEP 8`_ guidelines.

.. _`PEP 8`: https://www.python.org/dev/peps/pep-0008/

Versioning:
    ``pyincept`` versioning uses semantic versioning and adheres to the
    guidelines specified `here`_.

.. _`here`: https://semver.org/

CI/CD:
    - All builds are automated through GitHub actions.
    - Development builds are executed against the ``develop`` branch.
    - Beta builds are executed with each push to the ``master`` branch.
    - Release builds are triggered by the creation of a release through GitHub.

License
=======

``pyincept`` is released under the Apache Software License - see the files
``LICENSE`` for further details.

Bugs, Contribution, and Feedback
================================

Contributions and feedback are welcome.

This project was created to fill what looked like a lack of standardized
conventions practices for structuring Python projects, and out of the desire
to avoid the need to manually create the same directory and file structures
over and over again.

If you come across this project and know of other project which accomplish
similar goals, or of standards around Python project structure, would
welcome hearing about them.

Please submit bugs, feature requests, and code changes using GitHub at:
http://github.com/avanherick/pyincept

Changes
=======

**v0.1.0**

- Initial public version

:author: Andrew van Herick
:email: avanherick@gmail.com
:date: 2020-06-29
