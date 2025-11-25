import random

options = ("rock", "paper", "scissors")
is_playing = True


while is_playing:
    
    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("select (rock, paper, scissors): ")

    print(f"you: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("it is a tie.")

    elif player == "rock" and computer == "scissors":
        print("You win")

    elif player == "paper" and computer == "rock":
        print("you win")

    elif player == "scissors" and computer == "paper":
        print("you win")
        
    else:
        print("you lose")
    
    if not input("play again? (y/n): ").lower() == "y":
        is_playing = False
print()
print("Thank you for playing")