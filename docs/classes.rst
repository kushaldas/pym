

=====
Class
=====

Classes and objects are part of programming idea also known as `Object-oriented
programming <https://en.wikipedia.org/wiki/Object-oriented_programming>`_. Here
the data, and functions working on the data stays together (we call those
functions as methods in the objects). `Simula
<https://en.wikipedia.org/wiki/Object-oriented_programming#History>`_ is the
first language which featured these ideas. `Java` and `C++` are two most known
object oriented programming languages in the schools.



Your first class
================

.. index:: Class

Before writing your first class, you should know the syntax. We define a class in the following way.

::

    class nameoftheclass(parent_class):
        statement1
        statement2
        statement3

In the statements you can write any Python statement, you can define functions (which we call methods of a class).

::

    >>> class MyClass(object):
    ...     a = 90
    ...     b = 88
    ...
    >>> p = MyClass()
    >>> p
    <__main__.MyClass instance at 0xb7c8aa6c>

.. index:: dir

In the above example you can see first we are declaring a class called MyClass, writing some random statements inside that class. After the class definition, we are creating an *object* p of the *class* MyClass. If you do a dir on that

::

    >>> dir(p)
    ['__doc__', '__module__', 'a', 'b']

you can see the variables *a* and *b* inside it.

.. index:: __init__

__init__ method
===============

__init__ is a special method in Python classes, it is the constructor method for a class. In the following example you can see how to use it.
::

    class Student(object):
        """
        Returns a ```Student``` object with the given name, branch and year.

        """
        def __init__(self, name, branch, year):
                self.name = name
                self.branch = branch
                self.year = year
                print("A student object is created.")

        def print_details(self):
            """
            Prints the details of the student.
            """
            print("Name:", self.name)
            print("Branch:", self.branch)
            print("Year:", self.year)



__init__ is called when ever an object of the class is constructed. That means
when ever we will create a student object we will see the message "A student
object is created" in the prompt. You can see the first argument to the method
is *self*. It is a special variable which points to the current object (like
`this` in C++). The object is passed implicitly to every method available in
it, but we have to get it explicitly in every method while writing the
methods. Example shown below. Remember to declare all the possible attributes
in the *__init__* method itself. Even if you are not using them right away,
you can always assign them as *None*.

::

    >>> std1 = Student()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: __init__() takes exactly 4 arguments (1 given)
    >>> std1 = Student('Kushal','CSE','2005')
    A student object is created

In this example at first we tried to create a Student object without passing any argument and Python interpreter complained that it takes exactly 4 arguments but received only one (self). Then we created an object with proper argument values and from the message printed, one can easily understand that *__init__* method was called as the constructor method.

Now we are going to call *print_details()* method.

::

    >>> std1.print_details()
    Name: Kushal
    Branch: CSE
    Year: 2005


.. note:: *__init__* is pronounced as dunder init, all functions with double underscore in the front and end
         is pronounced in this way. Example: dunder str or dunder repr.


Unique class level variables
=============================

All the values stored in the instance via `self.` are data inside of an
instance. Each instance of the class can have different values for given
attribute (anything we access via . is also known as attribute). But, when we
define an variable in the class level, that is same accross all objects. In
the following example, we define a class called `Point`, and we also have a
special class level variable called `style` in it. After we create 2 objects
of type `Point`, we can see that both has the same `class` attribute `style`
and changing in the class level also changes in the all objects.


::

    class Point:
        style="fun"

        def __init__(self, x, y):
            self.x = x
            self.y = y

    p1 = Point(10, 10)
    p2 = Point(100, 100)
    for p in [p1, p2]:
        print(f"Object {p} has style value= {p.style}")

    Point.style = "work"
    for p in [p1, p2]:
        print(f"Object {p} has style value= {p.style}")

Output::

    Object <__main__.Point object at 0x10de37210> has style value= fun
    Object <__main__.Point object at 0x10de0bb50> has style value= fun
    Object <__main__.Point object at 0x10de37210> has style value= work
    Object <__main__.Point object at 0x10de0bb50> has style value= work


__repr__ method
=================

`__repr__` is a special method used by the `print` function to show the
representation of an object. We can use the same to make our `Point` object
look better as print output.

::


    class Point:
        style="fun"

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"<Point x={self.x} y={self.y}>"

    p1 = Point(10, 10)
    p2 = Point(100, 100)
    for p in [p1, p2]:
        print(f"Object {p}")

The output::

        Object <Point x=10 y=10>
        Object <Point x=100 y=100>



.. index:: Inheritance

Inheritance
===========

In general we human beings always know about inheritance. In programming it is
almost the same. When a class inherits another class it inherits all features
(like variables and methods) of the parent class. This helps in reusing codes.

In the next example we first create a class called Person and create two
sub-classes Student and Teacher. As both of the classes are inherited from
Person class they will have all methods of Person and will have new methods and
variables for their own purpose.

student_teacher.py
-------------------
::

    #!/usr/bin/env python3

    class Person(object):
        """
        Returns a ```Person``` object with given name.

        """
        def __init__(self, name):
            self.name = name

        def get_details(self):
            "Returns a string containing name of the person"
            return self.name


    class Student(Person):
        """
        Returns a ```Student``` object, takes 3 arguments, name, branch, year.

        """
        def __init__(self, name, branch, year):
            super().__init__(name)
            self.branch = branch
            self.year = year

        def get_details(self):
            "Returns a string containing student's details."
            return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)


    class Teacher(Person):
        """
        Returns a ```Teacher``` object, takes a list of strings (list of papers) as
        argument.
        """
        def __init__(self, name, papers):
            super().__init__(name)
            self.papers = papers

        def get_details(self):
            return "%s teaches %s" % (self.name, ','.join(self.papers))


    person1 = Person('Sachin')
    student1 = Student('Kushal', 'CSE', 2005)
    teacher1 = Teacher('Prashad', ['C', 'C++'])

    print(person1.get_details())
    print(student1.get_details())
    print(teacher1.get_details())

The output:

::

    $ ./student_teacher.py
    Sachin
    Kushal studies CSE and is in 2005 year.
    Prashad teaches C,C++

In this example you can see how we called the __init__ method of the parent
class using the `super()` in both Student and Teacher classes' __init__ method.
We also reimplemented *get_details()* method of Person class in both Student
and Teacher class. So, when we are calling *get_details()* method on the
teacher1 object it returns based on the object itself (which is of teacher
class) and when we call *get_details()* on the student1 or person1 object it
returns based on *get_details()* method implemented in it's own class.


When a class inherites another class, the child class is also known as the
instance of the parent class. Here is an example based on the above class.

```Python
isinstance(student1, Person)
True
```

Multiple Inheritance
====================

One class can inherit more than one classes. It gets access to all methods and variables of the parent classes. The general syntax is:

::

    class MyClass(Parentclass1, Parentclass2,...):
        def __init__(self):
            Parentclass1.__init__(self)
            Parentclass2.__init__(self)
            ...
            ...

Encapsulation in Python
========================

Encapsulation is a way to provide details on how a data can be accessed. In
Python we have encapsulation as a programming style, which is different than
many other programming languages. For example, we use a leading `_` before any
variable name to tell that it is private. This way if the developer wants, they
can have a different variable with similar name in the child class.


::

    class Person():
        """
        Returns a ```Person``` object with given name.

        """
        def __init__(self, name):
            self._name = name

    def get_details(self):
        "Returns a string containing name of the person"
        return self._name


    class Child(Person):
        def __init__(self, name):
            super().__init__(name)

        def tell(self):
            print(f"The name is {self._name}")

    c = Child("kushal")
    c.tell()

The output::

    The name is kushal

You can see that we can still access the `_name` attribute. But, we are letting
the developer know that `_name` is a private attribute. If you want to make
sure that the attribute can not be accessed directly in the child class, you
can use `__` in front of the attribute name. It uses something called `name
mangling <https://docs.python.org/3/tutorial/classes.html#private-variables>_`.




Deleting an object
==================

As we already know how to create an object, now we are going to see how to delete an Python object. We use *del* for this.

::

    >>> s = "I love you"
    >>> del s
    >>> s
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 's' is not defined

*del* actually decreases reference count by one. When the reference count of an object becomes zero the garbage collector will delete that object.


Getters and setters in Python
==============================

One simple answer, don't. If you are coming from other languages (read Java), you will be tempted
to use getters or setters in all your classes. Please don't. Just use the attributes directly.
The following shows a direct example.
::

    >>> class Student(object):
    ...     def __init__(self, name):
    ...         self.name = name
    ...
    >>> std = Student("Kushal Das")
    >>> print(std.name)
    Kushal Das
    >>> std.name = "Python"
    >>> print(std.name)
    Python

.. index:: Property

Properties
===========

If you want more fine tuned control over data attribute access, then you can use properties.
In the following example of a bank account, we will make sure that no one can set the
money value to negative and also a property called *inr* will give us the INR values of
the dollars in the account.
::

    #!/usr/bin/env python3

    class Account(object):
        """The Account class,
        The amount is in dollars.
        """
        def __init__(self, rate):
            self.__amt = 0
            self.rate = rate

        @property
        def amount(self):
            "The amount of money in the account"
            return self.__amt

        @property
        def inr(self):
            "Gives the money in INR value."
            return self.__amt * self.rate

        @amount.setter
        def amount(self, value):
            if value < 0:
                print("Sorry, no negative amount in the account.")
                return
            self.__amt = value

    if __name__ == '__main__':
        acc = Account(rate=61) # Based on today's value of INR :(
        acc.amount = 20
        print("Dollar amount:", acc.amount)
        print("In INR:", acc.inr)
        acc.amount = -100
        print("Dollar amount:", acc.amount)


Output:
::

    $ python property.py
    Dollar amount: 20
    In INR: 1220
    Sorry, no negative amount in the account.
    Dollar amount: 20


Special dunder methods in classes
==================================

Below, we will see some special dunder methods (the methods which have double
underscores `__` before and after the name, example: `__init__`, we call it
*dunder init*).

__len__ method
---------------

Dunder len is a method used by the *len* function to know the length of any
iterator or similar objects. It should return an Integer. The *len* function
verifies if the returned value is Integer or not.

::

    class Foo:
        "Example class for __len__"
        def __init__(self, length=5):
            self.length = 5

        def __len__(self):
            return self.length


    f = Foo()
    length = len(f)
    print(f"Length of the f object is {length}")

The output:

::

    $ python3 code/lenexample.py 
    Length of the f object is 5

__contains__ method
--------------------

This method helps us to use `in` with our objects. For example, if we want to
match `"kushal" in studnet1` to be `True`, we implement `__contains__` method
in our class.


::

    class Student(Person):
        """
        Returns a ```Student``` object, takes 3 arguments, name, branch, year.

        """
        def __init__(self, name, branch, year):
            super().__init__(name)
            self.branch = branch
            self.year = year

        def get_details(self):
            "Returns a string containing student's details."
            return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)

        def __contains__(self, name):
            return self._name == name


    student1 = Student("kushal", "cse", 2005)

    print("kushal" in student1)
    print("sachin" in student1)


__new__ method
----------------

`__new__` is a special method. When we create an instance of the class,
internally this method gets called first, and then `__init__` gets called on
the returned object. It takes the class as the first argument. In the following
example, we are using our `Point` class again.

::

    p = Point.__new__(Point, 2, 3)
    p.__init__(2, 3)
    print(p)

    <Point x=2 y=3>


Creating a new context manager
===============================

Do you remember the `with` statement from the `files` chapter? Where we used a
context manager to make sure that the file is closed after we are done? The
same style is used in many places where we want the resources to be cleaned up
after the work is done; sometimes we want to call some extra functions when we are
done. We can write our own context manager in our classs using `__enter__` and
`__exit__` methods.

For example, we will create a new class called `TimeLog` which in turn will
create a file called `tmpdata.txt` in the current directory to log the time
this context manager is created and when it is done.

::

    import time

    class TimeLog:

        def __init__(self):
            self.fobj = None

        def __enter__(self):
            self.fobj = open("tmpdata.txt", "w")
            self.fobj.write(f"Entering at {time.time()}\n")

        def __exit__(self, ty, value, tb):
            self.fobj.write(f"Done at {time.time()}\n")
            self.fobj.close()
            self.fobj = None


    with TimeLog() as tl:
        a = [1, 2, 3]
        print(a)

Output in the `tmpdata.txt` file.

::

    Entering at 1590551277.323565
    Done at 1590551277.3238761

Later in the book we will learn even simpler methods to create context managers.

Deep down inside
=================

If we look inside of our class definitions, we will find a dictionary at the center.
Let us look at it in details in the following example.

::

    class User:
        def __init__(self, name, uid, gid, home, sudo):
            self.name = name
            self.uid = uid
            self.gids = [gid,]
            self.home = home
            self.sudo = sudo

        def can_sudo(self):
            return self.sudo
    
    u = User("kdas", 1000, 1000, "/home/kdas", True)
    pprint(u.__dict__)

    {'gids': [1000],
     'home': '/home/kdas',
     'name': 'kdas',
     'sudo': True,
     'uid': 1000}

All the attributes we defined via `self` in the `__init__` method, are stored in
the `__dict__` dictionary inside of each instance. When we try access any of
these attributes, Python first looks at this dictionary of the object, and then
also in the `__dict__` of the class itself.

::

    >>> pprint(User.__dict__)
    mappingproxy({'__dict__': <attribute '__dict__' of 'User' objects>,
                  '__doc__': None,
                  '__init__': <function User.__init__ at 0x7fa8c6f1bd40>,
                  '__module__': '__main__',
                  '__weakref__': <attribute '__weakref__' of 'User' objects>,
                  'can_sudo': <function User.can_sudo at 0x7fa8c6f3e3b0>})

When we try to access any attribute via the `.` operator, Python first checks the
`__getattribute__` method to look at the `__dict__`. If the key can not be found,
it tries to call the `__getattr__` method on the object.

::

    class Magic:
        def __init__(self):
            self.name = "magic"

        def __getattr__(self, attr):
            return attr.upper()

Now, if we try to use this `Magic` class, we can access any random attribute even if they don't exist.

::

    ❯ python3 -i deepinsideobjects.py
    >>> m = Magic()
    >>> m.name
    'magic'
    >>> m.what_is_this_magic
    'WHAT_IS_THIS_MAGIC'
    >>> m.this
    'THIS'
    >>> m.hello
    'HELLO'

Using the same approach we took, to access the data stored inside
another object of our class, we can also implement the `__setattr__` method,
which is used to set a value to any attribute.

::


    class User:

        def __init__(self, name, uid, gid, home, sudo):
            self.__dict__["_internal"] = {"name": name, "uid": uid, "gids": [gid,], "home": home, "sudo": sudo}

        def can_sudo(self):
            return self._internal["sudo"]

        def __getattr__(self, attr):
            print(f"Accessing attr: {attr}")
            return self._internal[attr]

        def __setattr__(self, attr, value):
            print(f"Setting attribute {attr} to {value}")
            self._internal[attr] = value


    u = User("kdas", 1000, 1000, "/home/kdas", True)

When we try to access any attribute of the object `u`, we can see the following.

::

    ❯ python3 -i deepinsideobjects.py
    >>> u.name
    Accessing attr: name
    'kdas'
    >>> u.uid
    Accessing attr: uid
    1000
    >>> u.can_sudo()
    True

There is also `__delattr__` method to delete any attribute of an instance. Feel
free to add it to the class above and see how it behaves.

