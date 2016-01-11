

==========
Virtualenv
==========

Virtual Python Environment or venv is a Python environment which will help you to install different versions of Python modules in a local directory using which you can develop and test your code without requiring to install everything systemwide.

Installation
============

In Python3 now there is a command called *pyvenv* which can be used to create virtual environments.

Usage
=====

We will create a directory call *virtual* inside which we will have two different virtual environment.

The following commands will create an env called virt1.

::

    $ cd virtual
    $ pyvenv virt1
    $

Now we can activate the virt1 environment.

::

    $ source virt1/bin/activate
    (virt1)[user@host]$

The first part of the prompt is now the name of the virtual environment, it will help you identify which environment you are in when you have multiple environments.

To deactivate the environment use *deactivate* command.

::

    (virt1)$ deactivate
    $

So, now we will install a Python module called redis.

::

    (virt1)$ pip install redis
    Collecting redis
      Downloading redis-2.10.5-py2.py3-none-any.whl (60kB)
        100% |████████████████████████████████| 61kB 607kB/s 
    Installing collected packages: redis
    Successfully installed redis-2.10.5


Now we will create another virtual environment *virt2* where we will install the same redis module but an old 2.4 version of it.

::

    $ virtualenv virt2
    New python executable in virt1/bin/python
    Installing setuptools............done.
    Installing pip...............done.
    $ source virt2/bin/activate
    (virt2)$
    (virt2)$ pip install redis==2.4
    Downloading/unpacking redis
    Downloading redis-2.4.0.tar.gz
    Running setup.py egg_info for package redis
    Installing collected packages: redis
    Running setup.py install for redis
    Successfully installed redis
    Cleaning up...

This way you can have many different environments for all of your development needs.

.. note:: Always remember to create virtualenvs while developing new applications. This will help you keep the system modules clean.


