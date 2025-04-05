# List of names to write
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

# Write names to the file
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Read names from the file and print them
with open("names.txt", "r") as file:
    print("Names in the file:")
    for line in file:
        print(line.strip())
