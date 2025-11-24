# Shopping cart program 

foods = []
prices = []
total = 0

while True:
    food = input("Enter your product: (press q to quit) ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the {food} price: $"))
        foods.append(food)
        prices.append(price)

for price in prices:
    total += price

print("--------------- Your cart items are -------------------")
for food in foods:
    print(food)
print(f"Your total bill is: ${total}")

print("---------- Thank you for Shopping with us -------------")