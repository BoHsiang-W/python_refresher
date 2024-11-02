# Dictionaries

## Dictionaries are a way to store information that is related in some way.
friends_age = {"Rolf": 24, "Adam": 30, "Anne": 27}

friends_age["Bob"] = 20
friends_age["Rolf"] = 25
print(friends_age)

## Accessing a dictionary

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]

print(friends[1]["name"])

## student
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

if "Bob" in student_attendance:
    print("Bob: ", student_attendance["Bob"])
else:
    print("Bob is not a student in this class.")

## Exercise
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))
