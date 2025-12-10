import json

file_path = "module-10/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["data"][1]["name"])
        
except FileNotFoundError:
    print("That file was not found")
    
except PermissionError:
    print("You do not have permission to read that file")