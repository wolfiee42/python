num = 6
a = 5
b = 6
age = 13
user_role = "admin"


result = "Even" if num%2==0 else "Odd"
max_num = a if a>b else b
min_num = a if a<b else b
status = "Adult" if age >= 18 else "Child"
access_level = "Full access" if user_role == "admin" else "Limited access"
# print("Positive" if num > 0 else "Negative")
print(access_level)
