# Functions returning values
def add(x, y=8):
    print(x + y)
    return x + y


result = add(5, 8)
print(result)  # 13

## function returning values


def add(x, y=8):
    return
    print(x + y)
    return x + y


result = add(5, 8)
print(result)  # None


## function returning values
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


result = divide(15, 0)
print(result)  # You fool!

result = divide(15, 3) * 5
print(result)  # 25.0
