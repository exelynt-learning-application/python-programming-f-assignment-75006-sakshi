# Type Conversion Practice Program

print("===== Type Conversion Practice Program =====")

# Accept user input
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Type casting
int_num1 = int(num1)
int_num2 = int(num2)

float_num1 = float(num1)
float_num2 = float(num2)

# Arithmetic operations using integer values
addition = int_num1 + int_num2
subtraction = int_num1 - int_num2
multiplication = int_num1 * int_num2
division = int_num1 / int_num2

# Display converted values
print("\n===== Converted Values =====")
print("Integer Value 1 :", int_num1)
print("Integer Value 2 :", int_num2)
print("Float Value 1   :", float_num1)
print("Float Value 2   :", float_num2)

# Display data types
print("\n===== Data Types =====")
print("Type of int_num1   :", type(int_num1))
print("Type of int_num2   :", type(int_num2))
print("Type of float_num1 :", type(float_num1))
print("Type of float_num2 :", type(float_num2))

# Display arithmetic results
print("\n===== Arithmetic Operations =====")
print("Addition       :", addition)
print("Subtraction    :", subtraction)
print("Multiplication :", multiplication)
print("Division       :", division)

# Convert numeric value to string
result_string = str(addition)

print("\n===== String Conversion =====")
print("Addition as a string is:", result_string)
print("Type of result_string:", type(result_string))
