#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

row = int(raw_input("Enter the number of rows: "))
n = row
while n >= 0:
    x =  "*" * n
    print(x)
    n -= 1
