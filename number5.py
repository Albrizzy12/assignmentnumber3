# Sample list of temperatures in Celsius
celsius_temps = [0, 10, 20, 25, 30, 37, 100]

# Convert to Fahrenheit using lambda and map
fahrenheit_temps = list(map(lambda c: c * 9 / 5 + 32, celsius_temps))

# Print the converted list
print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)
