# validate user input
# username no more than 12 character
# can not contain spaces
# can not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("your username can not be more than 12 characters")
elif not username.find(" ") == -1:
    print(" your username can not contain space")
elif not username.isalpha():
    print("your username can not contain numbers")