pyincept
========

A simple Python application designed to incept new Python project by creating
a standardized project structure complete with shell directories and stub
files, with package name, to start the project off.

This project was created to fill what looked like a lack of standardized
conventions practices for structuring Python projects, and out of the desire
to avoid the need to manually create the same directory and file structures
over and over again.

If you come across this project and know of other project which accomplish
similar goals, or of standards around Python project structure, would
welcome hearing about them.  Shoot me an email at the address below.

Features:

- Simple command-line invocation for creating shell Python projects,
  parameterized with project name, package names
- Shell project includes a all standard project files including:
    - setup.py (configured with package name and standard dependencies)
    - Directories for unit, integration, and end-to-end tests
    - Makefile with a smattering of useful targets.
- Sample project files, complete with a sample 'endpoint' file.

Contributions and feedback are welcome using Github at:
http://github.com/avanaherick/pyincept

Note that `pytest` requires installation of the following packages:

- click
- pathvalidate
- jinja2

Installation
============

#. `pip install pyincept`
#. Invoke `pyincept` as follows

::

    `pyincept my_package 'Jane Doe Author' jane.doe@some-email.org`

See 'Usage' below for additional information.

Configuration
=============

There are currently no further configuration steps necessary.  Future
versions may enable the addition of more parameters.

Documentation
=============

Since this is such a simple project, this README file is currently the only
formal documentation.  If use of this project is not clear, or you believe
additional more formal documentation would be beneficial, please send an
email to the address below.

Usage
=====

Once `pyincept` has been installed, you can create a new project shell as
follows:

::

    `pyincept my_package 'Jane Doe Author' jane.doe@some-email.org`

This will create a shell project with the following structure:

::

    <working-dir>/
        my_package/
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

where many of the files are parameterize with the package name, author name,
author email, etc.

Bugs & Contributions
====================

Please submit bugs, feature requests, and code changes using GitHub at:
http://github.com/avanaherick/pyincept

:author: Andrew van Herick
:email: avanherick@gmail.com
:date: 2020-06-25
