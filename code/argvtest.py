#!/usr/bin/env python3
import sys
print ("First value", sys.argv[0])
print ("All values")
for i, x  in enumerate(sys.argv):
    print (i, x)
