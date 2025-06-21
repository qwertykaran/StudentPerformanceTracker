from database import create_tables
from operations import *

def menu():
    print("""
    ===== Student Performance Tracker =====
    1. Add Student
    2. Add Marks
    3. View Performance
    4. Delete Student
    5. Exit
    """)

def main():
    create_tables()
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            class_ = input("Class: ")
            add_student(name, age, class_)
        elif choice == '2':
            student_id = int(input("Student ID: "))
            subject = input("Subject: ")
            marks = int(input("Marks: "))
            add_marks(student_id, subject, marks)
        elif choice == '3':
            student_id = int(input("Student ID: "))
            view_student_performance(student_id)
        elif choice == '4':
            student_id = int(input("Student ID: "))
            delete_student(student_id)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
