# PSHS Secure Club Registration System

# Allowed values for the registration system
allowed_sections = ["Dahlia"]
allowed_clubs = ["Robotics", "Science", "Mathematics", "Programming"]
allowed_attendance = ["Present", "Absent", "Late"]

# Assume the registration is valid until an error is found
registration_valid = True

# Get the student's name
student_name = input("Enter student name: ")

# Validate that the name is not blank
if student_name.strip() == "":
    print("Student name is required.")
    registration_valid = False

# Get and validate the student's section
section = input("Enter section: ")

if section not in allowed_sections:
    print("Invalid section.")
    registration_valid = False

# Get and validate the student's club choice
club_choice = input("Enter club choice: ")

if club_choice not in allowed_clubs:
    print("Please choose a valid club.")
    registration_valid = False

# Get and validate the school email
school_email = input("Enter school email: ")

if "@" not in school_email or "." not in school_email:
    print("Invalid school email.")
    registration_valid = False

# Get and validate attendance status
attendance_status = input("Enter attendance status: ")

if attendance_status not in allowed_attendance:
    print("Invalid attendance status.")
    registration_valid = False

# Display the final registration result
if registration_valid:
    print("REGISTRATION ACCEPTED")
    print("Student:", student_name)
    print("Section:", section)
    print("Club:", club_choice)
    print("Email:", school_email)
    print("Attendance:", attendance_status)
else:
    print("REGISTRATION NOT ACCEPTED")
