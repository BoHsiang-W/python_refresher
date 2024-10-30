# type_hinting
from typing import List

def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)

# list_avg(123)          # argument should be a list
list_avg([1, 2, 3])    # 2.0

####################################################################################################
class Book:
    TYPE = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: float):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    # Use quotes for return type hinting when referring to the same class
    @classmethod
    def hardcover(cls, name: str, page_weight: float) -> "Book":
        return cls(name, cls.TYPE[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: float) -> "Book":
        return cls(name, cls.TYPE[1], page_weight)

class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."