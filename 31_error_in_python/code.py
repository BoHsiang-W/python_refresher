def divide(dividend, divisor):
    if divisor == 0:
        print("You can't divide by zero!")
        return
    return dividend / divisor

divide(15, 0)

####################################################################################################

grade = [88, 99, 77, 55, 33, 22, 11, 44, 66, 100]
print("Welcome to the average grade program.")
average = divide(sum(grade), len(grade))
print(f"The average grade is {average}.")

####################################################################################################
def divide_1(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor

grade = []
print("Welcome to the average grade program.")
average = divide_1(sum(grade), len(grade))
print(f"The average grade is {average}.")

####################################################################################################
def divide_2(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor

grade = []
print("Welcome to the average grade program.")
try:
    average = divide_2(sum(grade), len(grade))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in the system.")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you for using the average grade program.")

####################################################################################################
students = [
    {"name": "Bob", "grades": [88, 99, 77, 55, 33, 22, 11, 44, 66, 100]},
    {"name": "Rolf", "grades": []},
    {"name": "Charlie", "grades": None}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide_1(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("--All Student's grades have been calculated--")
finally:
    print("Thank you for using the average grade program.")