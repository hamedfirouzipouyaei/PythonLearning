class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return "Bookshelf with {} books.".format(len(self.books))
    
class Book:
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return "Book: {}".format(self.name)
    
book1 = Book("Python Programming")
book2 = Book("Data Science Handbook")
shelf = BookShelf(book1, book2)

print(shelf)