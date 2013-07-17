

=============
File handling
=============

A file is some information or data which stays in the computer storage devices. You already know about different kinds of file , like your music files, video files, text files. Python gives you easy ways to manipulate these files. Generally we divide files in two categories, text file and binary file. Text files are simple text where as the binary files contain binary data which is only readable by computer.

File opening
============

To open a file we use *open()* function. It requires two arguments, first the file path or file name, second which mode it should open. Modes are like

+ "r" -> open read only, you can read the file but can not edit / delete anything inside

+ "w" -> open with write power, means if the file exists then delete all content and open it to write

+ "a" -> open in append mode

The default mode is read only, ie if you do not provide any mode it will open the file as read only. Let us open a file

::

    >>> fobj = open("love.txt")
    >>> fobj
    <open file 'love.txt', mode 'r' at 0xb7f2d968>

Closing a file
==============

After opening a file one should always close the opened file. We use method *close()* for this.

::

    >>> fobj = open("love.txt")
    >>> fobj
    <open file 'love.txt', mode 'r' at 0xb7f2d968>
    >>> fobj.close()

.. important:: Important

   Always make sure you *explicitly* close each open file, once its job is done and you have no reason to keep it open.
   Because
   - There is an upper limit to the number of files a program can open. If you exceed that limit, there is no reliable way of recovery, so the program could crash.
   - Each open file consumes some main-memory for the data-structures associated with it, like file descriptor/handle or file locks etc. So you could essentially end-up wasting lots of memory if you have more files open that are not useful or usable.
   - Open files always stand a chance of corruption and data loss.

Reading a file
==============

To read the whole file at once use the *read()* method.

::

    >>> fobj = open("sample.txt")
    >>> fobj.read()
    'I love Python\nPradeepto loves KDE\nSankarshan loves Openoffice\n'

If you call *read()* again it will return empty string as it already read the whole file. readline() can help you to read one line each time from the file.

::

    >>> fobj = open("sample.txt")
    >>> fobj.readline()
    'I love Python\n'
    >>> fobj.readline()
    'Pradeepto loves KDE\n'

To read all the lines in a list we use *readlines()* method.

::

    >>> fobj = open("sample.txt")
    >>> fobj.readlines()
    ['I love Python\n', 'Pradeepto loves KDE\n', 'Sankarshan loves Openoffice\n']

You can even loop through the lines in a file object.

::

    >>> fobj = open("sample.txt")
    >>> for x in f:
    ...     print x,
    ...
    I love Python
    Pradeepto loves KDE
    Sankarshan loves Openoffice

Let us write a program which will take the file name as the input from the user and show the content of the file in the console.

::

    #!/usr/bin/env python
    name = raw_input("Enter the file name: ")
    fobj = open(name)
    print fobj.read()
    fobj.close()

In the last line you can see that we closed the file object with the help of close() method.

The output

::

    $ ./showfile.py
    Enter the filename: sample.txt
    I love Python
    Pradeepto loves KDE
    Sankarshan loves Openoffice

Writing in a file
=================

Let us open a file then we will write some random text into it by using the write() method.

::

    >>> fobj = open("ircnicks.txt", 'w')
    >>> fobj.write('powerpork\n')
    >>> fobj.write('indrag\n')
    >>> fobj.write('mishti\n')
    >>> fobj.write('sankarshan')
    >>> fobj.close()

Now read the file we just created

::

    >>> fobj = open('ircnicks.txt')
    >>> s = fobj.read()
    >>> print s
    powerpork
    indrag
    mishti
    sankarshan

copyfile.py
===========

In this example we will copy a given text file to another file.

::

    #!/usr/bin/env python
    import sys
    if len(sys.argv) < 3:
        print "Wrong parameter"
        print "./copyfile.py file1 file2"
        sys.exit(1)
    f1 = open(sys.argv[1])
    s = f1.read()
    f1.close()
    f2 = open(sys.argv[2], 'w')
    f2.write(s)
    f2.close()

.. note:: This way of reading file is not always a good idea, a file can be very large to read and fit in the memory. It is always better to read a known size of the file and wirte that to the new file.

You can see we used a new module here *sys*. *sys.argv* contains all command line parameters. Remember *cp* command in shell, after *cp* we type first the file to be copied and then the new file name.

The first value in *sys.argv* is the name of the command itself.

::

    #!/usr/bin/env python
    import sys
    print "First value", sys.argv[0]
    print "All values"
    for i, x  in enumerate(sys.argv):
        print i, x

The output

::

    $ ./argvtest.py Hi there
    First value ./argvtest.py
    All values
    0 ./argvtest.py
    1 Hi
    2 there

Here we used a new function *enumerate(iterableobject)*, which returns the index number and the value from the iterable object.

Random seeking in a file
========================

You can also randomly move around inside a file using *seek()* method. It takes two arguments , offset and whence. To know more about it let us read what python help tells us

seek(...)
seek(offset[, whence]) -> None. Move to new file position.
Argument offset is a byte count. Optional argument whence defaults to
0 (offset from start of file, offset should be >= 0); other values are 1
(move relative to current position, positive or negative), and 2 (move
relative to end of file, usually negative, although many platforms allow
seeking beyond the end of a file). If the file is opened in text mode,
only offsets returned by tell() are legal. Use of other offsets causes
undefined behavior.
Note that not all file objects are speakable.

Let us see one example

::

    >>> fobj = open('/tmp/tempfile', 'w')
    >>> fobj.write('0123456789abcdef')
    >>> fobj.close()
    >>> fobj = open('/tmp/tempfile')
    >>> fobj.tell()    #tell us the offset position
    0L
    >>> fobj.seek(5) # Goto 5th byte
    >>> fobj.tell()
    5L
    >>> fobj.read(1) #Read 1 byte
    '5'
    >>> fobj.seek(-3, 2) # goto 3rd byte from the end
    >>> fobj.read() #Read till the end of the file
    'def'

Count spaces, tabs and new lines in a file
==========================================

Let us try to write an application which will count the spaces, tabs, and lines in any given file.

::

    #!/usr/bin/env python

    import os
    import sys


    def parse_file(path):
        """
        Parses the text file in the given path and returns space, tab & new line
        details.

        :arg path: Path of the text file to parse

        :return: A tuple with count of spacaes, tabs and lines. 
        """
        fd = open(path)
        i = 0
        spaces = 0
        tabs = 0
        for i,line in enumerate(fd):
            spaces += line.count(' ')
            tabs += line.count('\t')
        #Now close the open file
        fd.close()

        #Return the result as a tuple
        return spaces, tabs, i + 1

    def main(path):
        """
        Function which prints counts of spaces, tabs and lines in a file.

        :arg path: Path of the text file to parse
        :return: True if the file exits or False.
        """
        if os.path.exists(path):
            spaces, tabs, lines = parse_file(path)
            print "Spaces %d. tabs %d. lines %d" % (spaces, tabs, lines)
            return True
        else:
            return False


    if __name__ == '__main__':
        if len(sys.argv) > 1:
            main(sys.argv[1])
        else:
            sys.exit(-1)
        sys.exit(0)

You can see that we have two functions in the program , *main* and *parse_file* where the second one actually parses the file and returns the result and we print the result in *main* function. By splitting up the code in smaller units (functions) helps us to organize the codebase and also it will be easier to write test cases for the functions.

Using the with statement
=========================

In real life scenarios we should try to use `with` statement. It will take care of closing the file for you.
::

    >>> with open('setup.py') as fobj:
    ...     for line in fobj:
    ...         print line,
    ... 
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
        license = "http://www.gnu.org/copyleft/gpl.html",
        packages=find_packages()
        )

