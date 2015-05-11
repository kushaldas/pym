#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)


n = int(raw_input("Enter the value of n: "))
print( "Enter values for the Matrix A")
a = []
for i in range(0, n):
    a.append([int(x) for x in raw_input("").split(" ")])

print( "Enter values for the Matrix B")
b = []
for i in range(0, n):
    b.append([int(x) for x in raw_input("").split(" ")])
c = []
for i in range(0, n):
    c.append([a[i][j] * b[j][i] for j in range(0,n)])
print ("After matrix multiplication")
print( "-" * 10 * n)
for x in c:
    for y in x:
        print( "%5d" % y,)
    print( "")
print( "-" * 10 * n)
