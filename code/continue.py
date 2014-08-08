#!/usr/bin/env python3

while True:
    n = int(input("Please enter an Integer: "))
    if n < 0:
        continue #this will take the execution back to the starting of the loop
    elif n == 0:
        break
    print ("Square is ", n ** 2)
print ("Goodbye")
