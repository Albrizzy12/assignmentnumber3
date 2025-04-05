def calculate_average(*args):
    valid_numbers = []

    for arg in args:
        while True:
            try:
                num = float(arg)
                valid_numbers.append(num)
                break
            except ValueError:
                arg = input(f"Invalid input '{arg}'. Please enter a valid number: ")

    if valid_numbers:
        return sum(valid_numbers) / len(valid_numbers)
    else:
        return 0


# Example usage:
# You can pass values manually here
result = calculate_average("10", "20", "abc", "40")
print("Average is:", result)