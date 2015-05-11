#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)


s = raw_input("Please eneter a string: ")
z = [x for x in s]
z.reverse()
if s == "".join(z):
    print ("The string is a palindrome")
else:
    print( "The string is not a palindrome")
