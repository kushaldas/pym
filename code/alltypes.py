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