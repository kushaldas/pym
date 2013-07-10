

===============
Data Structures
===============

Python is having a few built-in data structure. If you are still wondering what is a data structure, then it is nothing a but a way to store data and the having particular methods to retrieve or manipulate it. We already saw lists before, now we will go in depth.

Lists
=====
::

    >>> a = [23, 45, 1, -3434, 43624356, 234]
    >>> a.append(45)
    >>> a
    [23, 45, 1, -3434, 43624356, 234, 45]

At first we created a list *a*. Then to add *45* at the end of the list we call *a.append(45)* method. You can see that *45* added at the end of the list. Sometimes it may require to insert data at any place within the list, for that we have *insert()* method.

::

    >>> a.insert(0, 1) # 1 added at the 0th position of the list
    >>> a
    [1, 23, 45, 1, -3434, 43624356, 234, 45]
    >>> a.insert(0, 111)
    >>> a
    [111, 1, 23, 45, 1, -3434, 43624356, 234, 45]

*count(s)* will return you number of times *s* is in the list. Here we are going to check how many times *45* is there in the list.

::

    >>> a.count(45)
    2

If you want to remove any particular value from the list you have to use *remove()* method.

::

    >>> a.remove(234)
    >>> a
    [111, 1, 23, 45, 1, -3434, 43624356, 45]

Now to reverse the whole list

::

    >>> a.reverse()
    >>> a
    [45, 43624356, -3434, 1, 45, 23, 1, 111]

We can store anything in the list, so first we are going to add another list  *b* in  *a*, then we will learn how to add the values of  *b* into  *a*.

::

    >>> b = [45, 56, 90]
    >>> a.append(b)
    >>> a
    [45, 43624356, -3434, 1, 45, 23, 1, 111, [45, 56, 90]]
    >>> a[-1]
    [45, 56, 90]
    >>> a.extend(b) #To add the values of b not the b itself
    >>> a
    [45, 43624356, -3434, 1, 45, 23, 1, 111, [45, 56, 90], 45, 56, 90]
    >>> a[-1]
    90

Above you can see how we used *a.extend()* method to extend the list. To sort any list we have *sort()* method.

::

    >>> a.sort()
    >>> a
    [-3434, 1, 1, 23, 45, 45, 45, 56, 90, 111, 43624356, [45, 56, 90]]

You can also delete element at any particular position of the list using the del keyword.

::

    >>> del a[-1]
    >>> a
    [-3434, 1, 1, 23, 45, 45, 45, 56, 90, 111, 43624356]

Using lists as stack and queue
==============================

Stacks are often known as LIFO (Last In First Out) structure. It means the data will enter into it at the end , and the last data will come out first. The easiest example can be of couple of marbles in an one side closed pipe. So if you want to take the marbles out of it you have to do that from the end where you entered the last marble. To achieve the same in code

::

    >>> a
    [1, 2, 3, 4, 5, 6]
    >>> a.pop()
    6
    >>> a.pop()
    5
    >>> a.pop()
    4
    >>> a.pop()
    3
    >>> a
    [1, 2]
    >>> a.append(34)
    >>> a
    [1, 2, 34]

We learned a new method above *pop()*. *pop(i)* will take out the ith data from the list.

In our daily life we have to encounter queues many times, like in ticket counters or in library or in the billing section of any supermarket. Queue is the data structure where you can append more data at the end and take out data from the beginning. That is why it is known as FIFO (First In First Out).

::

    >>> a = [1, 2, 3, 4, 5]
    >>> a.append(1)
    >>> a
    [1, 2, 3, 4, 5, 1]
    >>> a.pop(0)
    1
    >>> a.pop(0)
    2
    >>> a
    [3, 4, 5, 1]

To take out the first element of the list we are using *a.pop(0)*.

List Comprehensions
===================

List comprehensions provide a concise way to create lists. Each list comprehension consists of an expression followed by a for clause, then zero or more for or if clauses. The result will be a list resulting from evaluating the expression in the context of the for and if clauses which follow it.

For example if we want to make a list out of the square values of another list, then

::

    >>> a = [1, 2, 3]
    >>> [x ** 2 for x in a]
    [1, 4, 9]
    >>> z = [x + 1 for x in [x ** 2 for x in a]]
    >>> z
    [2, 5, 10]

Above in the second case we used two list comprehensions in a same line.

Tuples
======

Tuples are data separated by comma.

::

    >>> a = 'Fedora', 'Debian', 'Kubuntu', 'Pardus'
    >>> a
    ('Fedora', 'Debian', 'Kubuntu', 'Pardus')
    >>> a[1]
    'Debian'
    >>> for x in a:
    ...     print x,
    ...
    Fedora Debian Kubuntu Pardus

You can also unpack values of any tuple in to variables, like

::

    >>> divmod(15,2)
    (7, 1)
    >>> x, y = divmod(15,2)
    >>> x
    7
    >>> y
    1

Tuples are immutable, that means you can not del/add/edit any value inside the tuple. Here is another example

::

    >>> a = (1, 2, 3, 4)
    >>> del a[0]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object doesn't support item deletion

Above you can see python is giving error when we are trying to delete a value in the tuple.

To create a tuple which contains only one value you have to type a trailing comma.

::

    >>> a = (123)
    >>> a
    123
    >>> type(a)
    <type 'int'>
    >>> a = (123, ) #Look at the trailing comma
    >>> a
    (123,)
    >>> type(a)
    <type 'tuple'>

Using the built in function *type()* you can know the data type of any variable. Remember the *len()* function we used to find the length of any sequence ?

::

    >>> type(len)
    <type 'builtin_function_or_method'>

Sets
====

Sets are another type of data structure with no duplicate items. We can also mathematical set operations on sets.

::

    >>> a = set('abcthabcjwethddda')
    >>> a
    set(['a', 'c', 'b', 'e', 'd', 'h', 'j', 't', 'w'])

And some examples of the set operations

::

    >>> a = set('abracadabra')
    >>> b = set('alacazam')
    >>> a                                  # unique letters in a
    set(['a', 'r', 'b', 'c', 'd'])
    >>> a - b                              # letters in a but not in b
    set(['r', 'd', 'b'])
    >>> a | b                              # letters in either a or b
    set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
    >>> a & b                              # letters in both a and b
    set(['a', 'c'])
    >>> a ^ b                              # letters in a or b but not both
    set(['r', 'd', 'b', 'm', 'z', 'l'])

To add or pop values from a set

::

    >>> a
    set(['a', 'c', 'b', 'e', 'd', 'h', 'j', 'q', 't', 'w'])
    >>> a.add('p')
    >>> a
    set(['a', 'c', 'b', 'e', 'd', 'h', 'j', 'q', 'p', 't', 'w'])

Dictionaries
============

Dictionaries are unordered set of *key: value* pairs where keys are unique. We declare dictionaries using {} braces. We use dictionaries to store data for any particular key and then retrieve them.

::

    >>> data = {'kushal':'Fedora', 'kart_':'Debian', 'Jace':'Mac'}
    >>> data
    {'kushal': 'Fedora', 'Jace': 'Mac', 'kart_': 'Debian'}
    >>> data['kart_']
    'Debian'

We can add more data to it by simply

::

    >>> data['parthan'] = 'Ubuntu'
    >>> data
    {'kushal': 'Fedora', 'Jace': 'Mac', 'kart_': 'Debian', 'parthan': 'Ubuntu'}

To delete any particular *key:value* pair

::

    >>> del data['kushal']
    >>> data
    {'Jace': 'Mac', 'kart_': 'Debian', 'parthan': 'Ubuntu'

To check if any *key* is there in the dictionary or not you can use *in* keyword.

::

    >>> 'Soumya' in data
    False

You must remember that no mutable object can be a *key*, that means you can not use a *list* as a *key*.

*dict()* can create dictionaries from tuples of *key,value* pair.

::

    >>> dict((('Indian','Delhi'),('Bangladesh','Dhaka')))
    {'Indian': 'Delhi', 'Bangladesh': 'Dhaka'}

If you want to loop through a dict use *iteritems()* method.

::

    >>> data
    {'Kushal': 'Fedora', 'Jace': 'Mac', 'kart_': 'Debian', 'parthan': 'Ubuntu'}
    >>> for x, y in data.iteritems():
    ...     print "%s uses %s" % (x, y)
    ...
    Kushal uses Fedora
    Jace uses Mac
    kart_ uses Debian
    parthan uses Ubuntu

Many times it happens that we want to add more data to a value in a dictionary and if the key does not exists then we add some default value. You can do this efficiently using *dict.setdefault(key, default)*.
::

    >>> data = {}
    >>> data.setdefault('names', []).append('Ruby')
    >>> data
    {'names': ['Ruby']}
    >>> data.setdefault('names', []).append('Python')
    >>> data
    {'names': ['Ruby', 'Python']}
    >>> data.setdefault('names', []).append('C')
    >>> data
    {'names': ['Ruby', 'Python', 'C']}

When we try to get value for a key which does not exists we get *KeyError*. We can use *dict.get(key, default)* to get a default value when they key does not exists before.

::

    >>> data['foo']
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: 'foo'
    >>> data.get('foo', 0)
    0

If you want to loop through a list (or any sequence) and get iteration number at the same time you have to use *enumerate()*.

::

    >>> for i, j in enumerate(['a', 'b', 'c']):
    ...     print i, j
    ...
    0 a
    1 b
    2 c

You may also need to iterate through two sequences same time, for that use *zip()* function.

::

    >>> a = ['Pradeepto', 'Kushal']
    >>> b = ['OpenSUSE', 'Fedora']
    >>> for x, y in zip(a, b):
    ...     print "%s uses %s" % (x, y)
    ...
    Pradeepto uses OpenSUSE
    Kushal uses Fedora

students.py
===========

In this example , you have to take number of students as input , then ask marks for three subjects as 'Physics', 'Maths', 'History', if the total marks for any student is less 120 then print he failed, or else say passed.

::

    #!/usr/bin/env python
    n = int(raw_input("Enter the number of students:"))
    data = {} # here we will store the data
    languages = ('Physics', 'Maths', 'History') #all languages
    for i in range(0, n): #for the n number of students
        name = raw_input('Enter the name of the student %d: ' % (i + 1)) #Get the name of the student
        marks = []
        for x in languages:
            marks.append(int(raw_input('Enter marks of %s: ' % x))) #Get the marks for  languages
        data[name] = marks
    for x, y in data.iteritems():
        total =  sum(y)
        print "%s 's  total marks %d" % (x, total)
        if total < 120:
            print "%s failed :(" % x
        else:
            print "%s passed :)" % y

The output

::

    [kd@kdlappy book]$ ./students.py
    Enter the number of students:2
    Enter the name of the student 1: Babai
    Enter marks of Physics: 12
    Enter marks of Maths: 45
    Enter marks of History: 40
    Enter the name of the student 2: Tesla
    Enter marks of Physics: 99
    Enter marks of Maths: 98
    Enter marks of History: 99
    Babai 's  total marks 97
    Babai failed :(
    Tesla 's  total marks 296
    Tesla passed :)

matrixmul.py
============

In this example we will multiply two matrices. First we will take input the number of rows/columns in the matrix (here we assume we are using n x n matrix). Then values of the matrices.

::

    #!/usr/bin/env python
    n = int(raw_input("Enter the value of n: "))
    print "Enter values for the Matrix A"
    a = []
    for i in range(0, n):
        a.append([int(x) for x in raw_input("").split(" ")])
    print "Enter values for the Matrix B"
    b = []
    for i in range(0, n):
        b.append([int(x) for x in raw_input("").split(" ")])
    c = []
    for i in range(0, n):
        c.append([a[i][j] * b[j][i] for j in range(0,n)])
    print "After matrix multiplication"
    print "-" * 10 * n
    for x in c:
        for y in x:
            print "%5d" % y,
        print ""
    print "-" * 10 * n

The output

::

    [kd@kdlappy book]$ ./matrixmul.py
    Enter the value of n: 3
    Enter values for the Matrix A
    1 2 3
    4 5 6
    7 8 9
    Enter values for the Matrix B
    9 8 7
    6 5 4
    3 2 1
    After matrix multiplication
    ------------------------------
        9    12     9 
       32    25    12 
       49    32     9 
    ------------------------------

Here we have used list comprehensions couple of times. *[int(x) for x in raw_input("").split(" ")]* here first it takes the input as string by *raw_input()*, then split the result by " ", then for each value create one int. We are also using *[a[i][j] * b[j][i] for j in range(0,n)]* to get the resultant row in a single line.


