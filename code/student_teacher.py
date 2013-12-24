#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

class Person(object):
    """
    Returns a ```Person``` object with given name.
    """
    def __init__(self,name):
        self.name = name

    def get_details(self):
        "Returns a string containing name of the person"
        return self.name


class Student(Person):
    """
    Returns a ```Student``` object, takes 3 arguments, name, branch, year.
    """
    def __init__(self,name,branch,year):
        Person.__init__(self,name)
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


person1 = Person('Rahul')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print( person1.get_details())
print( student1.get_details())
print( teacher1.get_details())

