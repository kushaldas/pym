#!/usr/bin/env python3
row = int(input("Enter the number of rows: "))
n = row
while n >= 0:
    x =  "*" * n
    y = " " * (row - n)
    print (y + x)
    n -= 1
