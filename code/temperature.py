#!/usr/bin/env python3

fahrenheit = 0.0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32.0) / 1.8  # Here we calculate the Celsius value
    print("%5.1f %7.2f" % (fahrenheit, celsius))
    fahrenheit = fahrenheit + 25
