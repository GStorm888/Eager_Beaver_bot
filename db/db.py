import sqlite3
from essence import User, Lesson, ChangeLesson, Admin


class Database:
    SCHEMA = "db/schema.sql"
    DATABASE = "db/Eager_Beaver.db"

    @staticmethod
    def execute(sql, params=()):
        connection = sqlite3.connect(Database.DATABASE, check_same_thread=False)

        cursor = connection.cursor()

        cursor.execute(sql, params)

        connection.commit()

    @staticmethod
    def create_table():
        with open(Database.SCHEMA) as schema_file:
            connection = sqlite3.connect(Database.DATABASE)
            cursor = connection.cursor()
            cursor.executescript(schema_file.read())
            connection.commit()
            connection.close()
    
    @staticmethod
    def add_user(user: User):
        Database.execute(
            "INSERT INTO users (const_user_name, user_user_name, telegram_id, name_teacher) VALUES (?, ?, ?, ?)",
            [
                user.const_user_name,
                user.user_user_name,
                user.telegram_id,
                user.name_teacher
            ],
        )
        return True
    
    @staticmethod
    def add_lesson(lesson: Lesson):
        Database.execute(
            "INSERT INTO lessons (telegram_id, day_lesson, time_lesson, time_reminder, name_teacher) VALUES (?, ?, ?, ?, ?)",
            [   
                lesson.telegram_id,
                lesson.day_lesson,
                lesson.time_lesson,
                lesson.time_reminder
                lesson.name_teacher
            ],
        )
        return True
    
    @staticmethod
    def add_change_lesson(change_lessons: ChangeLesson):
        Database.execute(
            "INSERT INTO users (telegram_id, day_lesson, old_time_lesson, new_time_lesson, time_reminder, name_teacher) VALUES (?, ?, ?, ?, ?, ?)",
            [
                change_lessons.telegram_id,
                change_lessons.day_lesson,
                change_lessons.old_time_lesson,
                change_lessons.new_time_lesson,
                change_lessons.time_reminder,
                change_lessons.name_teacher
            ],
        )
        return True
    
    @staticmethod
    def add_admin(admin: Admin):
        Database.execute(
            "INSERT INTO users (telegram_id, day_lesson, old_time_lesson, new_time_lesson, time_reminder, name_teacher) VALUES (?, ?, ?, ?, ?, ?)",
            [
                admin.name_admin,
                admin.password_admin,
                admin.telegram_id,
                admin.status_admin,
            ],
        )
        return True