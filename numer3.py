def get_valid_number():
    while True:
        try:
            user_input = input("Enter a number: ")
            number = float(user_input)  # Change to int(user_input) if you want integers only
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the function
number = get_valid_number()
print("You entered:", number)

