# Object Oriented Programming

student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))  # 88.0
print(student.average())  # AttributeError: 'dict' object has no attribute 'average'


# Object Oriented Programming
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Rolf", (89, 90, 93, 78, 90))
print(student.name)
print(student.grades)
print(student.average())  # 88.0
student2 = Student("Bob", (100, 100, 93, 78, 90))
print(student2.name)
print(student2.grades)
print(student2.average())  # 92.2
