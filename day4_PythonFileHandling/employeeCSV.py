import csv

FILE_NAME = "employees.csv"

# Employee data
employees = [
    ["Name", "Salary", "Department"],
    ["Amit", 50000, "IT"],
    ["Neha", 65000, "HR"],
    ["Rahul", 80000, "Finance"],
    ["Priya", 72000, "Marketing"]
]

# Create CSV file
with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(employees)

print("Employee CSV file created successfully.\n")

# Read CSV and print employees
print("Employee Records:")
with open(FILE_NAME, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    employee_list = []

    for row in reader:
        employee_list.append(row)

        print(
            f"Name: {row['Name']}, "
            f"Salary: {row['Salary']}, "
            f"Department: {row['Department']}"
        )

# Find employee with highest salary
highest_salary_employee = max(
    employee_list,
    key=lambda emp: int(emp["Salary"])
)

print("\nHighest Salary Employee:")
print(
    f"Name: {highest_salary_employee['Name']}, "
    f"Salary: {highest_salary_employee['Salary']}, "
    f"Department: {highest_salary_employee['Department']}"
)