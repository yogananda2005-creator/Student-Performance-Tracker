# from student_tracker import StudentTracker
# student_tracker.py
# import sqlite3

# class Student:
#     def __init__(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number

# class StudentTracker:
#     def __init__(self, db_name='students.db'):
#         self.conn = sqlite3.connect(db_name)
#         self.cursor = self.conn.cursor()

#     def add_student(self, name, roll_number):
#         try:
#             self.cursor.execute("INSERT INTO students (roll_number, name) VALUES (?, ?)", (roll_number, name))
#             self.conn.commit()
#             print(f"Student {name} added.")
#         except sqlite3.IntegrityError:
#             print("Student with this roll number already exists.")

#     def add_grade(self, roll_number, subject, grade):
#         self.cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))
#         if not self.cursor.fetchone():
#             print("Student not found.")
#             return
#         self.cursor.execute("INSERT INTO grades (roll_number, subject, grade) VALUES (?, ?, ?)", (roll_number, subject, grade))
#         self.conn.commit()
#         print(f"Grade added: {subject} = {grade}")

#     def view_student(self, roll_number):
#         self.cursor.execute("SELECT name FROM students WHERE roll_number = ?", (roll_number,))
#         student = self.cursor.fetchone()
#         if not student:
#             print("Student not found.")
#             return
#         print(f"Name: {student[0]}, Roll Number: {roll_number}")
#         self.cursor.execute("SELECT subject, grade FROM grades WHERE roll_number = ?", (roll_number,))
#         grades = self.cursor.fetchall()
#         if grades:
#             for subject, grade in grades:
#                 print(f"{subject}: {grade}")
#             avg = sum(g for _, g in grades) / len(grades)
#             print(f"Average: {avg:.2f}")
#         else:
#             print("No grades available.")

#     def close(self):
#         self.conn.close()


import sqlite3

class StudentTracker:
    def __init__(self, db_name='students.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_student(self, name, roll_number):
        try:
            self.cursor.execute("INSERT INTO students (roll_number, name) VALUES (?, ?)", (roll_number, name))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Student with this roll number already exists.")

    def add_grade(self, roll_number, subject, grade):
        self.cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))
        if not self.cursor.fetchone():
            print("Student not found.")
            return
        self.cursor.execute("INSERT INTO grades (roll_number, subject, grade) VALUES (?, ?, ?)", (roll_number, subject, grade))
        self.conn.commit()

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




# from student_tracker 
# import StudentTracker

def main():
    tracker = StudentTracker()

    while True:
        print("\n--- Student Performance Tracker ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Details")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            tracker.add_student(name, roll)

        elif choice == '2':
            roll = input("Enter roll number: ")
            subject = input("Enter subject: ")
            grade = int(input("Enter grade (0-100): "))
            tracker.add_grade(roll, subject, grade)

        elif choice == '3':
            roll = input("Enter roll number: ")
            tracker.view_student(roll)

        elif choice == '4':
            tracker.close()
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()


