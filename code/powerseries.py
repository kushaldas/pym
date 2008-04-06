#!/usr/bin/env python
x = float(raw_input("Enter the value of x: "))
n = term = num = 1
sum = 1.0
while n <= 100:
    term *= x / n
    sum += term
    n += 1
    if term < 0.0001:
        break
print "No of Times= %d and Sum= %f" % (n, sum)


