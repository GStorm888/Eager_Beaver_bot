CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    const_user_name TEXT NOT NULL UNIQUE,
    user_user_name TEXT,
    telegram_id TEXT NOT NULL UNIQUE,
    name_teacher TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id TEXT NOT NULL,
    day_lesson INTEGER NOT NULL, 
    time_lesson TEXT NOT NULL,
    time_reminder TEXT NOT NULL,
    name_teacher TEXT NOT NULL,
    FOREIGN KEY (const_user_name) REFERENCES users(const_user_name),
    FOREIGN KEY (telegram_id) REFERENCES users(telegram_id),
    FOREIGN KEY (name_teacher) REFERENCES users(name_teacher)
);

CREATE TABLE IF NOT EXISTS change_lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id TEXT NOT NULL,
    day_lesson INTEGER NOT NULL,
    old_time_lesson TEXT NOT NULL,
    new_time_lesson TEXT NOT NULL,
    time_reminder TEXT NOT NULL,
    name_teacher TEXT NOT NULL,
    FOREIGN KEY (day_lesson) REFERENCES lessons(day_lesson),
    FOREIGN KEY (old_time_lesson) REFERENCES lessons(time_lesson),
    FOREIGN KEY (name_teacher) REFERENCES lessons(name_teacher)

);

CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_admin TEXT NOT NULL, 
    password_admin TEXT NOT NULL,
    telegram_id TEXT NOT NULL, 
    status_admin INTEGER NOT NULL
)