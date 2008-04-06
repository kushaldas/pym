#!/usr/bin/env python
name = raw_input("Enter the filename: ")
f = open(name)
print f.read()
f.close()
