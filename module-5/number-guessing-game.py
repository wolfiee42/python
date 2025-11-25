import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses = 0
isRunning = True

while isRunning:

    print(f"Select a number between {lowest_num} and {highest_num}")
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses+=1

        if guess < lowest_num and guess > highest_num:
            print("Out of range")
            print(f"Select a number bet50ween {lowest_num} and {highest_num}")

        elif guess > answer:
            print("too high")

        elif guess < answer:
            print("too low")

        else:
            print(f"There, you have it. the number was {answer} and it took you {guesses} attempts to guess it.")
            isRunning = False

    else:
        print("invalid guess")
        