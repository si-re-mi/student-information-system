# Student Information System

A console-based Student Information System developed with **Python** and **SQLite**. The project demonstrates relational database design, normalization, SQL querying, and basic database management using Python.

## Features

- Relational database designed using normalization principles
- Separate entities for students, teachers, groups, subjects, and persons
- Student dormitory management
- Library management with book loans
- Scholarship records
- Student hobbies (many-to-many relationship)
- History of personal name changes
- Sample data generation
- Analytical SQL queries and reports


## Technologies

- Python 3
- SQLite
- SQL
- Git


## Database Structure

The database includes the following main entities:

- Persons
- Person Names
- Students
- Teachers
- Groups
- Subjects
- Grades
- Scholarships
- Dorm Rooms
- Books
- Book Loans
- Hobbies
- Student Hobbies


## Project Structure

student-information-system/
│
├── config/
│   └── config.py
│
├── database/
│   ├── create_db.py
│   └── fill_db.py
│
├── queries/
│   ├── queries.py
│   ├── sql_queries.py
│   └── query_utils.py
│
├── README.md
├── start.py
└── .gitignore


## Database Design

The project demonstrates the use of:

* Primary Keys
* Foreign Keys
* UNIQUE constraints
* CHECK constraints
* DEFAULT values
* One-to-Many relationships
* Many-to-Many relationships
* Historical data storage using validity periods (`valid_from`, `valid_to`)


## SQL Features

The project includes SQL queries using:

* INNER JOIN
* LEFT JOIN
* GROUP BY
* ORDER BY
* Aggregate Functions (`COUNT`, `AVG`, `SUM`)
* Subqueries
* Data filtering
* Analytical reports


## Running the Project

Clone the repository:

```bash
git clone https://github.com/si-re-mi/student-information-system.git
```

Navigate to the project folder:

```bash
cd student-information-system
```

Run:

```bash
python start.py
```

The application will:

1. Create a new SQLite database.
2. Create all database tables.
3. Populate the database with sample data.
4. Execute analytical SQL queries.
5. Display query results in the console.

---

## Example Output

```
Інформаційна система 'Студент'
Виконання проєкту...

Створення бази даних…
Базу даних створено.

Заповнення тестовими даними…
Дані додано.

Виконання запитів…

Рейтинг групи
('Іваненко', 'Іван', 94.33)
('Сидоренко', 'Марія', 91.33)
('Петренко', 'Петро', 80.33)
('Коваленко', 'Олена', 70.0)
('Шевченко', 'Андрій', 51.67)

Боржники бібліотеки
('Іваненко', 'Іван', 2, 220.0)
('Коваленко', 'Олена', 1, 250.0)

Рейтинг і стипендія студента
('Іваненко', 'Іван', 94.33, 2000.0)

Звіт успішності групи
('Іваненко Іван', 3, 0, 0, 0, 3)
('Коваленко Олена', 0, 2, 1, 0, 3)
('Петренко Петро', 0, 3, 0, 0, 3)
('Сидоренко Марія', 2, 1, 0, 0, 3)
('Шевченко Андрій', 0, 0, 2, 1, 3)

Найпопулярніші хобі
('Читання', 2)
('Програмування', 2)
('Шахи', 2)
('Футбол', 2)
('Подорожі', 1)

Зміна прізвища
('Петренко', 'Марія', 'Ігорівна')

Зміна прізвища
('Сидоренко', 'Марія', 'Ігорівна')

Усі операції виконані успішно.

Роботу завершенно.
```

---

## Learning Objectives

This project was created to practice:

* Database normalization
* Relational database design
* SQL querying
* Python interaction with SQLite
* Organizing a small Python project
* Writing reusable SQL queries

---

## Future Improvements

* CRUD operations
* Interactive console menu
* Search and filtering
* Export reports to CSV
* Unit tests
* Logging
* Database migrations

---

## Author

**Mykhailo Pavlenko**

GitHub: github.com/si-re-mi
linkedin.com/in/mykhailo-pavlenko-b5a340359