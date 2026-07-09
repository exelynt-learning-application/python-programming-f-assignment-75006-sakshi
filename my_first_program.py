# My First Python Program
# This program demonstrates variables, input/output operations,
# type casting, arithmetic operations, and type checking.

print("===== Welcome to My First Python Program =====")

# Take user input
name = input("Enter your name: ")

# Type casting numeric inputs
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
favorite_number = float(input("Enter your favorite number: "))

# Display user details
print("\n===== User Details =====")
print("Name            :", name)
print("Age             :", age)
print("Height (meters) :", height)
print("Favorite Number :", favorite_number)

# Display data types
print("\n===== Data Types =====")
print("Type of name            :", type(name))
print("Type of age             :", type(age))
print("Type of height          :", type(height))
print("Type of favorite_number :", type(favorite_number))

# Perform arithmetic operation
total = age + favorite_number

# Display result
print("\n===== Arithmetic Operation =====")
print("Age + Favorite Number =", total)

print("\nThank you for using My First Python Program!")
