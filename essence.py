from dataclasses import dataclass


@dataclass
class User:
    const_user_name: str
    user_user_name: str
    telegram_id: str = None
    name_teacher: str
    id: int = None


@dataclass
class Lesson:
    telegram_id: str = None
    day_lesson: int
    time_lesson: str
    time_reminder: str
    name_teacher: str
    id: int = None

@dataclass
class ChangeLesson:
    telegram_id: str = None
    day_lesson: int
    old_time_lesson: str
    new_time_lesson: str
    name_teacher: str
    id: int = None

@dataclass
class Admin:
    name_admin: str
    password_admin: str
    telegram_id: str
    status_admin: str
    id: int = None