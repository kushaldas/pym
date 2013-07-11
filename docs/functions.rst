

=========
Functions
=========

Reusing the same code is required many times within a same program. Functions help us to do so. We write the things we have to do repeatedly in a function then call it where ever required. We already saw build in functions like *len()*, *divmod()*.

Defining a function
===================

We use *def* keyword to define a function. General syntax is like

::

    def functionname(params):
        statement1
        statement2

Let us write a function which will take two integers as input and then return the sum.

::

    >>> def sum(a, b):
    ...     return a + b

In the second line with the *return* keyword, we are sending back the value of *a + b* to the caller. You must call it like

::

    >>> res = sum(234234, 34453546464)
    >>> res
    34453780698L

Remember the palindrome program we wrote in the last chapter. Let us write a function which will check if a given string is palindrome or not, then return *True* or *False*.

::

    #!/usr/bin/env python
    def palindrome(s):
        return s == s[::-1]
    if __name__ == '__main__':
        s = raw_input("Enter a string: ")
        if palindrome(s):
            print "Yay a palindrome"
        else:
            print "Oh no, not a palindrome"

Now run the code :)

Local and global variables
==========================

To understand local and global variables we will go through two examples.

::

    #!/usr/bin/env python
    def change(b):
        a = 90
        print a
    a = 9
    print "Before the function call ", a
    print "inside change function",
    change(a)
    print "After the function call ", a]

The output
::

    $ ./local.py
    Before the function call  9
    inside change function 90
    After the function call  9

First we are assigning *9* to *a*, then calling change function, inside of that we are assigning *90* to *a* and printing *a*. After the function call we are again printing the value of *a*. When we are writing *a = 90* inside the function, it is actually creating a new variable called *a*, which is only available inside the function and will be destroyed after the function finished. So though the name is same for the variable *a* but they are different in and out side of the function.

::

    #!/usr/bin/env python
    def change(b):
        global a
        a = 90
        print a
    a = 9
    print "Before the function call ", a
    print "inside change function",
    change(a)
    print "After the function call ", a

Here by using global keyword we are telling that *a* is globally defined, so when we are changing a's value inside the function it is actually changing for the *a* outside of the function also.

Default argument value
======================

In a function variables may have default argument values, that means if we don't give any value for that particular variable it will assigned automatically.

::

    >>> def test(a , b = -99):
    ...     if a > b:
    ...         return True
    ...     else:
    ...         return False

In the above example we have written *b = -99* in the function parameter list. That means of no value for *b* is given then b's value is *-99*. This is a very simple example of default arguments. You can test the code by

::

    >>> test(12, 23)
    False
    >>> test(12)
    True

.. important:: Important
   ---------
   Remember that you can not have an argument without default argument if you already have one argument with default values before it. Like *f(a, b=90, c)* is illegal as *b* is having a default value but after that *c* is not having any default value.

Also remember that default value is evaluated only once, so if you have any mutable object like list it will make a difference. See the next example

::

    >>> def f(a, data=[]):
    ...     data.append(a)
    ...     return data
    ...
    >>> print f(1)
    [1]
    >>> print f(2)
    [1, 2]
    >>> print f(3)
    [1, 2, 3]

To avoid this you can write more idiomatic Python, like the following

::

    >>> def f(a, data=None):
    ...     if data is None:
    ...         data = []
    ...         data.append(a)
    ...         return data
    ...
    >>> print f(1)
    [1]
    >>> print f(2)
    [2]

.. note:: To understand more read `this link <http://docs.python.org/2/tutorial/controlflow.html#default-argument-values>`_.

Keyword arguments
=================
::

    >>> def func(a, b=5, c=10):
    ...     print 'a is', a, 'and b is', b, 'and c is', c
    ...
    >>> func(12, 24)
    a is 12 and b is 24 and c is 10
    >>> func(12, c = 24)
    a is 12 and b is 5 and c is 24
    >>> func(b=12, c = 24, a = -1)
    a is -1 and b is 12 and c is 24

In the above example you can see we are calling the function with variable names, like *func(12, c = 24)*, by that we are assigning *24* to *c* and *b* is getting its default value. Also remember that you can not have without keyword based argument after a keyword based argument. like

::

    >>> def func(a, b=13, v):
    ...     print a, b, v
    ...
    File "<stdin>", line 1
    SyntaxError: non-default argument follows default argument

Docstrings
==========
Docstrings in Python

In Python we use docstrings to explain how to use the code, it will be useful in interactive mode and to create auto-documentation. Below we see an example of the docstring for a function called *longest_side*.


::

    #!/usr/bin/env python
    import math

    def longest_side(a, b):
        """
        Function to find the length of the longest side of a right triangle.

        :arg a: Side a of the triangle
        :arg b: Side b of the triangle

        :return: Length of the longest side c as float
        """
        return math.sqrt(a*a + b*b)

    if __name__ == '__main__':
        print longest_side(4, 5)

We will learn more on docstrings in reStructuredText chapter.


