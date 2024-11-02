# str and repr


class Person:
    def __init__(self, name, age):  # constructor method
        self.name = name
        self.age = age

    def __str__(self):  # string representation of the object
        return f"Person({self.name}, {self.age}) years old"

    def __repr__(self):  # representation of the object
        return f"<Person({self.name}, {self.age})>"


bob = Person("Bob", 35)
print(bob)  # Person Bob, 35 years old
# __str__ and __repr__ are both used to represent an object,
# but __str__ is used for a more human-readable output,
# while __repr__ is used for a more unambiguous output.
