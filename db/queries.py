# RDBMS - СУБД
import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    db_path = Path(__file__).parent.parent / "db.sqlite"
    global db, cursor
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

def create_tables():
    cursor.execute("""
        DROP TABLE IF EXISTS courses
    """)
    cursor.execute("""
        DROP TABLE IF EXISTS teachers
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            duration INTEGER,
            image TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            photo TEXT,
            course_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    """)
    db.commit()

def populate_tables():
    cursor.execute("""
        INSERT INTO courses (name, duration, image) VALUES
        ('Backend', 5, 'python.png'),
        ('Frontend', 5, 'react.png'),
        ('Design', 3, 'design.png'),
        ('Android', 6, 'react.png'),
        ('Project management', 2, 'react.png')
    """)
    cursor.execute("""
        INSERT INTO teachers (name, photo, course_id) VALUES
        ("Alex", "python.png", 1),
        ("Igor", "react.png", 2),
        ("Adilet", "react.png", 3)
    """)
    db.commit()

def get_courses():
    # cursor.execute("SELECT * FROM courses LIMIT 2")
    cursor.execute("SELECT * FROM courses ORDER BY name DESC")
    # [("Backend",), ("Frontend",)]
    return cursor.fetchall()

def get_course_by_id(id: int):
    cursor.execute("SELECT * FROM courses WHERE id = ?", (id,))
    # cursor.execute("SELECT * FROM courses WHERE id = 2")
    return cursor.fetchone()

def get_all_teachers():
    cursor.execute("""
        SELECT t.name, c.name, c.duration FROM teachers AS t
        JOIN courses AS c ON t.course_id = c.id
    """)
    return cursor.fetchall()

def get_teachers_by_course_id(course_id: int):
    cursor.execute("""
        SELECT * FROM teachers WHERE course_id = :qqqq
    """, {"qqqq": course_id}
    )
    return cursor.fetchall()

def get_teachers_by_course_name(name: str):
    cursor.execute("""
        SELECT * FROM teachers WHERE course_id = (
            SELECT id FROM courses WHERE name = :name
        ) ORDER BY name
    """, {"name": name})
    return cursor.fetchall()

def get_course_by_name(name: str):
    cursor.execute("SELECT * FROM courses WHERE name LIKE ?", (name,))
    return cursor.fetchone()

if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    # print(get_courses())
    # print(get_course_by_id(1))
    # print(get_course_by_name("Frontend"))
    # pprint(get_all_teachers())
    # pprint(get_teachers_by_course_id(2))
    pprint(get_teachers_by_course_name("Backend"))


# Primary Key  - уникальный идентификатор, первичный ключ
    
# ORM - Object Relational Mapping - маппинг между объектами и базой данных
    
# Связи между таблицами
# Courses
# 1, 'Backend', 5, 'python.png',
# 2, 'Frontend', 5, 'react.png',
# 3, 'Design', 3, 'react.png'
# 4, 'Android', 6, 'react.png'
# 5, 'Project management', 2, 'react.png'

# Foreign key - Внешний клюй
# Teachers
# 1, 'Alex', 1
# 2, "igor", 1
# 3, "Adilet", 1
# 4, "Vladimir", 2