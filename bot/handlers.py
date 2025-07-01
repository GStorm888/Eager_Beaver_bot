from telebot import TeleBot, types
from db.db import Database
from essence import User, Lesson, ChangeLesson, Admin
import datetime


def register_handlers(bot: TeleBot):
    def examination_date_type(user_time):
        time_format = "%H:%M"
        try:
            datetime.datetime.strptime(user_time, time_format)
            return True
        except:
            return False

    @bot.message_handler(func=lambda message: message.text == "🔙Назад")
    def back_button(message):
        bot.send_message(message.chat.id, "Хорошо, возвращаю вас в Help")
        help(message)

    # @bot.message_handler(commands=["test"])
    # def test(message):
    #     if message.text == "🔙Назад" or message.text == "Назад":
    #         handle_button(message)
    #         return
    #     Database.create_table()
    #     all_users = Database.get_all_users()
    #     print(all_users)
    #     all_reminders = Database.get_all_reminder()
    #     print(all_reminders)
    # markup = types.ReplyKeyboardRemove()
    # bot.send_message(message.chat.id, """клавиатура отчищена""", reply_markup=markup)

    @bot.message_handler(commands=["start"])
    def start(message):
        telegram_id = str(message.chat.id)
        if Database.get_user_from_users_by_telegram_id(telegram_id) is not None:
            bot.send_message(
                message.chat.id, "привет, я твои напоминания и информация о занятиях."
            )
            start_help_back_button(message)
            return None
        else:
            login(message)

    def login(message):
        bot.send_message(
            message.chat.id,
            "привет, я твои напоминания и информация о занятиях. введи свое имя и фамилию(через пробел), для того чтобы я понимал кто ты",
        )
        bot.register_next_step_handler(message, start)

    def login_user_name(message):
        user_input = message.text
        user_name = user_input.replace(" ", "_")
        if Database.get_user_from_users_by_const_user_name(user_name) is not None:
            Database.change_telegram_id_in_users_by_user_name(user_name)
            bot.send_message(message.chat.id, "хорошо, я тебя нашел")
        start_help_back_button(message)

    # появление кнопки '🔙Назад'
    def start_help_back_button(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("🔙Назад")
        markup.add(back)
        bot.send_message(
            message.chat.id,
            "Чтобы откуда угодно попасть в Help, просто нажмите на кнопку '🔙Назад'",
            reply_markup=markup,
        )

    @bot.message_handler(commands=["help"])
    def help(message):
        telegram_id = str(message.chat.id)
        user = Database.get_user_from_users_by_telegram_id(telegram_id)
        admin = Database.get_admin_from_admin_by_telegram_id(telegram_id)
        markup = types.InlineKeyboardMarkup()
        if user is not None:
            help_bttn = types.InlineKeyboardButton(text="🆘help", callback_data="help")
            start_bttn = types.InlineKeyboardButton(
                text="🚀start", callback_data="start"
            )

            view_lessons_bttn = types.InlineKeyboardButton(
                text="просмотр всех занятий на этой неделе",
                callback_data="view_lessons",
            )
            view_next_lesson_bttn = types.InlineKeyboardButton(
                text="просмотр ближайшего занятия", callback_data="view_next_lesson"
            )

            rename_bttn = types.InlineKeyboardButton(
                text="изменить имя пользователя", callback_data="rename"
            )
            markup.add(help_bttn, start_bttn)
            markup.add(view_lessons_bttn, view_next_lesson_bttn)
            markup.add(rename_bttn)

        if admin.status_admin == 1:
            add_lesson_bttn = types.InlineKeyboardButton(
                text="добавить занятие", callback_data="add_lesson"
            )

            change_lesson_bttn = types.InlineKeyboardButton(
                text="изменить занятие", callback_data="change_lesson"
            )

            delete_lesson_bttn = types.InlineKeyboardButton(
                text="отмена занятия", callback_data="delete_lesson"
            )
            reschedule_lesson_bttn = types.InlineKeyboardButton(
                text="перенос занятия", callback_data="reschedule_lesson"
            )

            view_my_reschedule_lesson_bttn = types.InlineKeyboardButton(
                text="просмотр моих переносов",
                callback_data="view_my_reschedule_lesson",
            )
            markup.add(add_lesson_bttn)
            markup.add(change_lesson_bttn)
            markup.add(delete_lesson_bttn)
            markup.add(reschedule_lesson_bttn)
            markup.add(view_my_reschedule_lesson_bttn)

            if admin.status_admin == 2:
                view_eschedule_lessons_bttn = types.InlineKeyboardButton(
                    text="просмотр всех переносов",
                    callback_data="view_eschedule_lessons",
                )

                send_message_studends_bttn = types.InlineKeyboardButton(
                    text="отправка сообщения всем ученикам",
                    callback_data="send_message_studends",
                )

                send_message_teachers_bttn = types.InlineKeyboardButton(
                    text="отправка сообщения всем учителям",
                    callback_data="send_message_teachers",
                )

                add_user_bttn = types.InlineKeyboardButton(
                    text="добавить пользователя", callback_data="add_user"
                )
                markup.add(view_eschedule_lessons_bttn)
                markup.add(send_message_studends_bttn)
                markup.add(send_message_teachers_bttn)
                markup.add(add_user_bttn)

                if admin_status_admin == 3:
                    chek_db = types.InlineKeyboardButton(
                        text="просмотр БД", callback_data="chek_db"
                    )
                    markup.add(chek_db)

    bot.send_message(
        message.chat.id,
        "в кнопках все команды и функции",
        reply_markup=markup,
    )
    markup.add(delete_account_bttn)
