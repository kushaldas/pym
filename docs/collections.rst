

==================
Collections module
==================

In this chapter we will learn about a module called *Collections*. This module implements some nice data structures which will help you to solve various real life problems.

::

    >>> import collections

This is how you can import the module, now we will see the available classes which you can use.


.. index:: Counter

Counter
=======

*Counter* is a *dict* subclass which helps to count hashable objects. Inside it elements are stored as dictionary keys and counts are stored as values which can be zero or negative.

Below we will see one example where we will find occurrences of words in the Python LICENSE file.

Counter example
---------------

::

    >>> from collections import Counter
    >>> import re
    >>> path = '/usr/share/doc/python-2.7.3/LICENSE'
    >>> words = re.findall('\w+', open(path).read().lower())
    >>> Counter(words).most_common(10)
    [('2', 97), ('the', 80), ('or', 78), ('1', 76), ('of', 61), ('to', 50), ('and', 47), ('python', 46), ('psf', 44), ('in', 38)]

Counter objects has a method called *elements* which returns an iterator over elements repeating each as many times as its count. Elements are returned in arbitrary order.

::

    >>> c = Counter(a=4, b=2, c=0, d=-2)
    >>> list(c.elements())
    ['a', 'a', 'a', 'a', 'b', 'b']

*most_common* is a method which returns most common elements and their counts from the most common to the least.

::

    >>> Counter('abracadabra').most_common(3)
    [('a', 5), ('r', 2), ('b', 2)]

.. index:: defaultdict

defaultdict
===========

*defaultdict* is a dictionary like object which provides all methods provided by dictionary but takes first argument (default_factory) as default data type for the dictionary. Using defaultdict is faster than doing the same using *dict.set_default* method.

defaultdict example
-------------------

::
    >>> from collections import defaultdict
    >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    >>> d = defaultdict(list)
    >>> for k, v in s:
    ...     d[k].append(v)
    ...
    >>> d.items()
    dict_items([('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])])

In the example you can see even if the key is not there in the defaultdict object, it automatically creates an empty list. *list.append* then helps to append the value to the list.

.. index:: namedtuple

namedtuple
==========

Named tuples helps to have meaning of each position in a tuple and allow us to code with better readability and self-documenting code. You can use them in any place where you are using *tuples*. In the example we will create a namedtuple to show hold information for points.

Named tuple
-----------

::

    >>> from collections import namedtuple
    >>> Point = namedtuple('Point', ['x', 'y'])  # Defining the namedtuple
    >>> p = Point(10, y=20)  # Creating an object
    >>> p
    Point(x=10, y=20)
    >>> p.x + p.y
    30
    >>> p[0] + p[1]  # Accessing the values in normal way
    30
    >>> x, y = p     # Unpacking the tuple
    >>> x
    10
    >>> y
    20


