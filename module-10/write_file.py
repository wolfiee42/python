# .txt , .json, .csv

txt_data = "i like shawarma"

file_path = "module-10/output.txt"


# with "w" method
# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path}' is created")


# with "x" method
# try:
#     with open(file_path, "x") as file:
#         file.write(txt_data)
#         print(f"txt file '{file_path} is created'")

# except FileExistsError:
#     print("File already exists.")


# with "a" method
with open(file_path, "a") as file:
    file.write("\n" + txt_data)
    print(f"txt file '{file_path}' is created")