import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            class TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject TEXT,
            marks INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    ''')
    conn.commit()
    conn.close()
