# Unpacking arguments
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(multiply(1, 3, 5))  # 15
print(multiply(-1))  # -1


## Unpacking arguments with multiply function
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)  # Unpacking the arguments
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"


print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="*"))


# Unpacking arguments with add function
def add(x, y):
    return x + y


nums = [3, 5]
add(*nums)  # 8
nums = {"x": 15, "y": 25}
print(add(x=nums["x"], y=nums["y"]))  # 40
print(add(**nums))  # 40
