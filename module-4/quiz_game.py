questions = (
    "What do plants need to make their own food?",
    "Which part of your body helps you think?",
    "What is the largest planet in our solar system?",
    "What do bees collect from flowers?",
    "Which gas do humans need to breathe?",
)

options = (
    ("A. Moonlight","B. Soil only","C. Sunlight","D. Wind"),
    ("A. Heart","B. Brain","C. Lungs","D. Stomach"),
    ("A. Earth","B. Mars","C. Jupiter","D. Venus"),
    ("A. Stones","B. Water","C. Nectar","D. Leaves"),
    ("A. Carbon dioxide","B. Nitrogen","C. Oxygen","D. Helium")
)

correct_answers = (
    "C",
    "B",
    "C",
    "C",
    "C",
)

guesses = []

questions_num = 0

score = 0

for question in questions:
    print("---------------------------")
    print(question)
    for option in options[questions_num]:
        print(option) 
    
    guess = input(" Enter your answer: ")
    guesses.append(guess.upper())
    
    if correct_answers[questions_num] == guesses[questions_num]:
        score+=1
    
    questions_num+=1

    
    
print("---------------------------")

print("Correct answers are: ", end=" ")
for correct_answer in correct_answers:
    print(correct_answer, end=" ")

print()

print("Your answers are:    ", end=" ")
for guess in guesses:
    print(guess, end=" ")

print()

total = int((score*100)/len(questions))
print(f"Your score is {total}%")