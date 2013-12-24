#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

def change(a):
    a = 90
    print (a)

a = 9
print ("Before the function call ", a)
print( "inside change function",
change(a))
print ("After the function call ", a)
