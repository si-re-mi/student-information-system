import os
import sqlite3

if os.path.exists("student.db"):
    os.remove("student.db")

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.executescript("""

CREATE TABLE groups (
id INTEGER PRIMARY KEY AUTOINCREMENT,
group_name TEXT NOT NULL,
specialty TEXT,
monitor_student_id INTEGER
);



CREATE TABLE persons (
id INTEGER PRIMARY KEY AUTOINCREMENT,

birth_date DATE,
birth_place TEXT,
address TEXT,
gender TEXT,
marital_status TEXT
);



CREATE TABLE person_names (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    person_id INTEGER NOT NULL,

    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    middle_name TEXT,

    valid_from DATE NOT NULL,
    valid_to DATE,

    FOREIGN KEY(person_id) REFERENCES persons(id)
);



CREATE TABLE dorm_rooms (
id INTEGER PRIMARY KEY AUTOINCREMENT,
room_number TEXT UNIQUE NOT NULL,
capacity INTEGER DEFAULT 3
);



CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
person_id INTEGER NOT NULL,
education_identifier BIGINT NOT NULL,
student_card_number TEXT UNIQUE NOT NULL,
group_id INTEGER,
scholarship_amount REAL DEFAULT 0,
room_id INTEGER,

FOREIGN KEY(person_id) REFERENCES persons(id),
FOREIGN KEY(group_id) REFERENCES groups(id),
FOREIGN KEY(room_id) REFERENCES dorm_rooms(id)
);



CREATE TABLE teachers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
person_id INTEGER NOT NULL,
FOREIGN KEY(person_id) REFERENCES persons(id)
);



CREATE TABLE subjects (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
teacher_id INTEGER NOT NULL,
FOREIGN KEY(teacher_id) REFERENCES teachers(id)
);



CREATE TABLE grades (
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER NOT NULL,
subject_id INTEGER NOT NULL,
points INTEGER CHECK(points BETWEEN 0 AND 100),
national_grade TEXT CHECK(
    national_grade IN
    ('Відмінно','Добре',
     'Задовільно','Незадовільно')
),
semester TEXT,
FOREIGN KEY(student_id) REFERENCES students(id),
FOREIGN KEY(subject_id) REFERENCES subjects(id)
);



CREATE TABLE scholarships (
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER NOT NULL,
semester TEXT,
amount REAL NOT NULL,
FOREIGN KEY(student_id) REFERENCES students(id)
);



CREATE TABLE hobbies (
id INTEGER PRIMARY KEY AUTOINCREMENT,
hobby_name TEXT NOT NULL UNIQUE
);



CREATE TABLE student_hobbies (
student_id INTEGER,
hobby_id INTEGER,
PRIMARY KEY(student_id, hobby_id),
FOREIGN KEY(student_id) REFERENCES students(id),
FOREIGN KEY(hobby_id) REFERENCES hobbies(id)
);



CREATE TABLE books (
id INTEGER PRIMARY KEY AUTOINCREMENT,
inventory_number TEXT UNIQUE NOT NULL,
title TEXT NOT NULL,
author TEXT NOT NULL,
genre TEXT,
price REAL NOT NULL
);



CREATE TABLE book_loans (
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER NOT NULL,
book_id INTEGER NOT NULL,
loan_date DATE NOT NULL,
return_date DATE,
FOREIGN KEY(student_id) REFERENCES students(id),
FOREIGN KEY(book_id) REFERENCES books(id)
);
""")

conn.commit()
conn.close()

print("Базу даних створено.")
