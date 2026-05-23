import json

student = {
    "name": "Rahul",
    "age": 25,
    "marks": 90
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)