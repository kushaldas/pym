

=====
Class
=====

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



__init__ is called when ever an object of the class is constructed. That means when ever we will create a student object we will see the message "A student object is created" in the prompt. You can see the first argument to the method is *self*. It is a special variable which points to the current object (like `this` in C++). The object is passed implicitly to every method available in it, but we have to get it explicitly in every method while writing the methods. Example shown below.
Remember to declare all the possible attributes in the *__init__* method itself. Even if you are not using them right away, you can always assign them as *None*.

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

.. index:: Inheritance

Inheritance
===========

In general we human beings always know about inheritance. In programming it is almost the same. When a class inherits another class it inherits all features (like variables and methods) of the parent class. This helps in reusing codes.

In the next example we first create a class called Person and create two sub-classes Student and Teacher. As both of the classes are inherited from Person class they will have all methods of Person and will have new methods and variables for their own purpose.

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
            Person.__init__(self, name)
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
            Person.__init__(self, name)
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

In this example you can see how we called the __init__ method of the class Person in both Student and Teacher classes' __init__ method. We also reimplemented *get_details()* method of Person class in both Student and Teacher class. So, when we are calling *get_details()* method on the teacher1 object it returns based on the object itself (which is of teacher class) and when we call *get_details()* on the student1 or person1 object it returns based on *get_details()* method implemented in it's own class.

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
