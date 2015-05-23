#!/usr/bin/env python3
name = input("Enter the filename: ")
f = open(name)
print (f.read())
f.close()
