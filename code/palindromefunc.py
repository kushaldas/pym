#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)


def palindrome(s):
    z = s
    z = [x for x in z]
    z.reverse()
    if s == "".join(z):
        return True
    else:
        return False

s = raw_input("Enter a string: ")
if palindrome(s):
    print ("Yay a palindrome")
else:
    print ("Oh no, not a palindrome")
