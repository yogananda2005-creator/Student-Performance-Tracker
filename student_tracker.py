# student_tracker.py
import sqlite3

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

class StudentTracker:
    def __init__(self, db_name='students.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_student(self, name, roll_number):
        try:
            self.cursor.execute("INSERT INTO students (roll_number, name) VALUES (?, ?)", (roll_number, name))
            self.conn.commit()
            print(f"Student {name} added.")
        except sqlite3.IntegrityError:
            print("Student with this roll number already exists.")

    def add_grade(self, roll_number, subject, grade):
        self.cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))
        if not self.cursor.fetchone():
            print("Student not found.")
            return
        self.cursor.execute("INSERT INTO grades (roll_number, subject, grade) VALUES (?, ?, ?)", (roll_number, subject, grade))
        self.conn.commit()
        print(f"Grade added: {subject} = {grade}")

    def view_student(self, roll_number):
        self.cursor.execute("SELECT name FROM students WHERE roll_number = ?", (roll_number,))
        student = self.cursor.fetchone()
        if not student:
            print("Student not found.")
            return
        print(f"Name: {student[0]}, Roll Number: {roll_number}")
        self.cursor.execute("SELECT subject, grade FROM grades WHERE roll_number = ?", (roll_number,))
        grades = self.cursor.fetchall()
        if grades:
            for subject, grade in grades:
                print(f"{subject}: {grade}")
            avg = sum(g for _, g in grades) / len(grades)
            print(f"Average: {avg:.2f}")
        else:
            print("No grades available.")

    def close(self):
        self.conn.close()
