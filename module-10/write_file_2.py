# .json

# list
# employees = ["Saif", "Nahin", "Maher", "Ashik" ]

import json

employees = {
    "data": [
        {
            "name": "ashik",
            "age": 20,
            "occupation": "Business man"
        },
        {
            "name": "saif",
            "age": 24,
            "occupation": "Software Engineer"
        },
    ]
}

# file_path = "module-10/output.txt"  // for list
file_path = "module-10/output.json"


# with "w" method for list
# with open(file_path, "w") as file:
#     for employee in employees:
#         file.write(employee + " ")
#     print(f"txt file '{file_path}' is created")


# with "w" method for json
with open(file_path, "w") as file:
    json.dump(employees, file, indent=4)
    print(f"json file '{file_path}' was created")
    # print(f"txt file '{file_path}' is created")

