#!/usr/bin/env python3

N = 10
sum = 0
count = 0
while count < N:
    number = float(input(""))
    sum = sum + number
    count = count + 1
average = float(sum) / N
print("N = %d , Sum = %f" % (N, sum))
print("Average = %f" % average)
