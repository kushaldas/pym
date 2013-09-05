

=======================
Variables and Datatypes
=======================

Every programming language is having own grammar rules just like the other languages we speak.

Keywords and Identifiers
========================

Python codes can be divided into identifiers. Identifiers (also referred to as names) are described by the following lexical definitions:

::

    identifier ::= (letter|"_") (letter | digit | "_")*
    letter ::= lowercase | uppercase
    lowercase ::= "a"..."z"
    uppercase ::= "A"..."Z"
    digit ::= "0"..."9"

This means *_abcd* is a valid identifier where as *1sd* is not. The following identifiers are used as reserved words, or keywords of the language, and cannot be used as ordinary identifiers. They must be spelled exactly as written here:

::

    and       del      from      not   while
    as        elif     global    or    with
    assert    else     if        pass  yield
    break     except   import    print
    class     exec     in        raise
    continue  finally  is        return
    def       for      lambda    try

In Python we don't specify what kind of data we are going to put in a variable. So you can directly write abc = 1 and abc will become an integer datatype. If you write abc = 1.0 abc will become of floating type. Here is a small program to add two given numbers

::

    >>> a = 13
    >>> b = 23
    >>> a + b
    36

From the above example you can understand that to declare a variable in python , what you need is just to type the name and the value. Python can also manipulate strings They can be enclosed in single quotes or double quotes like

::

    >>> 'India'
    'India'
    >>> 'India\'s best'
    "India's best"
    >>> "Hello World!"
    'Hello World!'

Reading input from the Keyboard
===============================

Generally the real life python codes do not need to read input from the keyboard. In python we use raw_input function to do input. *raw_input("String to show")* , this will return a string as output. Let us write a program to read a number from the keyboard and check if it is less than 100 or not. Name of the program is testhundred.py

.. code-block:: python

    #!/usr/bin/env python
    number = int(raw_input("Enter an integer: "))
    if number < 100:
        print "Your number is smaller than 100"
    else:
        print "Your number is greater than 100"

The output

::

    $ ./testhundred.py
    Enter an integer: 13
    Your number is smaller than 100
    $ ./testhundred.py
    Enter an integer: 123
    Your number is greater than 100

In the next program we are going to calculate investments.

::

    #!/usr/bin/env python
    amount = float(raw_input("Enter amount: "))
    inrate = float(raw_input("Enter Interest rate: "))
    period = int(raw_input("Enter period: "))
    value = 0
    year = 1
    while year <= period:
        value = amount + (inrate * amount)
        print "Year %d Rs. %.2f" % (year, value)
        amount = value
        year = year + 1

The output

::

    $ ./investment.py
    Enter amount: 10000
    Enter Interest rate: 0.14
    Enter period: 5
    Year 1 Rs. 11400.00
    Year 2 Rs. 12996.00
    Year 3 Rs. 14815.44
    Year 4 Rs. 16889.60
    Year 5 Rs. 19254.15

Some Examples
=============

Some examples of variables and datatypes:

Average of N numbers
--------------------

In the next program we will do an average of N numbers.

::

    #!/usr/bin/env python
    N = 10
    sum = 0
    count = 0
    while count < N:
        number = float(raw_input(""))
        sum = sum + number
        count = count + 1
    average = float(sum)/N
    print "N = %d , Sum = %f" % (N, sum)
    print "Average = %f" % average


The output

::

    $ ./averagen.py
    1
    2.3
    4.67
    1.42
    7
    3.67
    4.08
    2.2
    4.25
    8.21
    N = 10 , Sum = 38.800000
    Average = 3.880000

Temperature conversion
----------------------

In this program we will convert the given temperature to Celsius from Fahrenheit by using the formula C=(F-32)/1.8

::

    #!/usr/bin/env python
    fahrenheit = 0.0
    print "Fahrenheit Celsius"
    while fahrenheit <= 250:
        celsius = ( fahrenheit - 32.0 ) / 1.8 # Here we calculate the Celsius value
        print "%5.1f %7.2f" % (fahrenheit , celsius)
        fahrenheit = fahrenheit + 25

The output

::

    [kd@kdlappy book]$ ./temperature.py
    Fahrenheit Celsius
    0.0  -17.78
    25.0   -3.89
    50.0   10.00
    75.0   23.89
    100.0   37.78
    125.0   51.67
    150.0   65.56
    175.0   79.44
    200.0   93.33
    225.0  107.22
    250.0  121.11

Multiple assignments in a single line
=====================================

You can even assign values to multiple variables in a single line, like

::

    >>> a , b = 45, 54
    >>> a
    45
    >>> b
    54

Using this swapping two numbers becomes very easy

::

    >>> a, b = b , a
    >>> a
    54
    >>> b
    45

To understand how this works, you will have to learn about a data type called *tuple*. We use *comma* to create tuple. In the right hand side we create the tuple (we call this as tuple packing) and in the left hand side we do tuple unpacking into a new tuple.

Below we have another example of tuple unpacking.

::

    >>> data = ("Kushal Das", "India", "Python")
    >>> name, country, language = data
    >>> name
    'Kushal Das'
    >>> country
    'India'
    >>> language
    'Python'


