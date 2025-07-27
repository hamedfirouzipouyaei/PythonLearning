class ClassTest:
    @staticmethod
    def static_method():
        return "This is a static method"
    
    @classmethod
    def class_method(cls):
        return f"This is a class method of {cls.__name__}"
    
    def instance_method(self):
        return f"This is an instance method {self}"
    
# Example usage
if __name__ == "__main__":
    # Calling static method
    print(ClassTest.static_method())
    
    # Calling class method
    print(ClassTest.class_method())
    
    # Creating an instance and calling instance method
    instance = ClassTest()
    print(instance.instance_method())


class Book:
    TYPES = ('hardcover', 'paperback', 'ebook')

    def __init__(self, name, book_type, price):
        self.name = name
        self.book_type = book_type
        self.price = price
    

    def __repr__(self):
        return f"Book(name={self.name}, book_type={self.book_type}, price={self.price})"
    
    @classmethod
    def hardcover(cls, name, price):
        return Book(name, Book.TYPES[0], price)
    
    @classmethod
    def paperback(cls, name, price):
        return Book(name, Book.TYPES[1], price)
    
book = Book.hardcover("Python Programming", 29.99)
print("Book created using class method:")
print(book)
book1 = Book.paperback("Harry Potter", 30)
print("Book created using class method:")
print(book1)