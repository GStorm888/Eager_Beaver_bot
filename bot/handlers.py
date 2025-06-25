from telebot import TeleBot, types
from db.db import Database
from essence import User, Reminder
import datetime

def register_handlers(bot: TeleBot):

    def examination_date_type(user_time):
        time_format = "%H:%M"
        try:
            datetime.datetime.strptime(user_time, time_format)
            return True
        except:
            return False
        
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
            bot.send_message(message.chat.id, "привет, я твои напоминания и информация о занятиях.")
            start_help_back_button(message)
            return None
        else:
            login(message)


    def login(message):
        bot.send_message(message.chat.id, "привет, я твои напоминания и информация о занятиях. введи свое имя и фамилию(через пробел), для того чтобы я понимал кто ты")
        bot.register_next_step_handler(message, start)


    def login_user_name(message):
        user_input = message.text
        user_name = user_input.replace(" ", "_")
        telegram_id = str(message.chat.id)
        if Database.get_user_from_users_by_const_user_name(user_name) is not None:
            Database.change_telegram_id_in_users_by_user_name(user_name)
            bot.send_message(
                message.chat.id, "хорошо, я тебя нашел"
            )
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

    @bot.message_handler(
        func=lambda message: message.text == "🔙Назад"
    )
    def back_button(message):
        bot.send_message(message.chat.id, "Хорошо, возвращаю вас в Help")
        help(message)
