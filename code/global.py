#!/usr/bin/env python
def change(b):
    global a
    a = 90
    print a

a = 9
print "Before the function call ", a
print "inside change function",
change(a)
print "After the function call ", a
