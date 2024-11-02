a = []
b = a

print(id(a))  # 140067366748992
print(id(b))  # 140067366748992
# because a and b are the same object, they have the same id

a = []
b = []
a.append(35)
print(id(a))  # 1744327187264
print(id(b))  # 1744332279232
# because a and b are different objects, they have different ids

a = 8597
b = 8597

print(id(a))  # 1925900502704
print(id(b))  # 1925900502704
# because python already has an object for 8597, it just assigns the same object to b

a = 8598
b = 8597

print(id(a))  # 2269430319184
print(id(b))  # 2269430318768
# because a and b are different objects, they have different ids

a = "Hello"
b = a

print(id(a))  # 140067366748992
print(id(b))  # 140067366748992

a += " World"
print(id(a))  # 2139459547568
print(id(b))  # 2139459526384
# because strings are immutable, a new object is created when a is modified
