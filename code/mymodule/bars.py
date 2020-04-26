"""
Bars Module
============

This is an example module which provides different ways to print bars.

"""

ANSWER = 42


def starbar(num):
    """
    Prints a bar with *

    :arg num: Length of the bar

    """
    print("*" * num)


def hashbar(num):
    """
    Prints a bar with #

    :arg num: Length of the bar

    """
    print("#" * num)


def simplebar(num):
    """
    Prints a bar with -

    :arg num: Length of the bar
    
    """
    print("-" * num)


print(ANSWER)
