

=======
Modules
=======

In this chapter we are going to learn about Python modules.

Introduction
============


Up until now, all the code we wrote in the Python interpreter was lost when we exited the interpreter. But when people write large programs they tend to break their code into multiple different files for ease of use, debugging and readability. In Python we use *modules* to achieve such goals. Modules are nothing but files with Python definitions and statements. The module name, to import, has the same name of the Python file without the .py extension. 

You can find the name of the module by accessing the *__name__* variable. It is a global variable.

Now we are going to see how modules work. Create a file called bars.py. Content of the file is given bellow.

::

    """
    Bars Module
    ============
    This is an example module with provide different ways to print bars.
    """
    def starbar(num):
        """Prints a bar with *

        :arg num: Length of the bar
        """
        print('*' * num)

    def hashbar(num):
        """Prints a bar with #

        :arg num: Length of the bar
        """
        print('#' * num)
    
    def simplebar(num):
        """Prints a bar with -
        
        :arg num: Length of the bar
        """
        print('-' * num)

Now we are going to start the Python interpreter and import our module.

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

.. warning:: Never do *from module import \** Read `this link <http://docs.python.org/2/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module>`_ for more information.

Submodules
==========

We can have many submodules inside a module. A directory with a *__init__.py* can also be used as a module and all *.py* files inside it become submodules.

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

If `__init__.py` file contains a list called `__all__`, then only the names listed there will
be public. So if the mymodule's `__init__.py`
file contains the following
::

    from mymodule.bars import simplebar
    __all__ = [simplebar, ]


Then from mymodule only `simplebar` will be available.

.. note:: *from mymodule import \** will only work for module level objects, trying to use it to import functions or classes
    will cause syntax error.

Default modules
===============

Now your Python installation comes with different modules installed, you can use them as required and install new modules for any other special purposes. In the following few examples we are going to see many examples on the same.

::

    >>> help()

    Welcome to Python 3.5's help utility!

    If this is your first time using Python, you should definitely check out
    the tutorial on the Internet at http://docs.python.org/3.5/tutorial/.

    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".

    To get a list of available modules, keywords, symbols, or topics, type
    "modules", "keywords", "symbols", or "topics".  Each module also comes
    with a one-line summary of what it does; to list the modules whose name
    or summary contain a given string such as "spam", type "modules spam".

    help> modules

The above example shows how to get the list of all installed modules in your system. I am not pasting them here as it is a big list in my system :)

You can also use *help()* function in the interpeter to find documentation about any module/classes. Say you want to know all available methods in strings, you can use the following method

::

    >>> help(str)






Module os
=========

:py:mod:`os` module provides operating system dependent functionality. You can import it using the following import statement.

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
            print(name, end =' ')

Using the *view_dir* example.

::

    >>> view_dir('/')
    .readahead bin boot dev etc home junk lib lib64 lost+found media mnt opt 
    proc root run sbin srv sys tmp usr var


There are many other very useful functions available in the OS module, you can read about them `here <https://docs.python.org/3/library/os.html>`_

Requests Module
================

requests is a Python module which changed the way people used to write code for many many projects. It helps
you to do HTTP GET or POST calls in a very simple but elegant way. This is a third party module, that means
you have to install it from your OS distribution packages, it does not come default.

::

    # yum install python3-requests


The above command will install Python3 version of the requests module in your system.


Getting a simple web pages
------------------------------

You can use the *get* method to fetch any website.

::

    >>> import requests
    >>> req = requests.get('http://google.com')
    >>> req.status_code
    200

The *text* attribute holds the HTML returned by the server.

Using this knowledge, let us write a command which can download a given file (URL) from Internet.


.. code:: python 

    #!/usr/bin/env python3
    import os
    import os.path
    import requests

    def download(url):
        '''Download the given url and saves it to the current directory.

        :arg url: URL of the file to be downloaded.
        '''
        req = requests.get(url)
        # First let us check non existing files.
        if req.status_code == 404:
            print('No such file found at %s' % url)
            return
        filename = url.split('/')[-1]
        with open(filename, 'wb') as fobj:
            fobj.write(req.content)
        print("Download over.")

    if __name__ == '__main__':
        url = input('Enter a URL:')
        download(url)


Here we used something new, when the module name is *__main__*, then only
ask for a user input and then download the given URL. This also prevents 
the same when some other Python code imports this file as a Python module.

To learn more about requests module, go to their `wonderful documentation <http://docs.python-requests.org>`_.

You can actually modify the above program to become more user friendly. For example, you can check if that given
filename already exists in the current directory or not. Use :py:mod:`os.path` module for the name.


Command line arguments
======================

Do you remember your *ls* command, you can pass different kind of options as command line arguments. You can do that too .. important:: your application. Read `this how-to <https://docs.python.org/3/howto/argparse.html>`_ guide to learn about it.


TAB completion in your Python interpreter
==========================================

First create a file as *~/.pythonrc* and include the following in that file

::

    import rlcompleter, readline
    readline.parse_and_bind('tab: complete')


    history_file = os.path.expanduser('~/.python_history')
    readline.read_history_file(history_file)

    import atexit
    atexit.register(readline.write_history_file, history_file)


Next, just export PYTHONSTARTUP variable pointing to this file from your *~/.bashrc* file.

::

    export PYTHONSTARTUP=~/.pythonrc


Now from future whenever you open a bash shell, you will have TAB completion and history of code entered in your
Python interpreter.

To use it in the current shell, source the bashrc file.

::

    $ source ~/.bashrc

