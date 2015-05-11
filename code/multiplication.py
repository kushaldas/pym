#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

i = 1
print( "-" * 50)
while i < 11:
    n = 1
    while n <= 10:
        print ("%4d" % (i * n),
        n += 1)
    print( "")
    i += 1
print( "-" * 50)
