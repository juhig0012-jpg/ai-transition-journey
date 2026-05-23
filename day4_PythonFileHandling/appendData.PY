with open("notes.txt", "a") as file:
    file.write("\nNew line added")
with open("notes.txt", "r") as file:
    file_content = file.read()
print(file_content)