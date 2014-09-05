========================
Simple testing in Python
========================



What we should test ?
=====================

If possible everything in our codebase, each and every function. But it depends as a choice
of the developers. You can skip it if it is not practical to write a robust test. As Nick Coghlan
said in a guest session -- *... with a solid test suite, you can make big changes, confident that the externally visible behavior will remain the same*

Unit testing
=============

A method by which individual units of source code. `Wikipedia <http://en.wikipedia.org/wiki/Unit_testing>`_ says
*In computer programming, unit testing is a method by which individual units of source code,
sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures, are tested to determine if they are fit for use.*


unittest module
===============
In Python we have ``unittest`` module to help us.

Factorial code
===============

In this example we will write a file `factorial.py`.
::

    import sys

    def fact(n):
        """
        Factorial function

        :arg n: Number
        :returns: factorial of n

        """
        if n == 0:
            return 1
        return n * fact(n -1)

    def div(n):
        """
        Just divide
        """
        res = 10 / n
        return res


    def main(n):
        res = fact(n)
        print(res)

    if __name__ == '__main__':
        if len(sys.argv) > 1:
            main(int(sys.argv[1]))


Output
::

    $ python factorial.py 5

Which function to test ?
========================
As you can see ``fact(n)`` is function which is doing all calculations, so
we should test that at least.


Our first test case
===================

Now we will write our first test case.
::

    import unittest
    from factorial import fact

    class TestFactorial(unittest.TestCase):
        """
        Our basic test class
        """

        def test_fact(self):
            """
            The actual test.
            Any method which starts with ``test_`` will considered as a test case.
            """
            res = fact(5)
            self.assertEqual(res, 120)


    if __name__ == '__main__':
        unittest.main()


Running  the test:

::

   $ python factorial_test.py
   .
   ----------------------------------------------------------------------
   Ran 1 test in 0.000s

   OK


Description
===========
We are importing ``unittest`` module first and then the required functions
which we want to test.

A testcase is created by subclassing ``unittest.TestCase``.

Now open the test file and change *120* to *121* and see what happens :)


Different assert statements
===========================
   +-----------------------------------------+-----------------------------+---------------+
   | Method                                  | Checks that                 | New in        |
   +=========================================+=============================+===============+
   | `assertEqual(a, b)`                     | ``a == b``                  |               |
   +-----------------------------------------+-----------------------------+---------------+
   | `assertNotEqual(a, b)`                  | ``a != b``                  |               |
   +-----------------------------------------+-----------------------------+---------------+
   | `assertTrue(x)`                         | ``bool(x) is True``         |               |
   +-----------------------------------------+-----------------------------+---------------+
   | `assertFalse(x)`                        | ``bool(x) is False``        |               |
   +-----------------------------------------+-----------------------------+---------------+
   | `assertIs(a, b)`                        | ``a is b``                  | 2.7           |
   +-----------------------------------------+-----------------------------+---------------+
   | `assertIsNot(a, b)`                     | ``a is not b``              | 2.7           |
   +-----------------------------------------+-----------------------------+---------------+
   | `assertIsNone(x)`                       | ``x is None``               | 2.7           |
   +-----------------------------------------+-----------------------------+---------------+
   | `assertIsNotNone(x)`                    | ``x is not None``           | 2.7           |
   +-----------------------------------------+-----------------------------+---------------+
   | `assertIn(a, b)`                        | ``a in b``                  | 2.7           |
   +-----------------------------------------+-----------------------------+---------------+
   | `assertNotIn(a, b)`                     | ``a not in b``              | 2.7           |
   +-----------------------------------------+-----------------------------+---------------+
   | `assertIsInstance(a, b)`                | ``isinstance(a, b)``        | 2.7           |
   +-----------------------------------------+-----------------------------+---------------+
   | `assertNotIsInstance(a, b)`             | ``not isinstance(a, b)``    | 2.7           |
   +-----------------------------------------+-----------------------------+---------------+


Testing exceptions
==================
If we call ``div(0)`` in factorial.py , we can see if raises an exception.

We can also test these exceptions, like:

::

    self.assertRaises(ZeroDivisionError, div, 0)

Full code
::

    import unittest
    from factorial import fact, div

    class TestFactorial(unittest.TestCase):
        """
        Our basic test class
        """

        def test_fact(self):
            """
            The actual test.
            Any method which starts with ``test_`` will considered as a test case.
            """
            res = fact(5)
            self.assertEqual(res, 120)

        def test_error(self):
            """
            To test exception raise due to run time error
            """
            self.assertRaises(ZeroDivisionError, div, 0)



    if __name__ == '__main__':
        unittest.main()

mounttab.py
============
Here we have only one function *mount_details()* doing the parsing and printing mount details.
::

    import os


    def mount_details():
        """
        Prints the mount details
        """
        if os.path.exists('/proc/mounts'):
            fd = open('/proc/mounts')
            for line in fd:
                line = line.strip()
                words = line.split()
                print()'%s on %s type %s' % (words[0],words[1],words[2]), end=' ')
                if len(words) > 5:
                    print('(%s)' % ' '.join(words[3:-2]))
                else:
                    print('')


    if __name__ == '__main__':
        mount_details()


After refactoring
=================
Now we refactored the code and have one new function *parse_mounts* which we can test easily.
::

    import os

    def parse_mounts():
        """
        It parses /proc/mounts and returns a list of tuples
        """
        result = []
        if os.path.exists('/proc/mounts'):
            fd = open('/proc/mounts')
            for line in fd:
                line = line.strip()
                words = line.split()
                if len(words) > 5:
                    res = (words[0],words[1],words[2], '(%s)' % ' '.join(words[3:-2]))
                else:
                   res = (words[0],words[1],words[2])
                result.append(res)
        return result

    def mount_details():
        """
        Prints the mount details
        """
        result = parse_mounts()
        for line in result:
            if len(line) == 4:
                print('%s on %s type %s %s' % line)
            else:
                print('%s on %s type %s' % line)


    if __name__ == '__main__':
        mount_details()

and the test code for the same.
::

    #!/usr/bin/env python
    import unittest
    from mounttab2 import parse_mounts

    class TestMount(unittest.TestCase):
        """
        Our basic test class
        """

        def test_parsemount(self):
            """
            The actual test.
            Any method which starts with ``test_`` will considered as a test case.
            """
            result = parse_mounts()
            self.assertIsInstance(result, list)
            self.assertIsInstance(result[0], tuple)

        def test_rootext4(self):
            """
            Test to find root filesystem
            """
            result = parse_mounts()
            for line in result:
                if line[1] == '/' and line[2] != 'rootfs':
                    self.assertEqual(line[2], 'ext4')


    if __name__ == '__main__':
        unittest.main()

::

     $ python mounttest.py
     ..
     ----------------------------------------------------------------------
     Ran 2 tests in 0.001s

     OK


Test coverage
=============
Test coverage is a simple way to find untested parts of a codebase. It does not
tell you how good your tests are.

In Python we already have a nice coverage tool to help us. You can install it in Fedora

::

    # yum install python-coverage

Or using `pip`.
::

    $ pip install coverage

Coverage Example
================
::

    $ coverage -x mounttest.py
    <OUTPUT snipped>

    $ coverage -rm
    Name        Stmts   Miss  Cover   Missing
    -----------------------------------------
    mounttab2      21      7    67%   16, 24-29, 33
    mounttest      14      0   100%
    -----------------------------------------
    TOTAL          35      7    80%
