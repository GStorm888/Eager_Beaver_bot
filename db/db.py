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
                user.name_teacher,
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
                lesson.time_reminder,
                lesson.name_teacher,
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
                change_lessons.name_teacher,
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



    @staticmethod  # получение всех пользователей
    def get_all_users():
        connection = sqlite3.connect(Database.DATABASE)

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users")

        all_users = cursor.fetchall()
        users = []
        for id, const_user_name, user_user_name, telegram_id, name_teacher in all_users:
            user = User(const_user_name, user_user_name, telegram_id, name_teacher, id)
            users.append(user)
        if len(users) == 0:
            return None
        return users


    @staticmethod  # получение всех пользователей
    def get_all_lessons():
        connection = sqlite3.connect(Database.DATABASE)

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM lessons")

        all_lessons = cursor.fetchall()
        lessons = []
        for id, telegram_id, day_lesson, time_lesson, time_reminder, name_teacher in all_lessons:
            lesson = Lesson(telegram_id, day_lesson, time_lesson, time_reminder, name_teacher, id)
            lessons.append(lessons)
        if len(lessons) == 0:
            return None
        return lessons

    @staticmethod  # получение всех пользователей
    def get_all_change_lessons():
        connection = sqlite3.connect(Database.DATABASE)

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM change_lessons")

        all_change_lessons = cursor.fetchall()
        change_lessons = []
        for id, telegram_id, day_lesson, old_time_lesson, new_time_lesson, time_reminder, name_teacher in all_change_lessons:
            change_lesson = ChangeLesson(telegram_id, day_lesson, old_time_lesson, new_time_lesson, time_reminder, name_teacher, id)
            change_lessons.append(change_lesson)
        if len(change_lessons) == 0:
            return None
        return change_lessons


    @staticmethod  # получение всех пользователей
    def get_all_admins():
        connection = sqlite3.connect(Database.DATABASE)

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM admins")

        all_admins = cursor.fetchall()
        admins = []
        for id, name_admin, password_admin, telegram_id, status_admin in all_admins:
            admin = Admin(name_admin, password_admin, telegram_id, status_admin, id)
            admins.append(admin)
        if len(admins) == 0:
            return None
        return admins

    
    @staticmethod
    def get_user_from_users_by_telegram_id(telegram_id):
        connection = sqlite3.connect(Database.DATABASE, check_same_thread=False)

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE telegram_id = ?", [telegram_id]
        )
        users = cursor.fetchall()

        if len(users) == 0:
            return None

        id, const_user_name, user_user_name, telegram_id, name_teacher = users[0]
        user = User(const_user_name, user_user_name, telegram_id, name_teacher, id)
        return user


    @staticmethod 
    def change_telegram_id_in_users_by_user_name(telegram_id, const_user_name):
        Database.execute(
            "UPDATE users SET telegram_id=? WHERE const_user_name=?",
            [telegram_id, const_user_name],
        )
        return True

    @staticmethod
    def get_admin_from_admin_by_telegram_id(telegram_id)
        connection = sqlite3.connect(Database.DATABASE, check_same_thread=False)

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM admins WHERE telegram_id = ?", [telegram_id]
        )
        admins = cursor.fetchall()

        if len(admins) == 0:
            return None

        id, name_admin, password_admin, telegram_id, status_admin = admins[0]
        admin = Admins(name_admin, password_admin, telegram_id, status_admin, id)
        return admin