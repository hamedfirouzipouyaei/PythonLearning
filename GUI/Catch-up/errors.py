class TooManyArgumentsError(Exception): # Custom exception for too many arguments
    """Exception raised when too many arguments are passed to a function."""
    pass 


def divide(dividend, divisor):
    """
    Divides the dividend by the divisor and returns the result.
    Raises a ZeroDivisionError if the divisor is zero.
    """
    if divisor == 0:
        raise ZeroDivisionError("division by zero")
    return dividend / divisor

def safe_divide(dividend, divisor):
    """
    Safely divides the dividend by the divisor.
    Returns None if a ZeroDivisionError occurs.
    """
    try:
        return divide(dividend, divisor)
    except ZeroDivisionError:
        return None
    
def main():
    # Example usage of divide function
    try:
        result = divide(10, 2)
        print("Result of division:", result)
    except ZeroDivisionError as e:
        print("Error:", e)

    # Example usage of safe_divide function
    result = safe_divide(10, 0)
    if result is None:
        print("Division by zero occurred, returning None.")
    else:
        print("Result of safe division:", result)

if __name__ == "__main__":
    main()