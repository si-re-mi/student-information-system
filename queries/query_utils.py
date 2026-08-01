import sqlite3
from config.config import DATABASE_NAME

def execute_query(txt, query):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    print(txt)
    cursor.execute(query)
    for row in cursor.fetchall():
            print(row)