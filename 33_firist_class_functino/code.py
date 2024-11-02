def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)  # 5.0

result = calculate(20, 0, operator=divide)
print(result)  # ZeroDivisionError: Divisor cannot be 0.
####################################################################################################


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Anna Johnson", "age": 22},
    {"name": "Charlie Brown", "age": 30},
]


def get_friend_name(friend):
    return friend["name"]


print(
    search(friends, "Anna Johnson", get_friend_name)
)  # {'name': 'Anna Johnson', 'age': 22}

print(
    search(friends, "Anna Johnson", lambda friend: friend["name"])
)  # {'name': 'Anna Johnson', 'age': 22}

from operator import itemgetter

print(
    search(friends, "Anna Johnson", itemgetter("name"))
)  # {'name': 'Anna Johnson', 'age': 22}
