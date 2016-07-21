

=========================
Operators and expressions
=========================

In Python most of the lines you will write will be expressions. Expressions are made of operators and operands. An expression is like *2 + 3* .

Operators
=========

Operators are the symbols which tells the Python interpreter to do some mathematical or logical operation. Few basic examples of mathematical operators are given below:

::

    >>> 2 + 3
    5
    >>> 23 - 3
    20
    >>> 22.0 / 12
    1.8333333333333333

To get floating result you need to the division using any of operand as floating number. To do modulo operation use % operator

::

    >>> 14 % 3
    2

Example of integer arithmetic
=============================

The code

::

    #!/usr/bin/env python3
    days = int(input("Enter days: "))
    months = days / 30
    days = days % 30
    print("Months = %d Days = %d" % (months, days))

The output

::

    $ ./integer.py
    Enter days: 265
    Months = 8 Days = 25

In the first line I am taking the input of days, then getting the months and days and at last printing them. You can do it in a easy way

::

    #!/usr/bin/env python3
    days = int(input("Enter days: "))
    print("Months = %d Days = %d" % (divmod(days, 30)))

The divmod(num1, num2) function returns two values , first is the division of num1 and num2 and in second the modulo of num1 and num2.

Relational Operators
====================

You can use the following operators as relational operators

Relational Operators
--------------------

+----------+-----------------------------+
| Operator | Meaning                     |
+----------+-----------------------------+
| \<       | Is less than                |
+----------+-----------------------------+
| <=       | Is less than or equal to    |
+----------+-----------------------------+
| >        | Is greater than             |
+----------+-----------------------------+
| >=       | Is greater than or equal to |
+----------+-----------------------------+
| \=\=     | Is equal to                 |
+----------+-----------------------------+
| !=       | Is not equal to             |
+----------+-----------------------------+

Some examples

::

    >>> 1 < 2
    True
    >>> 3 > 34
    False
    >>> 23 == 45
    False
    >>> 34 != 323
    True

*//* operator gives the floor division result

::

    >>> 4.0 // 3
    1.0
    >>> 4.0 / 3
    1.3333333333333333

Logical Operators
=================

To do logical AND , OR we use *and* ,*or* keywords. *x and y* returns *False* if *x* is *False* else it returns evaluation of *y*. If *x* is *True*, it returns *True*.

::

    >>> 1 and 4
    4
    >>> 1 or 4
    1
    >>> -1 or 4
    -1
    >>> 0 or 4
    4

Shorthand Operator
==================

*x op = expression* is the syntax for shorthand operators. It will be evaluated like *x = x op expression* , Few examples are

::

    >>> a = 12
    >>> a += 13
    >>> a
    25
    >>> a /= 3
    >>> a
    8.333333333333334
    >>> a += (26 * 32)
    >>> a
    840.3333333333334

shorthand.py example

.. code-block:: python

    #!/usr/bin/env python3
    N = 100
    a = 2
    while a < N:
        print("%d" % a)
        a *= a

The output

::

    $ ./shorthand.py
    2
    4
    16

Expressions
===========

Generally while writing expressions we put spaces before and after every operator so that the code becomes clearer to read, like

::

    a = 234 * (45 - 56.0 / 34)

One example code used to show expressions

::

    #!/usr/bin/env python3
    a = 9
    b = 12
    c = 3
    x = a - b / 3 + c * 2 - 1
    y = a - b / (3 + c) * (2 - 1)
    z = a - (b / (3 + c) * 2) - 1
    print("X = ", x)
    print("Y = ", y)
    print("Z = ", z)

The output

::

    $ ./evaluationexp.py
    X =  10
    Y =  7
    Z =  4

At first *x* is being calculated. The steps are like this

::

    9 - 12 / 3 + 3 * 2 -1
    9 - 4 + 3 * 2 - 1
    9 - 4 + 6 - 1
    5 + 6 - 1
    11 - 1
    10

Now for *y* and *z* we have parentheses, so the expressions evaluated in different way. Do the calculation yourself to check them.

Type Conversions
================

We have to do the type conversions manually. Like
::

    float(string) -> float value
    int(string) -> integer value
    str(integer) or str(float) -> string representation
    >>> a = 8.126768
    >>> str(a)
    '8.126768'

evaluateequ.py
==============

This is a program to evaluate 1/x+1/(x+1)+1/(x+2)+ ... +1/n series upto n, in our case x = 1 and n =10

.. code-block:: python

    #!/usr/bin/env python3
    sum = 0.0
    for i in range(1, 11):
        sum += 1.0 / i
        print("%2d %6.4f" % (i , sum))

The output

::

    $ ./evaluateequ.py
    1 1.0000
    2 1.5000
    3 1.8333
    4 2.0833
    5 2.2833
    6 2.4500
    7 2.5929
    8 2.7179
    9 2.8290
    10 2.9290

In the line *sum += 1.0 / i* what is actually happening is *sum = sum + 1.0 / i*.

quadraticequation.py
====================

This is a program to evaluate the quadratic equation

::

    #!/usr/bin/env python3
    import math
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))
    d = b * b - 4 * a * c
    if d < 0:
        print("ROOTS are imaginary")
    else:
        root1 = (-b + math.sqrt(d)) / (2.0 * a)
        root2 = (-b - math.sqrt(d)) / (2.0 * a)
        print("Root 1 = ", root1)
        print("Root 2 = ", root2)

salesmansalary.py
=================

In this example we are going to calculate the salary of a camera salesman. His basic salary is 1500, for every camera he will sell he will get 200 and the commission on the month's sale is 2 %. The input will be number of cameras sold and total price of the cameras.

::

    #!/usr/bin/env python3
    basic_salary = 1500
    bonus_rate = 200
    commision_rate = 0.02
    numberofcamera = int(input("Enter the number of inputs sold: "))
    price = float(input("Enter the total prices: "))
    bonus = (bonus_rate * numberofcamera)
    commision = (commision_rate * numberofcamera * price)
    print("Bonus        = %6.2f" % bonus)
    print("Commision    = %6.2f" % commision)
    print("Gross salary = %6.2f" % (basic_salary + bonus + commision))

The output

::

    $ ./salesmansalary.py
    Enter the number of inputs sold: 5
    Enter the total prices: 20450
    Bonus        = 1000.00
    Commision    = 2045.00
    Gross salary = 4545.00
