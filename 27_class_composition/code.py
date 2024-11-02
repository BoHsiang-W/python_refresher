# Class Composition
class Bookshelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Bookshelf with {self.quantity} books."


shelf = Bookshelf(300)
print(shelf)  # Bookshelf with 300 books.


class Book(Bookshelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter", 20)
print(book)  # Book Harry Potter

####################################################################################################


class Bookshelf_composition:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book_composition:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book1 = Book_composition("Harry Potter")
book2 = Book_composition("Python 101")
shelf = Bookshelf_composition(book1, book2)
print(shelf)  # Bookshelf with 2 books.
