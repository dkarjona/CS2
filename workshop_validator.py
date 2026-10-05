# PSHS Workshop Registration Validator

# Assume the registration is valid until an error is found
registration_valid = True

# Get the student's name. 
student_name = input("Enter student name: ")

if student_name.strip() == "":
    print("Student name is required.")
    registration_valid = False

# Get the student's age. 
age_input = input("Enter age: ")

try:
    age = int(age_input)

    if age < 11 or age > 18:
        print("Age must be from 11 to 18.")
        registration_valid = False

except ValueError:
    print("Age must be a number.")
    registration_valid = False
    age = age_input

# Get the student's grade level. 
grade_input = input("Enter grade level: ")

try:
    grade_level = int(grade_input)

    if grade_level not in [7, 8, 9, 10, 11, 12]:
        print("Invalid grade level.")
        registration_valid = False

except ValueError:
    print("Invalid grade level.")
    registration_valid = False
    grade_level = grade_input

# Get the email. 
email = input("Enter email: ")

if "@" not in email or "." not in email:
    print("Invalid email address.")
    registration_valid = False

# Get the registration code. 
registration_code = input("Enter registration code: ")

if len(registration_code) != 6:
    print("The registration code must contain exactly 6 characters.")
    registration_valid = False

# Display the final registration result
if registration_valid:
    print("REGISTRATION ACCEPTED.")
    print("Student:", student_name)
    print("Age:", age)
    print("Grade Level:", grade_level)
    print("Email:", email)
    print("Registration Code:", registration_code)
else:
    print("REGISTRATION NOT ACCEPTED.")
