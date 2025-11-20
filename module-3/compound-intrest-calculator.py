principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can not be less than or equal to 0")
    else:
        break

while True:
    rate = float(input("Enter the intrest rate: "))
    if rate < 0:
        print("intrest rate can not be less than or equal to 0")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("time can not be less than or equal to 0")
    else:
        break
    
total = principle * pow((1 + rate /100), time)

print(f"Balance after {time} year/s: ${total:.2f}")