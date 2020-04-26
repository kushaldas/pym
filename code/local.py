#!/usr/bin/env python


def change(a):
    a = 90
    print(f"Inside of the change function {a}")


a = 9
print(f"Before the function call {a}")
change(a)
print(f"After the function call {a}")
