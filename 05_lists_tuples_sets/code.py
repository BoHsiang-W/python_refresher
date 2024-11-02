# List, tuples, and sets

l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

# Modify list
l[0] = "Smith"
l.append("Jen")  # Added an element to the list
l.remove("Rolf")  # Removed an element from the list
print(l)

# Tuples are immutable, so we can't modify them directly

# Modify set
s.add("Smith")
print(s)
