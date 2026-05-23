import json

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Save")
    print("4. Load")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        marks = int(input("Marks: "))

        students.append({
            "name": name,
            "marks": marks
        })

    elif choice == "2":
        for student in students:
            print(student)

    elif choice == "3":
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

    elif choice == "4":
        with open("students.json", "r") as file:
            students = json.load(file)

    elif choice == "5":
        break