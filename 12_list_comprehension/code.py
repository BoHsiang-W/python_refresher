# List comprehension

## List comprehension is a way to create lists in a more concise way
number = [1,3,5]
doubled = []

for num in number:
    doubled.append(num * 2)
print(doubled)

doubled = [num * 2 for num in number]
print(doubled)

## Another example
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)
print(starts_s)

strats_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)

print(friends)
print(starts_s) 
print(friends is starts_s)  # False
print("friends: ", id(friends), "starts_s: ", id(starts_s)) # id() returns the memory address of the object

