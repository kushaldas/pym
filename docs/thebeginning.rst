

=============
The Beginning
=============

So we are going to look at our first code. As Python is an interpreted language , you can directly write the code into the Python interpreter or write in a file and then run the file. First we are going to do that using the interpreter, to start type python in the command prompt (shell or terminal). I am using the latest Python built from the source code, so the version number can be different.

::

    Python 3.5.0a0 (default:d6ac4b6020b9+, Jun  9 2014, 12:15:05)
    [GCC 4.8.2 20131212 (Red Hat 4.8.2-7)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>


In our first code we are going to print "Hello World!" , so do it as below,
::

    >>> print("Hello World!")
    Hello World!

helloworld.py
=============

Now as a serious programmer you may want to write the above code into a source file. We will create a helloworld.py. Use any text editor you like to create the file. I used vi, you can even use GUI based tools like Kate, gedit too.

::

    #!/usr/bin/env python3
    print("Hello World!")

To run the code first you have to make the file executable, in GNU/Linux you can do that by giving the command in a shell or terminal

::

    $ chmod +x helloworld.py

Then

::

    $ ./helloworld.py
    Hello World!

On the first line you can *#!* , we call it sha-bang. Using this we are telling that use Python interpreter to run this code. In the next line we are printing a text message. In Python we call all the line of texts as strings.

Whitespaces and indentation
===========================

In Python whitespace is an important thing. We divide different identifiers using spaces.Whitespace in the beginning of the line is known as indentation, but if you give wrong indentation it will throw an error. Examples are given below:

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

There are more places where you should be following same type of rules of whitespace, they are like

- Add a space after "," in dicts, lists, tuples, and argument lists and after ":" in dicts.

- Spaces around assignments and comparisons (except in argument list)

- No spaces just inside parentheses.

Comments
========

Comments are some piece of English text which explains what this code does, we write comments in the code so that is easier for others to  understand. A comment line starts with *#* , everything after that is ignored as comment, that means they don't effect on the program.

::

    >>> # This is a comment
    >>> # The next line will add two numbers
    >>> a = 12 + 34
    >>> print(c) #this is a comment too :)

Comments are mainly for the people who would *develop* or *maintain* the codebase, so it means if you have some complex code somewhere you should write enough comments inside so that anyone else can understand the code by reading the comments. You should always give a space after # and then start writing
the comment. You can also use some standard comments like

::

    # FIXME -- fix these code later
    # TODO -- in future you have to do this

Modules
=======

Modules are Python files which contain different function definitions , variables which we can reuse, it should always end with a .py extension. Python itself is having a vast module library with the default installation. We are going to use some of them. To use a module you have to import it first.

::

    >>> import math
    >>> print(math.e)
    2.71828182846

We are going to learn more about modules in the Modules chapter.
