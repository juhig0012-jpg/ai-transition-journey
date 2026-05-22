class StudentGrades:
    def __init__(self, student_name):
        self.student_name = student_name
        self.grades = []

    # Add a grade
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100")

    # Calculate average grade
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    # Display all grades
    def display_grades(self):
        print(f"Grades for {self.student_name}: {self.grades}")

# Example usage
student = StudentGrades("Rahul")

student.add_grade(85)
student.add_grade(90)
student.add_grade(78)

student.display_grades()

average = student.get_average()
print("Average Grade:", average)