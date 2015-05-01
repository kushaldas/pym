

=============
The Beginning
=============

So, we are going to look at our first code. As Python is an interpreted language, you can either write the code directly into the Python interpreter or write it in a file and then run the file. First, we are going to start by using the interpreter. To start, type python in the command prompt (shell or terminal). I am using the latest Python built from the source code, so the version number may be different.

::

    Python 3.5.0a0 (default:d6ac4b6020b9+, Jun  9 2014, 12:15:05)
    [GCC 4.8.2 20131212 (Red Hat 4.8.2-7)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>


In our first code, we are going to print "Hello World!", try it as shown below,
::

    >>> print("Hello World!")
    Hello World!

helloworld.py
=============

Now, as a serious programmer, you may want to write the above code into a source file. We will create a helloworld.py. Use any text editor you like to create the file. I used vi, you can use GUI based tools like Kate or gedit if you prefer.

::

    #!/usr/bin/env python3
    print("Hello World!")

To run the code, first, you have to make the file executable. Under GNU/Linux, you can accomplish that by giving the following command in a shell or a terminal

::

    $ chmod +x helloworld.py

Then

::

    $ ./helloworld.py
    Hello World!

On the first, line you may have noticed the  *#!*. We call it the sha-bang or shebang, depending on your preference. By using the sha-bang, we are essentially telling the Python interpreter to run this code in Python and specifically Python3. In the next line, we are printing a text message. In Python we call all lines of texts strings.

Whitespaces and Indentation
===========================

In Python, whitespaces are important. We divide different identifiers using spaces. Whitespace in the beginning of the line is known as indentation, but if you give the interpreter wrong indentation it will throw an error. Examples are given below:

::

    >>> a = 12
    >>>  a = 12
    File "<stdin>", line 1
    a = 12
    ^
    IndentationError: unexpected indent

.. warning:: Warning
   -------
   There is an extra space in the beginning of the second line which is causing the error, so always look for the proper indentation.
   You can even get into this indentation errors if you mix up tabs and spaces. For example if you use spaces, only use spaces for indentation, don't use tabs in that case. From your perspective, it may look the same, but the code will throw you an error if you try to run it.

So, we can have few basic rules ready for spaces and indentation:

- Use 4 spaces for indentation.

- Never mix tabs and spaces.

- One blank line between functions.

- Two blank lines between classes.

There are more places where you should be following the same type of rules of whitespace, they are:

- Add a space after "," in dicts, lists, tuples, and argument lists and after ":" in dicts.

- Spaces around assignments and comparisons (except in argument list).

- No spaces just inside parentheses.

Comments
========

Comments are some piece of English text which explains what the code does. We write comments in the code so that it is easier for others to read and understand. A comment line starts with *#* and everything after that is ignored as comment, which means they don't effect the program.

::

    >>> # This is a comment
    >>> # The next line will add two numbers
    >>> a = 12 + 34
    >>> print(c) # this is a comment too :)

Comments are mainly for the people who would *develop* or *maintain* the codebase. That means if you have some complex code somewhere, you should write enough comments inside in a way that anyone else reading the code can understand it by simply reading the comments. You should always give a space after # and then start writing the comment. You can also use some standard comments like

::

    # FIXME -- fix this code later
    # TODO -- in the future you have to do this

Modules
=======

Modules are Python files that contain different class and function definitions and variables that we can reuse. Python module files should always end with a .py extension. Python itself comes with a vast module library with the default installation. We are going to use some of them. To use a module you have to import it first.

::

    >>> import math
    >>> print(math.e)
    2.71828182846

We are going to learn more about modules in the Modules chapter.
