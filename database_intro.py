#PYTHON + DATABASE CONNECTION (SQLITE)
#SQLite is a small database built into python, perfect for learning and no installation, used in many beginner projects, teaches database thinking.
import sqlite3
#What is SQLite? It is a built-in Python library that lets Python create and talk to databases. It is a great way to learn about databases without needing to set up a separate database server.
#Creating a connection to a SQLite database (or creating the database if it doesn't exist)\
#Create Database Connection
connection = sqlite3.connect("student.db")
#What happens? Python creates: student.db inside your project folder. This file is your database where all your data will be stored.
#Real-life example: Creating a student.db is like opening a new Excel workbook.
#Create Cursor Object:
cursor = connection.cursor()
#What is a Cursor? Cursor is like a messenger. It sends SQL commands into the database.
#Flow: Python code -> Cursor -> Database -> Cursor -> Python code
#Create a Table:
cursor.execute("""
               CREATE TABLE IF NOT EXISTS student(
               name TEXT,
               Marks INTEGER)
               """)
#Real Database Example: Tables are like Excel sheets. Columns: NAME, MARKS. Rows hold data.
#Save Changes:
connection.commit()
#Why commit? Database changes stay temporary until committed. commit means "save permanently".
#Close Database Connection:
connection.close()
#Why Close Connection? Close connection after work is done. Professional habit
print("Database created and table student created successfully!")  

import sqlite3
connection = sqlite3.connect("student.db")
cursor = connection.cursor()
cursor.execute("""INSERT INTO student VALUES ('Joseph', 90)""")
connection.commit()
connection.close()
print("Student added successfully!")