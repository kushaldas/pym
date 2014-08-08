#!/usr/bin/env python3
s = input("Please eneter a string: ")
z = [x for x in s]
z.reverse()
if s == "".join(z):
    print ("The string is a palindrome")
else:
    print ("The string is not a palindrome")
