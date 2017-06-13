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
std2 = Student("Sayan", 2005, "cse", 121)
std3 = Student("Anwesha", 2005, "law", 122)

std1.papers = {"english": 78, "math": 82, "science": 77}
std2.papers = {"english": 80, "math": 92, "science": 78}
std3.papers = {"english": 82, "math": 87, "science": 77}

for std in [std1, std2, std3]:
    print("Passed: {0}. The toral score of {1} is {2}".format(std.is_passed(), std.name, std.total_score()))

std1 = {"type": "studnet"}