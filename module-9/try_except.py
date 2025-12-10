# ValueError
# ZeroDivisionError

try:
    number = int(input("Enter a number: "))
    print(1/number)

except ValueError:
    print("Only interger please")
    
except ZeroDivisionError:
    print("You can not divide with 0 IDIOT")
    
except Exception:
    print("Something went wrong!")
    
finally:
    print("Do some cleanup here.")