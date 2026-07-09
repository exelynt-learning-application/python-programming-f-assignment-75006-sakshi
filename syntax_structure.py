# syntax_structure.py

# Program Title
print("===== Python Syntax & Indentation Demonstration =====")

# Top-level print statements
print("Welcome to the Python Syntax Demo.")
print("This program demonstrates indentation and nested blocks.")
print("Python uses indentation to define code blocks.")

number = 15

# The if block starts here.
# Indentation is required because Python uses spaces to identify
# which statements belong to the if block.
if number > 10:
    print("The number is greater than 10.")

    # Nested block starts here.
    # This block is inside the if statement and must be indented further.
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
    # Nested block ends here.

    print("End of the if block.")

# The if block ends here.

print("Program executed successfully.")
