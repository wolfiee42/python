#  shopping cart

item = input("What would you like to buy?: ")
quantity = int(input("How many of them?: "))
price = float(input("What is the price?: "))

total = quantity*price

print(f"You have bought {quantity}x {item}/s")
print(f"the price is ${total}")