import random

def spin_row():
    items = ["🍇", "🍉", "🍋", "🍓", "🥑"]
    return [random.choice(items) for _ in range(3)]

def print_row(row):
    print(" ".join(row))

def get_balance(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍇":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 6
        elif row[0] == "🥑":
            return bet * 8
        elif row[0] == "🍓":
            return bet * 10
    return 0


def main():
    
    balance = 100

    print("Welcome to python slot")
    print(" 🍇 🍉 🍋 🥑 🍓 ")

    while balance > 0:
        print(f"your current balance ${balance}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid input")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient balance")

        elif bet < 0:
            print("Can not be 0")

        balance -= bet
        row = spin_row()
        print_row(row)

        new_balance = get_balance(row, bet)

        if new_balance > 0:
            print(f"hurray You won {new_balance}")
        else:
            print("Sorry, you lost the game.")

        balance += new_balance

        opinion = input("Do you want to play again? (Y/N)\n").upper()

        if not opinion == "Y":
            print(f"Your Current Balance is {balance}")
            break
        else:
            continue

if __name__ == "__main__":
    main()