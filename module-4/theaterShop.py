menu = {
    "popcorn": 6.00,
    "chips": 1.00,
    "pizza": 3.00,
    "fries": 2.50,
    "soda": 3.00,
    "lemonade": 4.25 
}


cart = []
total = 0.00


print("--------Menu-------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-------------------")



while True:
    food = input("Select an item: (press q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)

print("======== Your bill =======")
print(f"Your total: ${total:.2f}")