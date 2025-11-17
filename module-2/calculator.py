# python calc

operator = input("select an operator (+ - * / ): ")
num1 = float(input("Enter first num: "))
num2 = float(input("Enter second num: "))


if operator == "+":
    result = num1+num2
    print(round(result, 2))
elif operator == "-":
    result = num1-num2
    print(round(result, 2))
elif operator == "*":
    result = num1*num2
    print(round(result, 2))
elif operator == "/":
    result = num1/num2
    print(round(result, 2))
else:
    print(f"{operator} is not a valid operator")


