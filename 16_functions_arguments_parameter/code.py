# function with arguments and parameter


def add(x, y):
    result = x + y
    print(result)


add(5, 3)


# function with arguments and parameter
def say_hello(name, surname):
    print(f"Hello!, {name} {surname}")  # Hello!, Rolf Bob


say_hello(surname="Bob", name="Rolf")


# function with arguments and parameter
def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


divide(15, 0)  # You fool!
divide(dividend=15, divisor=3)  # 5.0
divide(dividend=15, divisor=0)  # You fool!
