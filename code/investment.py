#!/usr/bin/env python3
amount = float(input("Enter amount: "))
inrate = float(input("Enter Interest rate: "))
period = int(input("Enter period: "))
value = 0
year = 1
while year <= period:
    value = amount + (inrate/100 * amount)
    print ("Year %d Rs. %.2f" %(year, value))
    amount = value
    year = year + 1
