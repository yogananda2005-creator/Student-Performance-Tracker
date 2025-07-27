# from flask import Flask, render_template, request, redirect, url_for
# from student_tracker import StudentTracker


# import os
# import sqlite3
# from flask import Flask, render_template


# app = Flask(__name__)
# tracker = StudentTracker()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/add-student', methods=['GET', 'POST'])
# def add_student():
#     if request.method == 'POST':
#         name = request.form['name']
#         roll = request.form['roll']
#         tracker.add_student(name, roll)
#         return redirect(url_for('index'))
#     return render_template('add_student.html')

# @app.route('/add-grade', methods=['GET', 'POST'])
# def add_grade():
#     if request.method == 'POST':
#         roll = request.form['roll']
#         subject = request.form['subject']
#         grade = int(request.form['grade'])
#         tracker.add_grade(roll, subject, grade)
#         return redirect(url_for('index'))
#     return render_template('add_grade.html')

# # -------------------------------------------------
# @app.route("/view-student")
# def view_student():
#     import os
#     db_path = os.path.join(os.path.dirname(__file__), "students.db")
#     # conn = sqlite3.connect(db_path)

#     conn = sqlite3.connect("students.db")  # your actual DB file
#     cursor = conn.cursor()
#     student_data = cursor.execute("SELECT * FROM students").fetchall()
#     conn.close()
#     return render_template("view.html", data=student_data)




# # @app.route('/view-student', methods=['GET', 'POST'])
# # def view_student():
# #     student_data = None
# #     grades = []
# #     average = None


# # -------------------------------------------------

#     if request.method == 'POST':
#         roll = request.form['roll']
#         student_data = tracker.cursor.execute(
#             "SELECT name FROM students WHERE roll_number = ?", (roll,)
#         ).fetchone()
#         grades = tracker.cursor.execute(
#             "SELECT subject, grade FROM grades WHERE roll_number = ?", (roll,)
#         ).fetchall()
#         if grades:
#             average = sum([g[1] for g in grades]) / len(grades)

#     return render_template(
#         'view_student.html',
#         student=student_data,
#         grades=grades,
#         average=average
#     )

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
from student_tracker import StudentTracker
import os
import sqlite3

app = Flask(__name__)
tracker = StudentTracker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        tracker.add_student(name, roll)
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/add-grade', methods=['GET', 'POST'])
def add_grade():
    if request.method == 'POST':
        roll = request.form['roll']
        subject = request.form['subject']
        grade = int(request.form['grade'])
        tracker.add_grade(roll, subject, grade)
        return redirect(url_for('index'))
    return render_template('add_grade.html')

# ✅ View All Students (optional)
@app.route("/students")
def view_all_students():
    db_path = os.path.join(os.path.dirname(__file__), "students.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    student_data = cursor.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("view.html", data=student_data)

# ✅ View One Student + Grades
@app.route('/view-student', methods=['GET', 'POST'])
def view_student():
    student_data = None
    grades = []
    average = None

    if request.method == 'POST':
        roll = request.form['roll']
        student_data = tracker.cursor.execute(
            "SELECT name FROM students WHERE roll_number = ?", (roll,)
        ).fetchone()
        grades = tracker.cursor.execute(
            "SELECT subject, grade FROM grades WHERE roll_number = ?", (roll,)
        ).fetchall()
        if grades:
            average = sum([g[1] for g in grades]) / len(grades)

    return render_template(
        'view_student.html',
        student=student_data,
        grades=grades,
        average=average
    )

if __name__ == '__main__':
    app.run(debug=True)
