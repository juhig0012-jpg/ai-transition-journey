crud operations in python using sqlite3
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
# update data
cursor.execute("UPDATE Student SET AGE = 21 WHERE NAME = 'Alice'")
conn.commit()
# delete data
cursor.execute("DELETE FROM Student WHERE NAME = 'Bob'")
conn.commit()
# select data after update and delete
cursor.execute("SELECT * FROM Student")
rows = cursor.fetchall()
for row in rows:
    print(row)
# close connection
conn.close()

searching for students with age 20
import sqlite3
# connect to database
conn = sqlite3.connect('student.db')
# create cursor
cursor = conn.cursor()
# search for students with age 20
cursor.execute("SELECT * FROM Student WHERE AGE = 20")
rows = cursor.fetchall()
for row in rows:
    print(row)
# close connection
conn.close()