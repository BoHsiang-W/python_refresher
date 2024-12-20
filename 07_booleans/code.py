# Booleans in Python

print(5 == 5)  # True

print(5 > 5)  # False

print(10 != 10)  # False

# Comparisons: ==, !=, >, <, >=, <=

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)  # True
print(friends is abroad)  # False

abroad = friends

print(friends == abroad)  # True
