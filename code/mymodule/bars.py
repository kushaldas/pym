"""
Bars Module
============

This is an example module which provides different ways to print bars.

"""

def starbar(num):
    """
    Prints a bar with *

    :arg num: Length of the bar

    """
    print('*' * num)

def hashbar(num):
    """
    Prints a bar with #

    :arg num: Length of the bar

    """
    print('#' * num)

def simplebar(num):
    """
    Prints a bar with -

    :arg num: Length of the bar
    
    """
    print('-' * num)

if __name__=='__main__':
    simplebar(20)
