class StudentRankingSystem:
    def __init__(self):
        self.students = []

    # Add Student
    def add_student(self, roll_no, name, marks):
        self.students.append({
            "roll_no": roll_no,
            "name": name,
            "marks": marks
        })

    # Sort by Marks (Highest First)
    def sort_by_marks(self):
        self.students.sort(
            key=lambda student: student["marks"],
            reverse=True
        )

    # Search Student by Name
    def search_student(self, name):
        for student in self.students:
            if student["name"].lower() == name.lower():
                return student

        return None

    # Find Topper
    def find_topper(self):
        if not self.students:
            return None

        return max(
            self.students,
            key=lambda student: student["marks"]
        )

    # Binary Search by Roll Number
    def binary_search_roll(self, roll_no):

        # Sort by roll number first
        self.students.sort(
            key=lambda student: student["roll_no"]
        )

        left = 0
        right = len(self.students) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.students[mid]["roll_no"] == roll_no:
                return self.students[mid]

            elif self.students[mid]["roll_no"] < roll_no:
                left = mid + 1

            else:
                right = mid - 1

        return None

    # Display Students
    def display(self):
        for student in self.students:
            print(student)


# Driver Code
system = StudentRankingSystem()

system.add_student(101, "Rahul", 90)
system.add_student(102, "Ananya", 95)
system.add_student(103, "Vikas", 85)
system.add_student(104, "Priya", 92)

print("All Students:")
system.display()

# Sort by Marks
system.sort_by_marks()

print("\nRanking:")
system.display()

# Search Student
print("\nSearch Rahul:")
print(system.search_student("Rahul"))

# Find Topper
print("\nTopper:")
print(system.find_topper())

# Binary Search by Roll Number
print("\nSearch Roll No 103:")
print(system.binary_search_roll(103))