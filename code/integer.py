#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

days = int(raw_input("Enter days: "))
months = days / 30
days = days % 30
print( "Months = %d Days = %d" % (months, days))
