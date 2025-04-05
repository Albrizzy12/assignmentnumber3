# Define custom exception
class NegativeNumberError(Exception):
    """Exception raised for errors in the input if the number is negative."""
    def __init__(self, number):
        self.number = number
        self.message = f"NegativeNumberError: {number} is a negative number."
        super().__init__(self.message)

# Function that checks for positive numbers
def check_positive(number):
    if number < 0:
        raise NegativeNumberError(number)
    else:
        print(f"{number} is positive.")

# Demonstration using try block
try:
    num = int(input("Enter a number: "))
    check_positive(num)
except NegativeNumberError as e:
    print(e)
