# Unpacking arguments
def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)  # {'name': 'Bob', 'age': 25}


def named(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

named(**details)  # Bob 25


def named(**kwargs):
    print(kwargs)


details = {"name": "Bob", "age": 25}
named(**details)  # {'name': 'Bob', 'age': 25}


## Unpacking keyword arguments with print nicely
def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)  # Bob 25


## Unpacking keyword arguments with args and kwargs
def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)  # (1, 3, 5) {'name': 'Bob', 'age': 25}


## Unpacking keyword arguments with kwargs
def my_function(**kwargs):
    print(kwargs)


my_function(**"Bob")  # TypeError: unpacking argument of type 'str' is not iterable
my_function(**None)  # TypeError: 'NoneType' object is not iterable
