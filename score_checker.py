# Ask the user to enter a student score
score = int(input("Enter student score: "))

# Check whether the score is within the valid range of 0 to 100
if score < 0 or score > 100:
    print("Invalid Score.")

# Classify the valid score based on its range
elif score >= 90:
    print("Outstanding.")
elif score >= 80:
    print("Very satisfactory.")
elif score >= 75:
    print("Satisfactory.")
else:
    print("Needs improvement.")
