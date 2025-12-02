# STRING
# word = "APPLE"

# letter = input("Guess a letter: ")

# if letter in word:
#     print(f"{word} has {letter} in it.")
# else:
#     print(f"{letter} is not found.")

# SET
# students = {"Ashik", "Omar", "Fahad"}
# student = input("Write a student name: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} is not a student")

# DICTIONARY
# grades = {
#     "Saif": "B",
#     "Ashik": "A",
#     "Omar": "C"
# }

# student_name = input("Who's Grade you want to know? Write down his name: ")

# if student_name in grades:
#     print(f"{student_name} got {grades.get(student_name)}")
# elif student_name not in grades:
#     print(f"{student_name} not found.")


# EXERCISE
email = "saif@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("invalid email")