#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

sum = 0.0
for i in range(1, 11):
    sum += 1.0 / i
    print( "%2d %10.4f" % (i , sum))
