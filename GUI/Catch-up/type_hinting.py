from typing import List

def list_avr(sequence: List) -> float:
    """Calculate the average of a list of numbers."""
    if not sequence:
        return 0.0
    return sum(sequence) / len(sequence)

try:
    list_avr(123)  # This will raise a TypeError because the input is not a list
except TypeError as e:
    print(f"Error: {e}. Please provide a list of numbers.")
    pass

list_avr([1, 2, 3, 4, 5])  # This will work correctly and return the average
list_avr([])  # This will return 0.0 since the list is empty