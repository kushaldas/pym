#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

while True:
    n = int(raw_input("Please enter an Integer: "))
    if n < 0:
        continue #this will take the execution back to the starting of the loop
    elif n == 0:
        break
    print( "Square is ", n ** 2)
print ("Goodbye")
