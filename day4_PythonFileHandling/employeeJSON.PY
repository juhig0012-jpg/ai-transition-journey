import json

FILE_NAME = "employees.json"

# Employee data
employees = [
    {
        "name": "Amit",
        "salary": 50000,
        "department": "IT"
    },
    {
        "name": "Neha",
        "salary": 65000,
        "department": "HR"
    },
    {
        "name": "Rahul",
        "salary": 80000,
        "department": "Finance"
    },
    {
        "name": "Priya",
        "salary": 72000,
        "department": "Marketing"
    }
]

# Create JSON file
with open(FILE_NAME, "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

print("Employee JSON file created successfully.\n")

# Read JSON file
with open(FILE_NAME, "r", encoding="utf-8") as file:
    employee_data = json.load(file)

print("Employee Records:")
for emp in employee_data:
    print(
        f"Name: {emp['name']}, "
        f"Salary: {emp['salary']}, "
        f"Department: {emp['department']}"
    )

# Search employee by name
search_name = input("\nEnter employee name to search: ")

found = False

for emp in employee_data:
    if emp["name"].lower() == search_name.lower():
        print("\nEmployee Found:")
        print(
            f"Name: {emp['name']}, "
            f"Salary: {emp['salary']}, "
            f"Department: {emp['department']}"
        )
        found = True
        break

if not found:
    print("\nEmployee not found.")