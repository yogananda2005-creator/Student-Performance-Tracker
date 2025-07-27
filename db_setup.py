# # db_setup.py
# import sqlite3

# def init_db():
#     conn = sqlite3.connect('students.db')
#     cursor = conn.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS students (
#             roll_number TEXT PRIMARY KEY,
#             name TEXT NOT NULL
#         )
#     """)

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS grades (
#             roll_number TEXT,
#             subject TEXT,
#             grade INTEGER,
#             FOREIGN KEY (roll_number) REFERENCES students(roll_number)
#         )
#     """)

#     conn.commit()
#     conn.close()

# if __name__ == '__main__':
#     init_db()
#     print("Database initialized successfully.")


import sqlite3

def init_db():
    conn = sqlite3.connect('students.db')  # This creates the file in your project folder
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_number TEXT PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            roll_number TEXT,
            subject TEXT,
            grade INTEGER,
            FOREIGN KEY (roll_number) REFERENCES students(roll_number)
        )
    """)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("✅ Database initialized successfully.")
