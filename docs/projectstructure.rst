
====================
A project structure
====================

This chapter explains a full Python project structure. What kind of directory layout
you can use and how make release a software to the world.

We will call our example project *factorial*.
::

    $ mkdir factorial
    $ cd factorial/

Primary code
=============

The name of the Python module will be *myfact*, so we will create the directory next.
::

    $ mkdir myfact

The primary code will be in a file called *fact.py*
::

    "myfact module"

    def factorial(num):
        """
        Returns the factorial value of the given number.

        :arg num: Interger value of whose factorial we will calculate.

        :return: The value of the the factorial or -1 in case negative value passed.
        """
        if num >= 0:
            if num == 0:
                return 1
            return num * factorial(num -1)
        else:
            return -1

We also have a *__init__.py* file for the module.
::

    from fact import factorial
    __all__ = [factorial, ]

We also added a *README.rst* file. So, the directory structure looks like
::

    $ ls
    myfact  README.rst
    $ ls myfact/
    fact.py  __init__.py


MANIFEST.in
============

Now we have to write a *MANIFEST.in* file which will be used to find out which all
files will be part of the source tar ball of the project at the time of using *sdist* command.
::

    include *.py
    include README.rst

If you want to exclude some file, you can use *exclude* statements in this file.

Installing python-setuptools package
====================================

You have to install *python-setuptools* package in your system. For this we are using
a virtualenv (not showing the steps here)


    $ pip install setuptools


setup.py
=========

Finally we have to write a *setup.py* which then can be used to create a source tarball
or installing the software.
::

    #!/usr/bin/env python
    """Factorial project"""
    from setuptools import find_packages, setup

    setup(name = 'factorial',
        version = '0.1',
        description = "Factorial module.",
        long_description = "A test module for our book.",
        platforms = ["Linux"],
        author="Kushal Das",
        author_email="kushaldas@gmail.com",
        url="http://pymbook.readthedocs.org/en/latest/",
        license = "MIT",
        packages=find_packages()
        )
*name* is the name of the project, *version* is the release version. You can easily
understand *description* and *long_description*. *platforms* is a list of the platforms
this module can work on. *find_packages* is a special function which can find
all modules under your source directory.

.. note:: To learn more you can read the `packaging docs <https://packaging.python.org/en/latest/distributing.html>`_.


Usage of setup.py
==================

To create a source release one execute the following command.
::

    $ python setup.py sdist
    running sdist
    running egg_info
    creating factorial.egg-info
    writing factorial.egg-info/PKG-INFO
    writing top-level names to factorial.egg-info/top_level.txt
    writing dependency_links to factorial.egg-info/dependency_links.txt
    writing manifest file 'factorial.egg-info/SOURCES.txt'
    reading manifest file 'factorial.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    writing manifest file 'factorial.egg-info/SOURCES.txt'
    running check
    creating factorial-0.1
    creating factorial-0.1/factorial.egg-info
    creating factorial-0.1/myfact
    making hard links in factorial-0.1...
    hard linking MANIFEST.in -> factorial-0.1
    hard linking README.rst -> factorial-0.1
    hard linking setup.py -> factorial-0.1
    hard linking factorial.egg-info/PKG-INFO -> factorial-0.1/factorial.egg-info
    hard linking factorial.egg-info/SOURCES.txt -> factorial-0.1/factorial.egg-info
    hard linking factorial.egg-info/dependency_links.txt -> factorial-0.1/factorial.egg-info
    hard linking factorial.egg-info/top_level.txt -> factorial-0.1/factorial.egg-info
    hard linking myfact/__init__.py -> factorial-0.1/myfact
    hard linking myfact/fact.py -> factorial-0.1/myfact
    Writing factorial-0.1/setup.cfg
    creating dist
    Creating tar archive
    removing 'factorial-0.1' (and everything under it)

One can see the tarball under *dist* directory.
::

    $ ls dist/
    factorial-0.1.tar.gz

.. note:: Remember to use a virtualenv while trying to install the code :)

To install from the source use the following command.
::

    $ python setup.py install

.. note:: To learn more, read from `packaging.python.org <https://packaging.python.org/en/latest/distributing.html>`_.

Python Package Index (PyPI)
============================

Do you remember the *pip* command we are using still now? Ever thought from where those packages
are coming from? The answer is `PyPI <http://pypi.python.org/pypi>`_. It is a
repository of software for the Python programming language.

For our example, we will use the test server of PyPI which is `https://testpypi.python.org/pypi <https://testpypi.python.org/pypi>`_

Creating account
-----------------

First register yourself in `this link <https://testpypi.python.org/pypi?%3Aaction=register_form>`_. You will
receive an email with a link, go to that link and confirm your registration.

 .pypirc file
 -------------

 Your account details genrally stay inside a file called *.pypirc* under your home directory.
 The content of the file will look like
 ::

    [distutils]
    index-servers =
        pypi

    [pypi]
    repository: https://testpypi.python.org/pypi
    username: <username>
    password: <password>

Replace <username> and <password> with your newly created account details.

.. note:: Remember to change the name of the project to something else in the `setup.py`to test following instructions.

Registering your project
-------------------------

Next we will register our project to the PyPI service. This is done using the `register` command. We will
also use `-r` to point it to the test server.
::

    $ python setup.py register -r https://testpypi.python.org/pypi
    running register
    running egg_info
    writing factorial.egg-info/PKG-INFO
    writing top-level names to factorial.egg-info/top_level.txt
    writing dependency_links to factorial.egg-info/dependency_links.txt
    reading manifest file 'factorial.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    writing manifest file 'factorial.egg-info/SOURCES.txt'
    running check
    Registering factorial to https://testpypi.python.org/pypi
    Server response (200): OK

Uploading your project
-----------------------

Now finally we can upload our project to the PyPI server using `upload` command.
Remember that this command needs to be invoked immediately after you build the source/binary
distribution files.
::

    $ python setup.py sdist upload -r https://testpypi.python.org/pypi
    running sdist
    running egg_info
    writing factorial.egg-info/PKG-INFO
    writing top-level names to factorial.egg-info/top_level.txt
    writing dependency_links to factorial.egg-info/dependency_links.txt
    reading manifest file 'factorial.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    writing manifest file 'factorial.egg-info/SOURCES.txt'
    running check
    creating factorial-0.1
    creating factorial-0.1/factorial.egg-info
    creating factorial-0.1/myfact
    making hard links in factorial-0.1...
    hard linking MANIFEST.in -> factorial-0.1
    hard linking README.rst -> factorial-0.1
    hard linking setup.py -> factorial-0.1
    hard linking factorial.egg-info/PKG-INFO -> factorial-0.1/factorial.egg-info
    hard linking factorial.egg-info/SOURCES.txt -> factorial-0.1/factorial.egg-info
    hard linking factorial.egg-info/dependency_links.txt -> factorial-0.1/factorial.egg-info
    hard linking factorial.egg-info/top_level.txt -> factorial-0.1/factorial.egg-info
    hard linking myfact/__init__.py -> factorial-0.1/myfact
    hard linking myfact/fact.py -> factorial-0.1/myfact
    Writing factorial-0.1/setup.cfg
    Creating tar archive
    removing 'factorial-0.1' (and everything under it)
    running upload
    Submitting dist/factorial-0.1.tar.gz to https://testpypi.python.org/pypi
    Server response (200): OK

Now if you visit the `site <https://testpypi.python.org/pypi/factorial/>`_, you will find
your project is ready to be used by others.

