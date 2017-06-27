

=============
The Beginning
=============

Let's look at our first code, hello world. Because Python is an interpreted
language, you can write the code into the Python interpreter directly or you
can write the code in a file and then run the file. In this topic, we will
first write the code using the interpreter, after starting Python in the
command prompt (shell or terminal). In case you are new to Linux command line,
+then you can read learn about various command from `this
book <https://lym.readthedocs.io/en/latest/>`_


Note that the code samples that follow use the latest Python built from the
source code, so the version number can be different.

::

    Python 3.5.0a0 (default:d6ac4b6020b9+, Jun  9 2014, 12:15:05)
    [GCC 4.8.2 20131212 (Red Hat 4.8.2-7)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Using the Python interpreter
==============================

In our first code we are going to print "Hello World!" using the interpreter. To generate the output, type the following:

::

    >>> print("Hello World!")
    Hello World!

Using a source file
=====================

As a serious programmer, you might want to write the above code into a source file. Use any text editor you like to create the file called helloworld.py. I used vi. You can even use GUI based tools like Kate or gedit. Enter the following text:

::

    #!/usr/bin/env python3
    print("Hello World!")

To run the code first you have to make the file executable. In GNU/Linux you can do this by typing the following command in a shell or terminal:

::

    $ chmod +x helloworld.py

Now you can type the filename and it will run:

::

    $ ./helloworld.py
    Hello World!

On the first line you can *#!*, what we call it sha-bang. The sha-bang indicates that the Python interpreter should run this code. On the next line we are printing a text message. In Python we call all the lines of text "strings."

Whitespaces and indentation
===========================

In Python whitespace is an important thing. We divide different identifiers using spaces. Whitespace in the beginning of the line is known as indentation, but if you give wrong indentation it will throw an error. Below are some examples:

::

    >>> a = 12
    >>>  a = 12
    File "<stdin>", line 1
    a = 12
    ^
    IndentationError: unexpected indent

.. warning:: Warning
   There is an extra space in the beginning of the second line which is causing the error, so always look for the proper indentation.
   You can even get into this indentation errors if you mix up tabs and spaces. Like if you use spaces and only use spaces for indentation, don't use tabs in that case. For you it may look same, but the code will give you error if you try to run it.

So we can have few basic rules ready for spaces and indentation.

- Use 4 spaces for indentation.

- Never mix tab and spaces.

- One blank line between functions.

- Two blank lines between classes.

There are more places where you should be following the same type of whitespace rules:

- Add a space after "," in dicts, lists, tuples, and argument lists and after ":" in dicts.

- Spaces around assignments and comparisons (except in argument list)

- No spaces just inside parentheses.

Comments
========

Comments are snippets of English text that explain what this code does. Write comments in the code so that is easier for others to  understand. A comment line starts with *#*. Everything after that is ignored as a comment and does not affect the program.

::

    >>> # This is a comment
    >>> # The next line will add two numbers
    >>> a = 12 + 34
    >>> print(c) #this is a comment too :)

Comments are mainly for people who *develop* or *maintain* the codebase. So if you have any complex code, you should write enough comments inside so that anyone else can understand the code by reading the comments. Always give a space after # and then start writing the comment. You can also use some standard comments like:

::

    # FIXME -- fix these code later
    # TODO -- in future you have to do this

Modules
=======

Modules are Python files that contain different function definitions or variables that can be reused. Module files should always end with a .py extension. Python itself has a vast module library with the default installation. We will use some of them later. To use a module you have to import it first.

::

    >>> import math
    >>> print(math.e)
    2.71828182846

We will learn more about modules in the Modules chapter.
