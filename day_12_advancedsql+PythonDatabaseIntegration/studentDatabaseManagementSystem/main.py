from database import create_database
from operations import *

create_database()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Sort By Marks")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        marks = float(input("Marks: "))

        add_student(name, age, marks)

        print("Student added successfully.")

    elif choice == "2":
        view_students()

    elif choice == "3":
        student_id = int(input("Student ID: "))
        marks = float(input("New Marks: "))

        update_marks(student_id, marks)

        print("Marks updated successfully.")

    elif choice == "4":
        student_id = int(input("Student ID: "))

        delete_student(student_id)

        print("Student deleted successfully.")

    elif choice == "5":
        name = input("Enter name to search: ")

        search_student(name)

    elif choice == "6":
        sort_by_marks()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")