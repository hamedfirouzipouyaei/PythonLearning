student = {"name": "Jhon", "grades": [90, 80, 85, 95]}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))

class Student:
    def __init__(self, name_, grades_):
        self.name = name_
        self.grades= grades_
    def average(self):
        return sum(self.grades) / len(self.grades)
    

student1 = Student("Jhon", [90, 85, 85, 95])
print(student1.average())