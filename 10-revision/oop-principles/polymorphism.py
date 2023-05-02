from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def grade_range(self):
        pass


class ElementarySchoolStudent(Student):
    def __init__(self, name):
        super().__init__(name)

    def grade_range(self):
        print("0 to 10")


class HighSchoolStudent(Student):
    def __init__(self, name):
        super().__init__(name)

    def grade_range(self):
        print("0 to 20")


class UniversityStudent(Student):
    def __init__(self, name):
        super().__init__(name)

    def grade_range(self):
        print("A to D")


if __name__ == '__main__':
    students = []
    students.append(ElementarySchoolStudent("Nick"))
    students.append(HighSchoolStudent("Mike"))
    students.append(UniversityStudent("Ann"))

    for student in students:
        student.grade_range()
