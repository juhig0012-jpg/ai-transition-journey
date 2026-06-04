CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
);

INSERT INTO students (id, name, marks) VALUES
(1, 'Rahul', 90),
(2, 'Amit', 75),
(3, 'Sita', 85),
(4, 'Neha', 60),
(5, 'Karan', 95);

SELECT *
FROM students
ORDER BY marks DESC
LIMIT 1;

SELECT AVG(marks) AS average_marks
FROM students;

SELECT *
FROM students
ORDER BY marks DESC;

SELECT *
FROM students
ORDER BY marks ASC;

SELECT *
FROM students
WHERE marks > (SELECT AVG(marks) FROM students);