def classify_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

while True:
    try:
        user_input = int(input("Enter an integer: "))
        print("The number is:", classify_number(user_input))
        break  # Exit loop after a valid input
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
