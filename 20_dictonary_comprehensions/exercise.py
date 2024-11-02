# Dictionaries and students
# This coding exercise has three parts. See them outlined in detail the coding exercise, as comments in the code.
## Create a dictionary variable, called "student".
## Modify a variable `grades`, so it contains the values of the dictionary's key.
## Implement a function calculating a total average grade for a class of students.

### Part 1
student = {"name": "Rolf", "school": "Computing", "grades": (66, 77, 88, 99)}


### Part 2
def average_grade(data):
    grades = data["grades"]
    return sum(grades) / len(grades)


### Part 3
def average_grade_all_students(students):
    total = 0
    count = 0
    for student in students:
        total += sum(student["grades"])
        count += len(student["grades"])
    return total / count
