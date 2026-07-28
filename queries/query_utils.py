import sqlite3

def execute_query(txt, query):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    print(txt)
    cursor.execute(query)
    for row in cursor.fetchall():
            print(row)