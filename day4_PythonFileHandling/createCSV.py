import csv

data = [
    ["Name", "Marks"],
    ["Rahul", 90],
    ["Ananya", 95]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(data)