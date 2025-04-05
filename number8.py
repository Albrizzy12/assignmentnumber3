import random

def generate_random_numbers(count, start, end):
    """Generates a list of random integers."""
    return [random.randint(start, end) for _ in range(count)]

def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    return sum(numbers) / len(numbers)

# Main Program
random_numbers = generate_random_numbers(10, 1, 100)
average = calculate_average(random_numbers)

print("Generated numbers:", random_numbers)
print("Average:", average)
