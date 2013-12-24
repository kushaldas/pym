#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

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
    print( "%s 's  total marks %d" % (x, total))
    if total < 120:
        print( "%s failed :(" % x)
    else:
        print ("%s passed :)" % y)

    

