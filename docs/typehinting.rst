==============================
Type hinting and annotations
==============================

This is one of the new feature of the language. We can do the similar kind of
work in Python2 also, but with different syntax. Please remember that Python
will stay as a dynamically typed language, this type hinting does not effect
your code anyway.

The major benefit of having type hints in your codebase is about future
maintenance of the codebase. When a new developer will try to contribute to
your project, having type hints will save a lot of time for that new person.
It can also help to detect some of the runtime issues we see due to passing
of wrong variable types in different function calls.

First example of type annotation
==================================

Let us start with a simple example, adding of two integers.

::

    def add(a, b):
        return a + b

Now, the above example will work for any object which supports *+* operator.
But, we want to specify that it is expecting only Integers as parameters, and
the function call will return another Integer.

::

    def add(a: int, b: int) -> int:
        return a + b

You can see that the return type of the function call is defined after *->*.
We can do the same in Python2 using a comment (before any docstring).
::

    def add(a, b):
        # type: (int, int) -> int
        return a + b


Using mypy and more examples
=============================

`Mypy <https://mypy.rtfd.io>`_ is a static type checker written for Python. If we use the type
annotations as explained above, mypy can help by finding common problems in
our code. You can use mypy in various ways in your development workflow, may
be in CI as a proper test.

Installing mypy
---------------

We can install mypy inside of a virtual environment.

::

    $ pipenv install mypy
    Installing mypy…
    Looking in indexes: https://pypi.python.org/simple
    Collecting mypy
    Downloading https://files.pythonhosted.org/packages/e2/3f/e20e2544b35e862fbed4e26a89e3d857007c5bd32abc019ef21c02aecd98/mypy-0.600-py3-none-any.whl (1.3MB)
    Collecting typed-ast<1.2.0,>=1.1.0 (from mypy)
    Downloading https://files.pythonhosted.org/packages/5b/4e/79e873aa89b8038ca6474c00afe96f9468973b604e7f737cb82697a680c0/typed_ast-1.1.0-cp35-cp35m-manylinux1_x86_64.whl (724kB)
    Installing collected packages: typed-ast, mypy
    Successfully installed mypy-0.600 typed-ast-1.1.0

    Adding mypy to Pipfile's [packages]…
    Pipfile.lock (627f99) out of date, updating to (67e074)…
    Locking [dev-packages] dependencies…
    Locking [packages] dependencies…
    Updated Pipfile.lock (67e074)!
    Installing dependencies from Pipfile.lock (67e074)…
    🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 7/7 — 00:00:01
    To activate this project's virtualenv, run the following:
    $ pipenv shell


Our example code
-----------------

We wil working on the following example code. This does not do much useful
things, but we can use this to learn about type annotations and mypy.

::

    class Student:

        def __init__(self, name, batch, branch, roll):
            self.name = name
            self.batch = batch
            self.branch = branch
            self.roll = roll
            self.semester = None
            self.papers = {}

        def is_passed(self):
            "To find if the student has pass the exam in the current semester"
            for k, v in self.papers.items():
                if v < 34:
                    return False

            return True


        def total_score(self):
            "Returns the total score of the student"
            total = 0
            for k, v in self.papers.items():
                total += v

            return total


    std1 = Student("Kushal", 2005, "cse", "123")
    std2 = Student("Sayan", 2005, "cse", 121)
    std3 = Student("Anwesha", 2005, "law", 122)

    std1.papers = {"english": 78, "math": 82, "science": 77}
    std2.papers = {"english": 80, "math": 92, "science": "78"}
    std3.papers = {"english": 82, "math": 87, "science": 77}

    for std in [std1, std2, std3]:
        print("Passed: {0}. The toral score of {1} is {2}".format(std.is_passed(), std.name, std.total_score()))


You may find some errors in the code, but in case of a large codebase we can
not detect the similar issues unless we see the runtime errors.

Using mypy
-----------

We can just call mypy on our source file, I named it as *students2.py*

::

    $ mypy studets2.py

Enabling the first few type annotations
----------------------------------------

We will add some type annotations to the *__init__* method. For reducing the
code length, I am only showing the changed code below.

::

    class Student:

    def __init__(self, name: str, batch: int, branch: str, roll: int) -> None:
        self.name = name
        self.batch = batch
        self.branch = branch
        self.roll = roll
        self.semester = None
        self.papers = {}


::

    $ mypy students2.py
    students2.py:11: error: Need type annotation for variable
    students2.py:31: error: Argument 4 to "Student" has incompatible type "str"; expected "int"

You can see mypy is complaining about variable which does not have type
annotations, and also found that in line 31, as argument 4 we are passing
*str*, where as we were supposed to send in an Integer for the rull number.
Let us fix these.

::

    from typing import Dict

    class Student:

        def __init__(self, name: str, batch: int, branch: str, roll: int) -> None:
            self.name = name
            self.batch = batch
            self.branch = branch
            self.roll = roll
            self.semester: str = None
            self.papers: Dict[str, int] = {}

        def is_passed(self) -> bool:
            "To find if the student has pass the exam in the current semester"
            for k, v in self.papers.items():
                if v < 34:
                    return False

            return True


        def total_score(self) -> int:
            "Returns the total score of the student"
            total = 0
            for k, v in self.papers.items():
                total += v

            return total


    std1: Student = Student("Kushal", 2005, "cse", 123)
    std2: Student = Student("Sayan", 2005, "cse", 121)
    std3: Student = Student("Anwesha", 2005, "law", 122)

    std1.papers = {"english": 78, "math": 82, "science": 77}
    std2: Student.papers = {"english": 80, "math": 92, "science": 78}
    std3.papers = {"english": 82, "math": 87, "science": 77}

    for std in [std1, std2, std3]:
        print("Passed: {0}. The toral score of {1} is {2}".format(std.is_passed(), std.name, std.total_score()))

::

    $ mypy students2.py

Now, it does not complain about any error. You can see that in line 1, we
imported Dict from the typing module. And, then using the same we added the
type annotation of the *self.paper* variable. We are saying that it is a
dictionary which has string keys, and Integers as values. We also used our
*Student* class as type of std1, std2, and std3 variables.

Now let us say we by mistake assign a new list to the papers variable.

::

    std1.papers = ["English", "Math"]


Or maybe assigned a wrong kind of dictionary.

::

    std2.papers = {1: "Engish", 2: "Math"}

We can see what mypy says in these cases

::

    $ mypy students2.py
    students2.py:35: error: Incompatible types in assignment (expression has type List[str], variable has type Dict[str, int])
    students2.py:36: error: Dict entry 0 has incompatible type "int": "str"
    students2.py:36: error: Dict entry 1 has incompatible type "int": "str"


More examples of type annotations
==================================

::

    from typing import List, Tuple, Sequence, Optional

    values: List[int] = []
    city: int = 350 # The city code, not a name


    # This function returns a Tuple of two values, a str and an int
    def get_details() -> Tuple[str, int]:
        return "Python", 5

    # The following is an example of Tuple unpacking
    name: str
    marks: int
    name, marks = get_details()


    def print_all(values: Sequence) -> None:
        for v in values:
            print(v)


    print_all([1,2,3])
    print_all({"name": "kushal", "class": 5})
    # alltypes.py:23: error: Argument 1 to "print_all" has incompatible type Dict[str, object]; expected Sequence[Any]
    # But running the code will give us no error with wrong output

    def add_ten(number: Optional[int] = None) -> int:
        if number:
            return number + 10
        else:
            return 42

    print(add_ten())
    print(add_ten(12))

You can learn more about types from `PEP 484
<https://www.python.org/dev/peps/pep-0484/>`_. The `typing module
<https://docs.python.org/3/library/typing.html>`_ has detailed explanation and
more examples about how to add type annotations in your codebase.

You can also view `the talk <https://www.youtube.com/watch?v=pMgmKJyWKn8>`_
from Carl Meyer to learn about type checking in Python.
