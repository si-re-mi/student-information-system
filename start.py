import os
from database.create_db import create_database
from database.fill_db import fill_database
from queries.queries import run_queries
    
print("Інформаційна система 'Студент'")
print("Виконання проєкту...")

print("\nСтворення бази даних…")
create_database()

print("\nЗаповнення тестовими даними…")
fill_database()

print("\nВиконання запитів…")
run_queries()

print("\nУсі операції виконані успішно.")
print("\nРоботу завершенно.")