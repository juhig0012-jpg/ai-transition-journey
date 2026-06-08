-- connect to database in python
import sqlite3
# connect to database
conn = sqlite3.connect('student.db')
# create cursor
cursor = conn.cursor()
# create table
cursor.execute('''
CREATE TABLE Student (
    ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    AGE INTEGER
)''')
# insert data
cursor.execute("INSERT INTO Student (NAME, AGE) VALUES ('Alice', 20)")
cursor.execute("INSERT INTO Student (NAME, AGE) VALUES ('Bob', 22)")
cursor.execute("INSERT INTO Student (NAME, AGE) VALUES ('Charlie', 20)")
# commit changes
conn.commit()
# select data
cursor.execute("SELECT * FROM Student")
rows = cursor.fetchall()
for row in rows:
    print(row)
# close connection
conn.close()





