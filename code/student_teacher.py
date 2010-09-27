#!/usr/bin/env python

class Person:
    def __init__(self,name):
        self.name = name

    def getDetails(self):
        return self.name


class Student(Person):
    def __init__(self,name,branch,year):
        Person.__init__(self,name)
        self.branch = branch
        self.year = year

    def getDetails(self):
        return (self.name, self.branch, self.year)


class Teacher(Person):
    def __init__(self,name,papers):
        Person.__init__(self,name)
        self.papers = papers

    def getDetails(self):
        return (self.name, self.papers)


person1 = Person('Rahul')
student1 = Student('Kushal','CSE',2005)
teacher1 = Teacher('Prashad',['C','C++'])

print person1.getDetails()
print student1.getDetails()
print teacher1.getDetails()

