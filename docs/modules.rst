

=======
Modules
=======

In this chapter we are going to learn about Python modules.

Introduction
============


Up until now, all the code we wrote in the python interpreter was lost when we exited the interpreter. But when people write large programs they tend to break their code into multiple different files for ease of use, debugging and readability. In python we use *modules* to achieve such goals. Modules are nothing but files with python definitions and statements. The module name, to import, has the same name of the python file without the .py extension. 

You can find the name of the module by accessing the *__name__* variable. It is a global variable.

Now we are going to see how modules work. Create a file called bars.py. Content of the file is given bellow.

::

    """
    Bars Module
    ============
    This is an example module with provide different ways to print bars.
    """
    def starbar(num):
        """
        Prints a bar with *
        :arg num: Length of the bar
        """
        print '*' * num

    def hashbar(num):
        """
        Prints a bar with #
        :arg num: Length of the bar
        """
        print '#' * num
    
    def simplebar(num):
        """
        Prints a bar with -
        :arg num: Length of the bar
        """
        print '-' * num

Now we are going to start the python interpreter and import our module.

::

    >>> import bars
    >>>

This will import the module bars. We have to use the module name to access functions inside the module.

::

    >>> bars.hashbar(10)
    ##########
    >>> bars.simplebar(10)
    ----------
    >>> bars.starbar(10)
    **********

Importing modules
=================

There are different ways to import modules. We already saw one way to do this. You can even import selected functions from modules. To do so:

::

    >>> from bars import simplebar, starbar
    >>> simplebar(20)
    --------------------

.. note:: Never do *from module import \** Read `this link <http://docs.python.org/2/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module>`_ for more information.

Submodules
==========

We can many submodules inside a module. A directory with a *__init__.py* can also be used a module and all *.py* files inside it become submodules.

::

    $ tree mymodule
    mymodule
    |-- bars.py
    |-- __init__.py
    `-- utils.py

In this example *mymodule* is the module name and *bars* and *utils* are two submodules in it. You can create an empty *__init__.py* using touch command.

::

    $ touch mymodule/__init__.py


__all__ in __init__.py
=======================

If `__init__.py` file contains a list called `__all__` then, only the values listed there will only
be imported when some will call `from module import *`. So if in the mymodule's `__init__.py`
file contains the following
::

    from bars import simplebar
    __all__ = [simplebar, ]

Then if someone does `from mymodule import *` only `simplebar` will be available for them.


Default modules
===============

Now your Python installation comes with different modules installed, you can use them as required and install new modules for any other special purposes. In the following few examples we are going to see many examples on the same.

::

    >>> help()
    Welcome to Python 2.6!  This is the online help utility.
    If this is your first time using Python, you should definitely check out
    the tutorial on the Internet at http://docs.python.org/tutorial/.
    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".
    To get a list of available modules, keywords, or topics, type "modules",
    "keywords", or "topics".  Each module also comes with a one-line summary
    of what it does; to list the modules whose summaries contain a given word
    such as "spam", type "modules spam".
    help> modules

The above example shows how to get the list of all installed modules in your system. I am not pasting them here as it is a big list in my system :)

You can also use *help()* function in the interpeter to find documentation about any module/classes. Say you want to know all available methods in strings, you can use the following method

::

    >>> help(str)






Module os
=========

os module provides operating system dependent functionality. You can import it using the following import statement.

::

    >>> import os

*getuid()* function returns the current process's effective user's id.

::

    >>> os.getuid()
    500

*getpid()* returns the current process's id. *getppid()* returns the parent process's id.

::

    >>> os.getpid()
    16150
    >>> os.getppid()
    14847

*uname()* returns different information identifying the operating system, in Linux it returns details you can get from the *uname* command. The returned object is a tuple, *(sysname, nodename, release, version, machine)*

::

    >>> os.uname()
    ('Linux', 'd80', '2.6.34.7-56.fc13.i686.PAE', '#1 SMP Wed Sep 15 03:27:15 UTC 2010', 'i686')

*getcwd()*returns the current working directory. *chdir(path)* changes the current working directory to path. In the example we first see the current directory which is my home directory and change the current directory to */tmp* and then again checking the current directory.

::

    >>> os.getcwd()
    '/home/kushal'
    >>> os.chdir('/tmp')
    >>> os.getcwd()
    '/tmp'

So let us use another function provided by the os module and create our own function to list all files and directories in any given directory.

::

    def view_dir(path='.'):
        """
        This function prints all files and directories in the given directory.
        :args path: Path to the directory, default is current directory
        """
        names = os.listdir(path)
        names.sort()
        for name in names:
            print name,

Using the *view_dir* example.

::

    >>> view_dir('/')
    .readahead bin boot dev etc home junk lib lib64 lost+found media mnt opt 
    proc root run sbin srv sys tmp usr var


