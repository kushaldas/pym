

====================================
Iterators, generators and decorators
====================================

In this chapter we will learn about iterators, generators and decorators.

Iterators
=========

Python iterator objects are required to support two methods while following the iterator
protocol.

*__iter__* returns the iterator object itself. This is used in *for*
and *in* statements.

*__next__* method returns the next value from the iterator. If there is no more items
to return then it should raise *StopIteration* exception.

::

    class Counter(object):
        def __init__(self, low, high):
            self.current = low
            self.high = high

        def __iter__(self):
            'Returns itself as an iterator object'
            return self

        def __next__(self):
            'Returns the next value till current is lower than high'
            if self.current > self.high:
                raise StopIteration
            else:
                self.current += 1
                return self.current - 1

Now we can use this iterator in our code.

::

    >>> c = Counter(5,10)
    >>> for i in c:
    ...   print(i, end=' ')
    ...
    5 6 7 8 9 10

Remember that an iterator object can be used only once. It means after it raises *StopIteration*
once, it will keep raising the same exception.

::

    >>> c = Counter(5,6)
    >>> next(c)
    5
    >>> next(c)
    6
    >>> next(c)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 11, in next
    StopIteration
    >>> next(c)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 11, in next
    StopIteration

Using the iterator in for loop example we saw, the following example tries to show the code
behind the scenes.

::

    >>> iterator = iter(c)
    >>> while True:
    ...     try:
    ...         x = iterator.__next__()
    ...         print(x, end=' ')
    ...     except StopIteration as e:
    ...         break
    ...
    5 6 7 8 9 10

Generators
==========

In this section we learn about Python generators. They were introduced in Python 2.3. It
is an easier way to create iterators using a keyword *yield* from a function.

::

    >>> def my_generator():
    ...     print("Inside my generator")
    ...     yield 'a'
    ...     yield 'b'
    ...     yield 'c'
    ...
    >>> my_generator()
    <generator object my_generator at 0x7fbcfa0a6aa0>

In the above example we create a simple generator using the yield statements. We can use it
in a for loop just like we use any other iterators.

::

    >>> for char in my_generator():
    ...     print(char)
    ...
    Inside my generator
    a
    b
    c

In the next example we will create the same Counter class using a generator function and use it
in a for loop.

::

    def counter_generator(low, high):
        while low <= high:
           yield low
           low += 1

    >>> for i in counter_generator(5,10):
    ...     print(i, end=' ')
    ...
    5 6 7 8 9 10

Inside the while loop when it reaches to the *yield* statement, the value of low is returned
and the generator state is suspended. During the second *next* call the generator resumed where
it freeze-ed before and then the value of *low* is increased by one. It continues with the
while loop and comes to the *yield* statement again.

When you call an generator function it returns a \*generator* object. If you call \*dir*
on this object you will find that it contains *__iter__* and \*__next__* methods among the
other methods.

::

    >>> c = counter_generator(5,10)
    >>> dir(c)
    ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__iter__',
 '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'close', 'gi_code', 'gi_frame', 'gi_running', 'send', 'throw']

We mostly use generators for laze evaluations. This way generators become a good approach
to work with lots of data. If you don't want to load all the data in the memory, you can use
a generator which will pass you each piece of data at a time.

One of the biggest example of such example is *os.path.walk()* function which uses a callback
function and current *os.walk* generator. Using the generator implementation saves memory.

We can have generators which produces infinite values. The following is a one such example.

::

    >>> def infinite_generator(start=0):
    ...     while True:
    ...         yield start
    ...         start += 1
    ...
    >>> for num in infinite_generator(4):
    ...     print(num, end=' ')
    ...     if num > 20:
    ...         break
    ...
    4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21

If we go back to the example of *my_generator* we will find one feature of generators.
They are not re-usable.

::

    >>> g = my_generator()
    >>> for c in g:
    ...     print(c)
    ...
    Inside my generator
    a
    b
    c
    >>> for c in g:
    ...     print(c)
    ...

One way to create a reusable generator is Object based generators which does not hold any state. Any class with a *__iter__* method which yields data can be used as a object generator.
In the following example we will recreate out counter generator.

::

    >>> class Counter(object):
    ...     def __init__(self, low, high):
    ...         self.low = low
    ...         self.high = high
    ...     def __iter__(self):
    ...          counter = self.low
    ...          while self.high >= counter:
    ...              yield counter
    ...              counter += 1
    ...
    >>> gobj = Counter(5, 10)
    >>> for num in gobj:
    ...     print(num, end=' ')
    ...
    5 6 7 8 9 10
    >>> for num in gobj:
    ...     print(num, end=' ')
    ...
    5 6 7 8 9 10

Generator expressions
=====================

In this section we will learn about generator expressions which is a  high
performance, memory efficient generalization of list comprehensions and generators.

For example we will try to sum the squares of all numbers from 1 to 9.

::

    >>> sum([x*x for x in range(1,10)])

The example actually first creates a list of the square values in memory and then it
iterates over it and finally after sum it frees the memory. You can understand the memory
usage in case of a big list.

We can save memory usage by using a generator expression.

::

    sum(x*x for x in range(1,10))

The syntax of generator expression says that always needs to be directly inside a set of parentheses and cannot have a comma on either side. Which basically means both the examples below are valid generator expression usage example.

::

    >>> sum(x*x for x in range(1,10))
    285
    >>> g = (x*x for x in range(1,10))
    >>> g
    <generator object <genexpr> at 0x7fc559516b90>

We can have chaining of generators or generator expressions. In the following
example we will read the file \*/var/log/cron* and will find if any particular
job (in the example we are searching for anacron) is running successfully or not.

We can do the same using a shell command *tail -f /var/log/cron |grep anacron*

::

    >>> jobtext = 'anacron'
    >>> all_lines = (line for line in open('/var/log/cron', 'r') )
    >>> job = ( line for line in all_lines if line.find(jobtext) != -1)
    >>> text = next(job)
    >>> text
    "May  6 12:17:15 dhcp193-104 anacron[23052]: Job `cron.daily' terminated\n"
    >>> text = next(job)
    >>> text
    'May  6 12:17:15 dhcp193-104 anacron[23052]: Normal exit (1 job run)\n'
    >>> text = next(job)
    >>> text
    'May  6 13:01:01 dhcp193-104 run-parts(/etc/cron.hourly)[25907]: starting 0anacron\n'

You can write a for loop to the lines.

Closures
========

Closures are nothing but functions that are returned by another function. We use
closures to remove code duplication. In the following example we create
a simple closure for adding numbers.

::

    >>> def add_number(num):
    ...     def adder(number):
    ...         'adder is a closure'
    ...         return num + number
    ...     return adder
    ...
    >>> a_10 = add_number(10)
    >>> a_10(21)
    31
    >>> a_10(34)
    44
    >>> a_5 = add_number(5)
    >>> a_5(3)
    8

*adder* is a closure which adds a given number to a pre-defined one.

Decorators
==========

Decorator is way to dynamically add some new behavior to some objects. We achieve
the same in Python by using closures.

In the example we will create a simple example which will print some statement before
and after the execution of a function.

::

    >>> def my_decorator(func):
    ...     def wrapper(*args, **kwargs):
    ...         print("Before call")
    ...         result = func(*args, **kwargs)
    ...         print("After call")
    ...         return result
    ...     return wrapper
    ...
    >>> @my_decorator
    ... def add(a, b):
    ...     "Our add function"
    ...     return a + b
    ...
    >>> add(1, 3)
    Before call
    After call
    4
