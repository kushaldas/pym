#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

name = raw_input("Enter the filename: ")
f = open(name)
print( f.read())
f.close()
