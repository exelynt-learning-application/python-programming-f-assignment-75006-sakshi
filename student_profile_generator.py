# Student Profile Generator

# Store student details
student_name = "Shivani Yadav"      # String
age = 21                            # Integer
course_fee = 50000.0                # Float
is_enrolled = True                  # Boolean

# Display student details
print("===== Student Profile =====")
print("Student Name :", student_name)
print("Age          :", age)
print("Course Fee   :", course_fee)
print("Enrolled     :", is_enrolled)

# Display data types
print("\n===== Data Types =====")
print("student_name :", type(student_name))
print("age          :", type(age))
print("course_fee   :", type(course_fee))
print("is_enrolled  :", type(is_enrolled))

# Perform operations
tax = course_fee * 0.10   # 10% tax
course_fee = course_fee + tax

age = age + 1             # Increment age
is_enrolled = False       # Update enrollment status

# Display updated details
print("\n===== Updated Student Profile =====")
print("Student Name :", student_name)
print("Updated Age  :", age)
print("Updated Fee  :", course_fee)
print("Enrolled     :", is_enrolled)

# Display updated data types
print("\n===== Updated Data Types =====")
print("student_name :", type(student_name))
print("age          :", type(age))
print("course_fee   :", type(course_fee))
print("is_enrolled  :", type(is_enrolled))
