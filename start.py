import os
print("Інформаційна система 'Студент'")
print("Виконання проєкту...")

print("Створення бази даних…")
os.system("py create_db.py")

print("\nЗаповнення тестовими даними…")
os.system("py fill_db.py")

print("\nВиконання запитів…")
os.system("py queries.py")

print("Усі операції виконані успішно.")
print("\nРоботу завершенно.")