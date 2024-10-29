# Demonstrating classmethod and staticmethod usage

class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")

test = ClassTest()
test.instance_method()          # Called instance_method of <__main__.ClassTest object at 0x7f8b1b3b3d30>
ClassTest.instance_method(test) # Called instance_method of <__main__.ClassTest object at 0x7f8b1b3b3d30>

ClassTest.class_method()        # Called class_method of <class '__main__.ClassTest'>

ClassTest.static_method()       # Called static_method



class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

book = Book.hardcover("Harry Potter", 1500)
print(book) # <Book Harry Potter, hardcover, 1500g>

book2 = Book.paperback("Python 101", 600)
print(book2) # <Book Python 101, paperback, 700g>