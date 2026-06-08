import sqlite3

def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        marks REAL
    )
    """)

    conn.commit()
    conn.close()