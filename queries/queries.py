import sqlite3
from .query_utils import execute_query
from .sql_queries import (
    GROUP_RATING_QUERY,
    LIBRARY_DEBTORS_QUERY,
    STUDENT_RATING_AND_SCHOLARSHIP_QUERY,
    ACADEMIC_PERFORMANCE_REPORT_QUERY,
    MOST_POPULAR_HOBBIES_QUERY,
    SURNAME_HISTORY_1_QUERY,
    SURNAME_HISTORY_2_QUERY
)

def show_group_rating():
    execute_query(
        "\nРейтинг групи", 
        GROUP_RATING_QUERY
    )

def show_library_debtors():
    execute_query(
        "\nБоржники бібліотеки",
        LIBRARY_DEBTORS_QUERY
    )

def show_student_rating():
        execute_query(
        "\nРейтинг і стипендія студента", 
        STUDENT_RATING_AND_SCHOLARSHIP_QUERY
    )

def show_academic_report():
    execute_query(
        "\nЗвіт успішності групи",
        ACADEMIC_PERFORMANCE_REPORT_QUERY
    )

def show_popular_hobbies():
    execute_query(
        "\nНайпопулярніші хобі",
        MOST_POPULAR_HOBBIES_QUERY
    )

def show_surname_history():
    execute_query(
        "\nЗміна прізвища",
        SURNAME_HISTORY_1_QUERY
    )
    execute_query(
        "\nЗміна прізвища",
        SURNAME_HISTORY_2_QUERY
    )

def run_queries():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    show_group_rating()
    show_library_debtors()
    show_student_rating()
    show_academic_report()
    show_popular_hobbies()
    show_surname_history()

    conn.close()
