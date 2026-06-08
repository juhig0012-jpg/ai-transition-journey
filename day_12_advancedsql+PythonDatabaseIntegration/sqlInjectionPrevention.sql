-- sql injection prevention
-- use parameterized queries instead of string concatenation
-- example in Python using psycopg2
import psycopg2
def get_user_by_id(user_id):
    conn = psycopg2.connect("dbname=test user=postgres password=secret")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user
-- use stored procedures to encapsulate SQL logic
-- example in MySQL
DELIMITER //
CREATE PROCEDURE GetUserById(IN user_id INT)
BEGIN
    SELECT * FROM users WHERE id = user_id;
END //
DELIMITER ;
-- use ORM (Object-Relational Mapping) frameworks to abstract away SQL queries
-- example in Python using SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User
engine = create_engine('postgresql://postgres:secret@localhost/test')
Session = sessionmaker(bind=engine)
session = Session()
def get_user_by_id(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    return user
-- use input validation and sanitization to prevent malicious input
-- example in Python using regular expressions
import re
def validate_user_id(user_id):

    if re.match(r'^\d+$', user_id):
        return True
    else:
        return False
-- use least privilege principle for database users
-- create a separate database user with limited permissions for the application
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'app_password';
GRANT SELECT, INSERT, UPDATE, DELETE ON test.* TO 'app_user'@'localhost';
-- revoke unnecessary permissions from the default database user
RENAME USER 'postgres'@'localhost' TO 'admin_user'@'localhost';

REVOKE ALL PRIVILEGES ON *.* FROM 'admin_user'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON test.* TO 'admin_user'@'localhost';
-- use database firewalls and intrusion detection systems to monitor and block suspicious activity
-- example: use MySQL Enterprise Firewall to block SQL injection attempts
CREATE TABLE firewall_rules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rule_name VARCHAR(255) NOT NULL,
    rule_pattern VARCHAR(255) NOT NULL,
    action ENUM('ALLOW', 'BLOCK') NOT NULL
);
INSERT INTO firewall_rules (rule_name, rule_pattern, action) VALUES
('Block SQL Injection', '.*(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|--|#).*', 'BLOCK');

-- prepared statements and parameterized queries are the most effective way to prevent SQL injection attacks, as they ensure that user input is treated as data rather than executable code. Additionally, using stored procedures, ORM frameworks, input validation, and least privilege principles can further enhance the security of your database applications.
-- in python, you can use the built-in sqlite3 module to create parameterized queries and prevent SQL injection attacks. Here's an example:
import sqlite3
def get_user_by_id(user_id):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user
-- in this example, the "?" placeholder is used to indicate where the user input should be inserted, and the user_id variable is passed as a parameter to the execute() method. This ensures that the user input is properly escaped and prevents any malicious SQL code from being executed.


