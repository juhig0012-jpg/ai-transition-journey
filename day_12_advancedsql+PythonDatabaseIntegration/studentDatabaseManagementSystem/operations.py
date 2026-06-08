import sqlite3

DB_NAME = "students.db"


def add_student(name, age, marks):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age, marks) VALUES (?, ?, ?)",
        (name, age, marks)
    )

    conn.commit()
    conn.close()


def view_students():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    if not students:
        print("\nNo students found.\n")
        return

    print("\nID\tName\tAge\tMarks")
    print("-" * 35)

    for student in students:
        print(
            f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}"
        )


def update_marks(student_id, new_marks):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET marks=? WHERE id=?",
        (new_marks, student_id)
    )

    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()


def search_student(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    results = cursor.fetchall()

    conn.close()

    if results:
        print("\nSearch Results:")
        for row in results:
            print(row)
    else:
        print("Student not found.")


def sort_by_marks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students ORDER BY marks DESC"
    )

    students = cursor.fetchall()

    conn.close()

    print("\nStudents Sorted By Marks")

    for student in students:
        print(student)