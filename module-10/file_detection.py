# relative file path                   /folder/text.txt
# absolute file path                   C:/User/Wolfie/text.txt

import os

file_path = "module-10/text.txt"
# file_path = "module-10"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exist.")
    
    if os.path.isfile(file_path):
        print("That is a file")
        
    elif os.path.isdir(file_path):
        print("That is a folder")
else:
    print("The location doesn't exist.")