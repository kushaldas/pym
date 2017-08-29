.. index:: Exception

======================
Exceptions
======================

In this chapter we will learn about exceptions in Python and how to
handle them in your code.


Any error which happens during the execution of the code is an exception. Each
exception generally shows some error message.

NameError
==========

When one starts writing code, this will be one of the most common exception
he/she will find. This happens when someone tries to access a variable which is
not defined.
::

    >>> print(kushal)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'kushal' is not defined

The last line contains the details of the error message, the rest of the lines
shows the details of how it happened (or what caused that exception).

.. index:: TypeError

TypeError
==========

`TypeError` is also one of the most found exception. This happens when someone tries
to do an operation with different kinds of incompatible data types. A common example
is to do addition of Integers and a string.
::

    >>> print(1 + "kushal")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

How to handle exceptions?
=========================

We use `try...except` blocks to handle any exception. The basic syntax looks like
::

    try:
        statements to be inside try clause
        statement2
        statement3
        ...
    except ExceptionName:
        statements to evaluated in case of ExceptionName happens

It works in the following way:

    - First all lines between `try` and `except` statements.
    - If `ExceptionName` happens during execution of the statements then `except` clause statements execute
    - If no exception happens then the statements inside `except` clause does not execute.
    - If the `Exception` is not handled in the `except` block then it goes out of `try` block.

The following examples showcase these scenarios.
::

    >>> def get_number():
    ...     "Returns a float number"
    ...     number = float(input("Enter a float number: "))
    ...     return number
    ...
    >>>
    >>> while True:
    ...     try:
    ...         print(get_number())
    ...     except ValueError:
    ...         print("You entered a wrong value.")
    ...
    Enter a float number: 45.0
    45.0
    Enter a float number: 24,0
    You entered a wrong value.
    Enter a float number: Traceback (most recent call last):
      File "<stdin>", line 3, in <module>
      File "<stdin>", line 3, in get_number
    KeyboardInterrupt

As the first input I provided a proper float value and it printed it back, next
I entered a value with a comma, so the `except` clause executed and the print
statement executed.

In the third time I pressed *Ctrl+c* which caused a `KeyboardInterrupt`, which is
not handled in the `except` block so the execution stopped with that exception.

An empty `except` statement can catch any exception. Read the following example::

    >>> try:
    ...     input() # Press Ctrl+c for a KeyboardInterrupt
    ... except:
    ...     print("Unknown Exception")
    ...
    Unknown Exception

Raising exceptions
===================

One can raise an exception using `raise` statement.
::

    >>> raise ValueError("A value error happened.")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: A value error happened.


We can catch these exceptions like any other normal exceptions.
::

    >>> try:
    ...     raise ValueError("A value error happened.")
    ... except ValueError:
    ...     print("ValueError in our code.")
    ...
    ValueError in our code.

.. index:: finally

Using finally for cleanup
==========================

If we want to have some statements which must be executed under all circumstances,
we can use `finally` clause, it will be always executed before finishing `try`
statements.
::

    >>> try:
    ...     fobj = open("hello.txt", "w")
    ...     res = 12 / 0
    ... except ZeroDivisionError:
    ...     print("We have an error in division")
    ... finally:
    ...     fobj.close()
    ...     print("Closing the file object.")
    ...
    We have an error in division
    Closing the file object.

In this example we are making sure that the file object we open, must get closed
in the `finally` clause.
