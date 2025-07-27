class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def __str__(self): # This method is called when you use print(person)
        return f"Person(name={self.name}, age={self.age})"
    
    def __repr__ (self): # This method is called when you use repr(person)
        return f"Person(name={self.name}, age={self.age})"
    

bob = Person("Bob", 30)
print(bob)  # Output: Person(name=Bob, age=30)
