import numpy as np

print("This is a test script.")

a = np.array([1, 2, 3])
print("Numpy array created:", a)

class TestClass:
    def __init__(self, value):
        self.value = value
        self.new_value = value + 5

    def display(self):
        print("Value in TestClass:", self.value)
        print("New value in TestClass:", self.new_value)



def main():
    test_instance = TestClass(10)
    test_instance.display()

if __name__ == "__main__":
    main()