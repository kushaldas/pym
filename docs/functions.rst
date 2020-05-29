
=========
Functions
=========

Reusing the same code is required many times within a same program. Functions
help us to do so. We write the things we have to do repeatedly in a function
then call it where ever required. We already saw build in functions like
*len()*, *divmod()*.

Defining a function
===================

We use *def* keyword to define a function. General syntax is like

::

    def functionname(params):
        statement1
        statement2

Let us write a function which will take two integers as input and then return
the sum.

::

    >>> def sum(a, b):
    ...     return a + b

In the second line with the *return* keyword, we are sending back the value of
*a + b* to the caller. You must call it like

::

    >>> res = sum(234234, 34453546464)
    >>> res
    34453780698L

Remember the palindrome program we wrote in the last chapter. Let us write a
function which will check if a given string is palindrome or not, then return
*True* or *False*.

::

    #!/usr/bin/env python3


    def palindrome(s):
        return s == s[::-1]


    if __name__ == "__main__":
        s = input("Enter a string: ")
        if palindrome(s):
            print("Yay a palindrome")
        else:
            print("Oh no, not a palindrome")


Now run the code :)

Local and global variables
==========================

To understand local and global variables we will go through two examples.

::

    #!/usr/bin/env python


    def change(a):
        a = 90
        print(f"Inside of the change function {a}")


    a = 9
    print(f"Before the function call {a}")
    change(a)
    print(f"After the function call {a}")


The output
::

    $ ./local.py
    Before the function call  9
    Inside of the change function 90
    After the function call  9

First we are assigning *9* to *a*, then calling change function, inside of that
we are assigning *90* to *a* and printing *a*. After the function call we are
again printing the value of *a*. When we are writing *a = 90* inside the
function, it is actually creating a new variable called *a*, which is only
available inside the function and will be destroyed after the function finished.
So though the name is same for the variable *a* but they are different in and
out side of the function.

::

    #!/usr/bin/env python3
    def change(b):
        global a
        a = 90
        print(a)
    a = 9
    print("Before the function call ", a)
    print("inside change function", end=' ')
    change(a)
    print("After the function call ", a)

Here by using global keyword we are telling that *a* is globally defined, so
when we are changing a's value inside the function it is actually changing for
the *a* outside of the function also.

The output
::

    $ ./local.py
    Before the function call  9
    inside change function 90
    After the function call  90

Default argument value
======================

In a function variables may have default argument values, that means if we don't
give any value for that particular variable it will be assigned automatically.

::

    >>> def test(a , b=-99):
    ...     if a > b:
    ...         return True
    ...     else:
    ...         return False

In the above example we have written *b = -99* in the function parameter list.
That means if no value for *b* is given then b's value is *-99*. This is a very
simple example of default arguments. You can test the code by

::

    >>> test(12, 23)
    False
    >>> test(12)
    True

.. important:: Important

   Remember that you can not have an argument without default argument if you already have one argument with default values before it. Like *f(a, b=90, c)* is illegal as *b* is having a default value but after that *c* is not having any default value.

Also remember that default value is evaluated only once, so if you have any
mutable object like list it will make a difference. See the next example

::

    >>> def f(a, data=[]):
    ...     data.append(a)
    ...     return data
    ...
    >>> print(f(1))
    [1]
    >>> print(f(2))
    [1, 2]
    >>> print(f(3))
    [1, 2, 3]

To avoid this you can write more idiomatic Python, like the following

::

    >>> def f(a, data=None):
    ...     if data is None:
    ...         data = []
    ...     data.append(a)
    ...     return data
    ...
    >>> print(f(1))
    [1]
    >>> print(f(2))
    [2]

.. note:: To understand more read `this url <https://docs.python.org/3/tutorial/controlflow.html#default-argument-values>`_.

Keyword arguments
=================
::

    >>> def func(a, b=5, c=10):
    ...     print('a is', a, 'and b is', b, 'and c is', c)
    ...
    >>> func(12, 24)
    a is 12 and b is 24 and c is 10
    >>> func(12, c = 24)
    a is 12 and b is 5 and c is 24
    >>> func(b=12, c = 24, a = -1)
    a is -1 and b is 12 and c is 24

In the above example you can see we are calling the function with variable
names, like *func(12, c = 24)*, by that we are assigning *24* to *c* and *b* is
getting its default value. Also remember that you can not have without keyword
based argument after a keyword based argument. like

::

    >>> def func(a, b=13, v):
    ...     print(a, b, v)
    ...
    File "<stdin>", line 1
    SyntaxError: non-default argument follows default argument

Keyword only argument
=====================

We can also mark the arguments of function as keyword only. That way while
calling the function, the user will be forced to use correct keyword for each
parameter.

::

    >>> def hello(*, name='User'):
    ...     print("Hello %s" % name)
    ...
    >>> hello('Kushal')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: hello() takes 0 positional arguments but 1 was given
    >>> hello(name='Kushal')
    Hello Kushal


.. note:: To learn more please read `PEP-3102 <https://www.python.org/dev/peps/pep-3102/>`_.


Positional only argument
=========================

From Python3.8, we can also mark any function to have only positional arguments. Write
`/` at the end of all positional arguments in the function definition to have this feature.


::

    >>> def add(a, b, /):
    ...   return a + b
    ... 
    >>> add(2, 3)
    5
    >>> add(a=2, b=3)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: add() got some positional-only arguments passed as keyword arguments: 'a, b'


You can see that when we tried to call the `add` with keyword arguments, it raised a `TypeError`.


Docstrings
==========

In Python we use docstrings to explain how to use the code, it will be useful in
interactive mode and to create auto-documentation. Below we see an example of
the docstring for a function called *longest_side*.


::

    #!/usr/bin/env python3
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
        print(longest_side(4, 5))

We will learn more on docstrings in reStructuredText chapter.


Higher-order function
======================

Higher-order function or a functor is a function which does at least one of the
following step inside:

    - Takes one or more functions as argument.
    - Returns another function as output.

In Python any function can act as higher order function.
::

    >>> def high(func, value):
    ...     return func(value)
    ...
    >>> lst = high(dir, int)
    >>> print(lst[-3:])
    ['imag', 'numerator', 'real']
    >>> print(lst)


Let us look at another example. We will create a function, which in turn
returns another function to add 5 to the given argument.

::

    def givemefive():
        def add5(x):
            return x + 5
        return add5

    >>> myadder = givemefive()
    >>> print(myadder(10))
    15
    >>> print(type(myadder))
    <class 'function'>

Here when we call `givemefive`, it is actually returning the function `add5`,
and storing into `myadder`. Finally when we call the `myadder`, it adds 5 to
the given argument, and returns it. We also printed the `type` of `myadder`

::

    def givemeadder(num):
        def internal(x):
            return num + x
        return internal

    >>> add10 = givemeadder(10)
    >>> print(add10(20))
    30

In this example the `internal` function is using the `x` variable from the
outer scope. This is also known as `closure` where the function is using the
environment enclosed. If we need a new function which will add 100 to the given
number, we can do it easily like this.

::

    add_big = givemeadder(100)
    >>> print(add_big(1))
    101

.. note:: To know more read `this link <http://docs.python.org/3/faq/programming.html#how-do-you-make-a-higher-order-function-in-python>`_.

map 
====

`map` is a very useful class in python. It takes one function
and an iterator as input and then applies the function on each value of the
iterator and returns an iterator.

Example::

    >>> lst = [1, 2, 3, 4, 5]
    >>> def square(num):
    ...     "Returns the square of a given number."
    ...     return num * num
    ...
    >>> print(list(map(square, lst)))
    [1, 4, 9, 16, 25]

In Python2, `map` was a function and used to return list.


Parameters and arguments
=========================

`Parameters` are names defined in a function definition, and `arguments` are the
actual values passed that function call.

::

    def hello(name, age):
        return f"Hello {name}, you are {age} years old"

    hello("kushal", 90)

In the above example, `name` and `age` are the parameters of the `hello`, and `kushal` and `90` are
the arguments passed to the function.


*args and **kwargs in function definition 
=========================================

There are times when we don't know the number of arguments before hand. There
can be any number of positional or keyword arguments passed to the function.
This is where we use `*args` and `**kwargs` in the function.


::

    def unknown(*args, **kwargs):
        print(f"We received {len(args)} positional arguments. And they are:")
        for arg in args:
            print(arg, end= " ")
        print("")
        print(f"We received {len(kwargs)} keyword arguments. And they are:")
        for k, v in kwargs.items():
            print(f"key={k} and value={v}")
        
        
    unknown(30, 90, "kushal", lang="python", editor="vim")

    We received 3 positional arguments. And they are:
    30 90 kushal 
    We received 2 keyword arguments. And they are:
    key=lang and value=python
    key=editor and value=vim

This is really helpful when you are writing code which will take another
function as input, and you don't know about parameters of that function before
hand.  We will see more examples later in this book.


HOWTO Write a function
========================

Watch `this talk <https://www.youtube.com/watch?v=rrBJVMyD-Gs>`_ by Jack
Diederich at PyCon US 2018 to learn more about how to write clean Python
functions and many other tips.

