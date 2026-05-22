class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def details(self):
        print(f"{self.name} | Age: {self.age} | Marks: {self.marks}")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        self.students = [s for s in self.students if s.name != name]

    def list_students(self):
        for s in self.students:
            s.details()

    def find_student(self, name):
        for s in self.students:
            if s.name == name:
                s.details()
                return
        print("Student not found")

# usage
manager = StudentManager()
manager.add_student(Student("Rahul", 25, 90))
manager.add_student(Student("Ananya", 22, 95))

manager.list_students()
manager.find_student("Rahul")
manager.remove_student("Ananya")
manager.list_students()