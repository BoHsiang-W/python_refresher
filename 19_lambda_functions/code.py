# lambda functions


def add(x, y):
    return x + y


print(add(5, 7))  # 12

add = lambda x, y: x + y
print(add(5, 7))  # 12

print((lambda x, y: x + y)(5, 7))  # 12


## lambda functions with double function
def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
doubled = list(map(double, sequence))  # [2, 6, 10, 18]
doubled = [(lambda x: x * 2)(x) for x in sequence]  # [2, 6, 10, 18]
doubled = list(map(lambda x: x * 2, sequence))  # [2, 6, 10, 18]
