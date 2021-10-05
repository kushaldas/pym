

==========================
If-else , the control flow
==========================

While working on real life of problems we have to make decisions. Decisions
like which camera to buy or which cricket bat is better. At the time of writing
a computer program we do the same. We make the decisions using if-else
statements, we change the flow of control in the program by using them.

If statement
============

The syntax looks like

::

    if expression:
        do this

If the value of *expression* is true (anything other than zero), do the what is
written below under indentation. Please remember to give proper indentation,
all the lines indented will be evaluated on the True value of the expression.
One simple example is to take some number as input and check if the number is
less than 100 or not.

::

    #!/usr/bin/env python3
    number = int(input("Enter a number: "))
    if number < 100:
        print("The number is less than 100")

Then we execute the file.

::

    $ ./number100.py
    Enter a number: 12
    The number is less than 100

Else statement
==============

Now in the above example we want to print "Greater than" if the number is
greater than 100. For that we have to use the *else* statement. This works when
the *if* statement is not fulfilled.

::

    #!/usr/bin/env python3
    number = int(input("Enter a number: "))
    if number < 100:
        print("The number is less than 100")
    else:
        print("The number is greater than 100")

The output

::

    $ ./number100.py
    Enter a number: 345
    The number is greater than 100

Another very basic example

::

    >>> x = int(input("Please enter an integer: "))
    >>> if x < 0:
    ...      x = 0
    ...      print('Negative changed to zero')
    ... elif x == 0:
    ...      print('Zero')
    ... elif x == 1:
    ...      print('Single')
    ... else:
    ...      print('More')

Truth value testing
===================

The elegant way to test Truth values is like

::

    if x:
        pass

.. warning:: Don't do this
    
    ::
    
        if x == True:
            pass


match statements
=================

From Python 3.10 we have `match` statements. We can use these instead of if/elif/else blocks.
For example, in the following code, we are taking an integer as input and then matching the value with some predefined
HTTP status codes and print the names.

::

    status = int(input("Give us a status code: "))
    match status:
        case 200:
            print("OK")
        case 201:
            print("Created")
        case 301:
            print("Moved Permanently")
        case 302:
            print("Found")
        case _:
            print("The status is unknown to us.")

The last line, we are matching against anything else, we call it *wildcard* matching.

We can even match complex objects, say against tuples, or other objects.

::

    status = (100,500)
    match status:
        case (x,y):
            print(f"X and Y are: {x}, {y}")
        case x:
            print(x)

    status = 42
    match status:
        case (x,y):
            print(f"X and Y are: {x}, {y}")
        case x:
            print(x)

