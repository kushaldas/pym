#!/usr/bin/env python3
farenhite = 0.0
print ("Farenhite Celcious")
while farenhite <= 250:
    celcious = ( farenhite - 32.0 ) / 1.8
    print ("%5.1f %7.2f" % (farenhite , celcious))
    farenhite = farenhite + 25
