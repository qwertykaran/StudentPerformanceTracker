from database import connect_db

def add_student(name, age, class_):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, class) VALUES (?, ?, ?)", (name, age, class_))
    conn.commit()
    conn.close()

def add_marks(student_id, subject, marks):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO marks (student_id, subject, marks) VALUES (?, ?, ?)", (student_id, subject, marks))
    conn.commit()
    conn.close()

def view_student_performance(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()
    
    if student:
        print(f"Performance Report for {student[0]}:")
        cursor.execute("SELECT subject, marks FROM marks WHERE student_id=?", (student_id,))
        results = cursor.fetchall()
        total = 0
        for subject, marks in results:
            print(f" - {subject}: {marks}")
            total += marks
        if results:
            avg = total / len(results)
            print(f"\nAverage Marks: {avg:.2f}")
            grade = assign_grade(avg)
            print(f"Grade: {grade}")
        else:
            print("No marks found.")
    else:
        print("Student not found.")
    conn.close()

def assign_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 75:
        return 'A'
    elif avg >= 60:
        return 'B'
    elif avg >= 40:
        return 'C'
    else:
        return 'F'

def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM marks WHERE student_id=?", (student_id,))
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()
