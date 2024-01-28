
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

The name of the Python module will be *pymfactorial*, so we will create the directory
next.

::

    $ mkdir -p pymfactorial/pymfactorial
    $ cd pymfactorial/

The primary code will be in a file called *fact.py*
::

    import sys

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


    def cli():
        "The command line entry point"
        number = int(sys.argv[1])
        print(f"Factorial is {factorial(number)}")


We also have a *__init__.py* file for the module.

::

    "pymfactorial module and command line tool"

    __version__ = "0.1.0"

    from fact import factorial
    __all__ = [factorial, cli]

We also added a *README.md* file. So, the directory structure looks like

::

    $ ls
    pymfactorial  README.md
    $ ls pymfactorial/
    fact.py  __init__.py


LICENSE file
=============

Always remember to add a proper license to your project. You can take help
from `this site <https://choosealicense.com/>`_ if you are new to software
licensing.

The following is the content of our project, which is licensed under **MIT**.

::

    MIT License

    Copyright (c) 2021 Kushal Das <kushaldas@gmail.com>

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


Installing flit package
====================================

You have to install *flit* package in your system. For this we are
using a virtualenv. We will also install *wheel*
package.

::

    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ python3 -m pip install flit wheel


pyproject.toml
===============

Finally we have to write a *pyproject.toml* which then can be used to create a source
tarball or installing the software, or create a wheel to be uploaded to PyPI.

`flit init` command will help to create the initial file for us, provide the proper input as it asks.

::

    $ flit init
    Module name [pymfactorial]: 
    Author [Kushal Das]: 
    Author email [kushal@sunet.se]: mail@kushaldas.in
    Home page [https://github.com/kushaldas/pymfactorial]: https://github.com/kushaldas/pym
    Choose a license (see http://choosealicense.com/ for more info)
    1. MIT - simple and permissive
    2. Apache - explicitly grants patent rights
    3. GPL - ensures that code based on this is shared with the same terms
    4. Skip - choose a license later
    Enter 1-4 [4]: 1

    Written pyproject.toml; edit that file to add optional extra info.

This command created the `pyproject.toml` file in the same folder, we can check the conent.

::

    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"

    [project]
    name = "pymfactorial"
    authors = [{name = "Kushal Das", email = "mail@kushaldas.in"}]
    readme = "README.md"
    license = {file = "LICENSE"}
    classifiers = ["License :: OSI Approved :: MIT License"]
    dynamic = ["version", "description"]

    [project.urls]
    Home = "https://github.com/kushaldas/pym"


Next we will update the file to make sure that we include the `LICENSE` and
`README.md` file in the source tarball. We also mark the `cli` function as
the starting point for the command line tool.

::

    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"

    [project]
    name = "pymfactorial"
    authors = [{name = "Kushal Das", email = "mail@kushaldas.in"}]
    readme = "README.md"
    license = {file = "LICENSE"}
    classifiers = ["License :: OSI Approved :: MIT License"]
    dynamic = ["version", "description"]

    [project.urls]
    Home = "https://github.com/kushaldas/pym"

    [project.scripts]
    myfact = "pymfactorial:cli"

    [tool.flit.sdist]
    include = ["LICENSE", "README.MD"]


Please read `flit metadata documentation <https://flit.readthedocs.io/en/latest/pyproject_toml.html#new-style-metadata>`_ for details of the various keys and their values mentioned above.



Building a package
==================

To create a source release and also a binary wheel for distribution, use the following
command.

::

    $ flit build

One can see the output files under *dist* directory.
::

    $ ls dist/

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

    $ python3 -m pip install twine
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

    $ python3 -m pip install --index-url https://test.pypi.org/simple/ pymfactorial

More readings
==============

Please visit https://packaging.python.org to learn more about Python packaging.
There are many guides and tutorials available on that site. `PEP-621
<https://www.python.org/dev/peps/pep-0621/>`_ is also an important read.
