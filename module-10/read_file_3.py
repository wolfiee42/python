import csv

file_path = "module-10/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        
        for line in content:
            print(line)
        
except FileNotFoundError:
    print("That file was not found")
    
except PermissionError:
    print("You do not have permission to read that file")