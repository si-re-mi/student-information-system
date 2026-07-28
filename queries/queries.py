import sqlite3
from .query_utils import execute_query
from sql_queries import (
    GROUP_RATING_QUERY,
    LIBRARY_DEBTORS_QUERY,
    STUDENT_RATING_AND_SCHOLARSHIP_QUERY,
    ACADEMIC_PERFORMANCE_REPORT_QUERY,
    MOST_POPULAR_HOBBIES_QUERY,
    SURNAME_HISTORY_1_QUERY,
    SURNAME_HISTORY_2_QUERY
)

def run_queries():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    execute_query(
        "\nРейтинг групи", 
        GROUP_RATING_QUERY
    )

    execute_query(
        "\nБоржники бібліотеки",
        LIBRARY_DEBTORS_QUERY
    )

    execute_query(
        "\nРейтинг і стипендія студента", 
        STUDENT_RATING_AND_SCHOLARSHIP_QUERY
    )


    execute_query(
        "\nЗвіт успішності групи",
        ACADEMIC_PERFORMANCE_REPORT_QUERY
    )

    execute_query(
        "\nНайпопулярніші хобі",
        MOST_POPULAR_HOBBIES_QUERY
    )

    execute_query(
        "\nЗміна прізвища",
        SURNAME_HISTORY_1_QUERY
    )
    

    execute_query(
        "\nЗміна прізвища",
        SURNAME_HISTORY_2_QUERY
    )

    conn.close()
