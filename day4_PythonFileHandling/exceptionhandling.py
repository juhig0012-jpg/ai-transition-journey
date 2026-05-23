try:
    with open("abc.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist")