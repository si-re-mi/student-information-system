import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

print("\nРейтинг групи")

cursor.execute("""
SELECT
    pn.last_name,
    pn.first_name,
    ROUND(AVG(g.points),2) AS rating
FROM students s
JOIN person_names pn
    ON pn.person_id = s.person_id
    AND pn.valid_to IS NULL
JOIN grades g
    ON g.student_id = s.id
WHERE s.group_id = 1
GROUP BY s.id
ORDER BY rating DESC
""")

for row in cursor.fetchall():
    print(row)

print("\nБоржники бібліотеки")

cursor.execute("""
SELECT
    p.last_name,
    p.first_name,
    COUNT(bl.id),
    ROUND(SUM(b.price),2)
FROM book_loans bl
JOIN students s ON s.id = bl.student_id
JOIN person_names p
ON p.person_id = s.person_id
AND p.valid_to IS NULL
JOIN books b ON b.id = bl.book_id
WHERE bl.return_date IS NULL
AND julianday('now') - julianday(bl.loan_date) > 365
GROUP BY s.id
""")

for row in cursor.fetchall():
    print(row)

print("\nРейтинг і стипендія студента")

cursor.execute("""
SELECT
    p.last_name,
    p.first_name,
    ROUND(AVG(g.points),2),
    AVG(sc.amount)
FROM students s
JOIN person_names p
ON p.person_id = s.person_id
AND p.valid_to IS NULL
JOIN grades g
ON g.student_id = s.id
LEFT JOIN scholarships sc
ON sc.student_id = s.id
AND sc.semester='2025-1'
WHERE s.id = 1
AND g.semester='2025-1'
GROUP BY s.id
""")

for row in cursor.fetchall():
    print(row)

print("\nЗвіт успішності групи")

cursor.execute("""
SELECT
    p.last_name || ' ' || p.first_name,
    SUM(CASE WHEN g.national_grade='Відмінно' THEN 1 ELSE 0 END),
    SUM(CASE WHEN g.national_grade='Добре' THEN 1 ELSE 0 END),
    SUM(CASE WHEN g.national_grade='Задовільно' THEN 1 ELSE 0 END),
    SUM(CASE WHEN g.national_grade='Незадовільно' THEN 1 ELSE 0 END),
    COUNT(*)
FROM students s
JOIN person_names p
ON p.person_id = s.person_id
AND p.valid_to IS NULL
JOIN grades g ON g.student_id = s.id
WHERE s.group_id = 1
GROUP BY s.id
ORDER BY p.last_name
""")

for row in cursor.fetchall():
    print(row)

print("\nНайпопулярніші хобі")

cursor.execute("""
SELECT
    h.hobby_name,
    COUNT(*) AS students_count
FROM student_hobbies sh
JOIN hobbies h ON h.id = sh.hobby_id
GROUP BY h.id
ORDER BY students_count DESC
""")

for row in cursor.fetchall():
    print(row)

print("\nЗміна прізвища")

cursor.execute("""
SELECT
    last_name,
    first_name,
    middle_name
FROM person_names
WHERE person_id = 3
AND '2022-01-01'
BETWEEN valid_from
AND COALESCE(valid_to,'9999-12-31');
""")
for row in cursor.fetchall():
    print(row)
cursor.execute("""
SELECT
    last_name,
    first_name,
    middle_name
FROM person_names
WHERE person_id = 3
AND '2025-01-01'
BETWEEN valid_from
AND COALESCE(valid_to,'9999-12-31');
""")

for row in cursor.fetchall():
    print(row)

conn.close()
