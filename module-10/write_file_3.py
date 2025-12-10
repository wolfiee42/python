# .csv


import json
import csv

employees = [
    ["Name", "age", "occupation"],
    ["Ashik", 22, "Business man"],
    ["Saif", 24, "Software Engineer"],
    ["Nahin", 25, "Data Scientist"],
]

file_path = "module-10/output.csv"

# with "w" method for json
try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
        
except FileExistsError:
    print("File already exists.")