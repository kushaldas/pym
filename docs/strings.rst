
=======
Strings
=======

Strings are nothing but simple text. In Python we declare strings in between "" or '' or ''' ''' or """ """. The examples below will help you to understand string in a better way.

::

    >>> s = "I am Indian"
    >>> s
    'I am Indian'
    >>> s = 'I am Indian'
    >>> s = "Here is a line \
    ... split in two lines"
    >>> s
    'Here is a line split in two lines'
    >>> s = "Here is a line \n split in two lines"
    >>> s
    'Here is a line \n split in two lines'
    >>> print(s)
    Here is a line
     split in two lines

Now if you want to multiline strings you have to use triple single/double quotes.

::

    >>> s = """ This is a
    ... multiline string, so you can
    ... write many lines"""
    >>> print(s)
    This is a
    multiline string, so you can
    write many lines


We can have two string literals side by side, and it will behave like a single string. For example

::

    >>> s = "Hello " "World"
    >>> print(s)
    Hello World

This will help you to spilt a long string into smaller chunks in function calls.


You can find length of any string using the `len` function call.

::

    >>> s = "Python"
    >>> len(s)
    6


Different methods available for Strings
=======================================

Every string object is having couple of builtin methods available, we already saw some of them like *s.split(" ")*.

::

    >>> s = "kushal das"
    >>> s.title()
    'Kushal Das'

*title()* method returns a titlecased version of the string, words start with uppercase characters, all remaining cased characters are lowercase.

::

    >>> z = s.upper()
    >>> z
    'KUSHAL DAS'
    >>> z.lower()
    'kushal das'

*upper()* returns a total uppercase version whereas *lower()* returns a lower case version of the string.

::

    >>> s = "I am A pRoGraMMer"
    >> s.swapcase()
    'i AM a PrOgRAmmER'

*swapcase()* returns the string with case swapped :)

::

    >>> s = "jdwb 2323bjb"
    >>> s.isalnum()
    False
    >>> s = "jdwb2323bjb"
    >>> s.isalnum()
    True

Because of the space in the first line *isalnum()* returned *False* , it checks for all characters are alpha numeric or not.

::

    >>> s = "SankarshanSir"
    >>> s.isalpha()
    True
    >>> s = "Sankarshan Sir"
    >>> s.isalpha()
    False

*isalpha()* checkes for only alphabets.

::

    >>> s = "1234"
    >>> s.isdigit() # To check if all the characters are digits or not
    True
    >>> s = "Fedora9 is coming"
    >>> s.islower() # To check if all chracters are lower case or not
    False
    >>> s = "Fedora9 Is Coming"
    >>> s.istitle() # To check if it is a title or not
    True
    >>> s = "INDIA"
    >>> s.isupper() # To check if characters are in upper case or not
    True

To split any string we have *split()*. It takes a string as an argument , depending on that it will split the main string and returns a list containing splitted strings.

::

    >>> s = "We all love Python"
    >>> s.split(" ")
    ['We', 'all', 'love', 'Python']
    >>> x = "Nishant:is:waiting"
    >>> x.split(':')
    ['Nishant', 'is', 'waiting']

The opposite method for *split()* is *join()*. It takes a list contains strings as input and join them.

::

    >>> "-".join("GNU/Linux is great".split(" "))
    'GNU/Linux-is-great'

In the above example first we are splitting the string "GNU/Linux is great" based on the white space, then joining them with "-".

Strip the strings
=================

Strings do have few methods to do striping. The simplest one is *strip(chars)*. If you provide the chars argument then it will strip any combination of them. By default it strips only whitespace or newline characters.

::

    >>> s = "  abc\n "
    >>> s.strip()
    'abc'

You can particularly strip from the left hand or right hand side also using *lstrip(chars)* or *rstrip(chars)*.

::

    >>> s = "www.foss.in"
    >>> s.lstrip("cwsd.")
    'foss.in'
    >>> s.rstrip("cnwdi.")
    'www.foss'

Finding text
============

Strings have some methods which will help you in finding text/substring in a string. Examples are given below:

::

    >>> s = "faulty for a reason"
    >>> s.find("for")
    7
    >>> s.find("fora")
    -1
    >>> s.startswith("fa") #To check if the string startswith fa or not
    True
    >>> s.endswith("reason") #To check if the string endswith reason or not
    True

*find()* helps to find the first occurrence of the substring given, if not found it returns -1.

Palindrome checking
===================

Palindrome are the kind of strings which are same from left or right whichever way you read them. Example "madam". In this example we will take the word as input from the user and say if it is palindrome or not.

.. code-block:: python

    #!/usr/bin/env python3
    s = input("Please enter a string: ")
    z = s[::-1]
    if s == z:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

The output

::

    $ ./palindrome.py
    Please enter a string: madam1
    The string is not a palindrome
    $ ./palindrome.py
    Please enter a string: madam
    The string is a palindrome

Number of words
===============

In this example we will count the number of words in a given line

::

    #!/usr/bin/env python3
    s = input("Enter a line: ")
    print("The number of words in the line are %d" % (len(s.split(" "))))

The output
::

    $ ./countwords.py
    Enter a line: Sayamindu is a great programmer
    The number of words in the line are 5


Iterating over all characters of a string
==========================================

You can iterate over a string using simple `for` loop.

::

    >>> for ch in "Python":
    ...     print(ch)
    ... 
    P
    y
    t
    h
    o
    n

