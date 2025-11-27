def happy_birthday(name, age):
    print(f"happy birthday to {name}!")
    print(f"how are {age} years old!")

# happy_birthday("saif", 24)
# happy_birthday("ashik", 22)
# happy_birthday("suhail", 23)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"your amount is ${amount:.2f} and it's due date is {due_date}")

display_invoice("ashik", 43.2, "01/06/26")