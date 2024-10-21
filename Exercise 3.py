"""
Assessment1-Programming-Skills-Portfolio Exercise 3: Biography
"""

# Create a dictionary to store user information
values = {
    "name": "", # Prompt for user's name
    "hometown": "",# Prompt for user's hometown
    "age": 0,      # Initialize age
}

# Get user input for name and hometown
values["name"] = input("Enter your name: ")
values["hometown"] = input("Enter your hometown: ")

# Get user input for age with error handling
while True:
    try:
        values["age"] = int(input("Enter your age: "))# Convert input to an integer
        break# Exit loop if input is valid
    except ValueError:
        print("You need to enter a valid number for age.")# Error message for invalid input

# Display the collected user information
print(values["name"])
print(values["hometown"])
print(values["age"])
