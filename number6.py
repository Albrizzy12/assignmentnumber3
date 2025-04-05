def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input type. Please enter numbers only.")

# Example usage:
print("Result:", divide_numbers(10, 2))     # Should print 5.0
print("Result:", divide_numbers(10, 0))     # Should print error for division by zero
print("Result:", divide_numbers(10, 'a'))   # Should print error for invalid type
