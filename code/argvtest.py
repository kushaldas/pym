#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)
import sys
print ("First value", sys.argv[0])
print ("All values")
for i, x  in enumerate(sys.argv):
    print (i, x)
