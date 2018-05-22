
====================
A project structure
====================

This chapter explains a full Python project structure. What kind of directory
layout you can use and how make release a software to the world.

We will call our example project *factorial*.
::

    $ mkdir pymfactorial
    $ cd pymfactorial/

Primary code
=============

The name of the Python module will be *myfact*, so we will create the directory
next.

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

Now we have to write a *MANIFEST.in* file which will be used to find out which
all files will be part of the source tar ball of the project at the time of
using *sdist* command.

::

    include *.py
    include README.rst

If you want to exclude some file, you can use *exclude* statements in this file.

LICENSE file
=============

Always remember to add a proper license to your project. You can take help
from `this site <https://choosealicense.com/>`_ if you are new to software
licensing.

The following is the content of our project, which is licensed under **MIT**.

::

    MIT License

    Copyright (c) 2018 Kushal Das <kushaldas@gmail.com>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.


Installing python-setuptools package
====================================

You have to install *python3-setuptools* package in your system. For this we are
using a virtualenv (not showing the steps here). We will also install *wheel*
package.

::

    $ pip install setuptools wheel


setup.py
=========

Finally we have to write a *setup.py* which then can be used to create a source
tarball or installing the software.

::

    #!/usr/bin/env python3
    """Factorial project"""
    from setuptools import find_packages, setup

    with open("README.rst", "r") as fobj:
        long_description = fobj.read()

    setup(name = 'pymfactorial',
        version = '0.1',
        description = "pym Factorial module.",
        long_description = long_description,
        platforms = ["Linux"],
        author="Kushal Das",
        author_email="kushaldas@gmail.com",
        url="https://pymbook.readthedocs.io/en/latest/",
        license = "MIT",
        packages=find_packages()
    )

**name** is the name of the project, **version** is the release version. You can
easily understand **description** and **long_description**. *platforms* is a
list of the platforms this module can work on. **find_packages** is a special
function which can find all modules under your source directory.

.. note:: To learn more you can read the `packaging docs <https://packaging.python.org/en/latest/distributing.html>`_.


Usage of setup.py
==================

To create a source release and also a binary wheel for distribution, use the following
command.

::

    $ python3 setup.py sdist bdist_wheel
    running sdist
    running egg_info
    creating pymfactorial.egg-info
    writing top-level names to pymfactorial.egg-info/top_level.txt
    writing dependency_links to pymfactorial.egg-info/dependency_links.txt
    writing pymfactorial.egg-info/PKG-INFO
    writing manifest file 'pymfactorial.egg-info/SOURCES.txt'
    reading manifest file 'pymfactorial.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    writing manifest file 'pymfactorial.egg-info/SOURCES.txt'
    running check
    creating pymfactorial-0.1
    creating pymfactorial-0.1/myfact
    creating pymfactorial-0.1/pymfactorial.egg-info
    copying files to pymfactorial-0.1...
    copying MANIFEST.in -> pymfactorial-0.1
    copying README.rst -> pymfactorial-0.1
    copying setup.py -> pymfactorial-0.1
    copying myfact/__init__.py -> pymfactorial-0.1/myfact
    copying myfact/fact.py -> pymfactorial-0.1/myfact
    copying pymfactorial.egg-info/PKG-INFO -> pymfactorial-0.1/pymfactorial.egg-info
    copying pymfactorial.egg-info/SOURCES.txt -> pymfactorial-0.1/pymfactorial.egg-info
    copying pymfactorial.egg-info/dependency_links.txt -> pymfactorial-0.1/pymfactorial.egg-info
    copying pymfactorial.egg-info/top_level.txt -> pymfactorial-0.1/pymfactorial.egg-info
    Writing pymfactorial-0.1/setup.cfg
    creating dist
    Creating tar archive
    removing 'pymfactorial-0.1' (and everything under it)
    running bdist_wheel
    running build
    running build_py
    creating build
    creating build/lib
    creating build/lib/myfact
    copying myfact/fact.py -> build/lib/myfact
    copying myfact/__init__.py -> build/lib/myfact
    warning: build_py: byte-compiling is disabled, skipping.

    installing to build/bdist.linux-x86_64/wheel
    running install
    running install_lib
    creating build/bdist.linux-x86_64
    creating build/bdist.linux-x86_64/wheel
    creating build/bdist.linux-x86_64/wheel/myfact
    copying build/lib/myfact/fact.py -> build/bdist.linux-x86_64/wheel/myfact
    copying build/lib/myfact/__init__.py -> build/bdist.linux-x86_64/wheel/myfact
    warning: install_lib: byte-compiling is disabled, skipping.

    running install_egg_info
    Copying pymfactorial.egg-info to build/bdist.linux-x86_64/wheel/pymfactorial-0.1-py3.5.egg-info
    running install_scripts
    creating build/bdist.linux-x86_64/wheel/pymfactorial-0.1.dist-info/WHEEL
    creating '/home/kdas/code/pym/code/factorial/dist/pymfactorial-0.1-py3-none-any.whl' and adding '.' to it
    adding 'myfact/__init__.py'
    adding 'myfact/fact.py'
    adding 'pymfactorial-0.1.dist-info/top_level.txt'
    adding 'pymfactorial-0.1.dist-info/WHEEL'
    adding 'pymfactorial-0.1.dist-info/METADATA'
    adding 'pymfactorial-0.1.dist-info/RECORD'
    removing build/bdist.linux-x86_64/wheel

One can see the output files under *dist* directory.
::

    $ ls dist/
    pymfactorial-0.1-py3-none-any.whl  pymfactorial-0.1.tar.gz

.. warning:: Remember to use a virtualenv while trying to install the code :)


Python Package Index (PyPI)
============================

Do you remember the **pip** command we are using still now? Ever thought from
where those packages are coming from? The answer is `PyPI <http://pypi..org/>`_.
It is a repository of software for the Python programming language.

For our example, we will use the test server of PyPI which is `https://test.pypi.org/ <https://test.pypi.org/>`_

Creating account
-----------------

First register yourself in `this link
<https://test.pypi.org/account/register/>`_. You will receive
an email with a link, go to that link and confirm your registration.


.. note:: Remember to change the name of the project
          to something else in the `setup.py` to test following
          instructions.

Uploading your project
-----------------------

Now finally we can upload our project to the PyPI server using **twine** command.
Remember that this command needs to be invoked immediately after you build the
source/binary distribution files.

First, we will have to install **twine** using **pip** (we are using a virtualenv).

::

    $ pip install twine
    $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    Uploading distributions to https://test.pypi.org/legacy/
    Enter your username: kushaldas
    Enter your password: 
    Uploading pymfactorial-0.1-py3-none-any.whl
    100%|██████████████████████████████████████| 4.29k/4.29k [00:01<00:00, 3.77kB/s]
    Uploading pymfactorial-0.1.tar.gz
    100%|██████████████████████████████████████| 3.83k/3.83k [00:00<00:00, 7.57kB/s]

Now if you visit the `site <https://test.pypi.org/pypi/pymfactorial/>`_, you will
find your project is ready to be used by others.

Install from the test PyPI
===========================

You can use the following command to install from the test PyPI.

::

    $ pip install --index-url https://test.pypi.org/simple/ pymfactorial

More readings
==============

Please visit https://packaging.python.org to learn more about Python packaging.
There are many guides and tutorials available on that site.
