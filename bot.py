import telebot
from telebot import types


TOKEN = '8421969968:AAFokWamiocgyjMCUGO4KZZSsPI7nH72mUc'


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📅 Расписание")
    btn2 = types.KeyboardButton("🔗 Полезные ссылки")
    btn3 = types.KeyboardButton("ℹ️ О школе")
    markup.add(btn1, btn2, btn3)

    welcome_text = (f"Привет, {message.from_user.first_name}! 👋\n"
                    f"Я бот-помощник для учеников нашей школы.\n"
                    f"Выбери нужный раздел в меню ниже:")
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == "📅 Расписание":
        schedule_text = ("📅 **Расписание уроков на понедельник:**\n"
                         "1. Разговоры о важном (каб. 24)\n"
                         "2. Классный час (каб. 24)\n"
                         "3. Русский язык (каб. 28)\n"
                         "4. ОБЗР (каб. 44)\n"
                         "5. Англ. язык (22)\n"
                         "6. Литература (28)\n"
                         "7. Алгебра (41)\n"
                         "8. Информатика (42)\n"
                         "9. Информатика (42)\n"
                         "\n"
                         "*Актуальное расписание уточняйте у классного руководителя.*")
        bot.send_message(message.chat.id, schedule_text, parse_mode='Markdown')

    elif message.text == "🔗 Полезные ссылки":
        markup = types.InlineKeyboardMarkup()
        btn_site = types.InlineKeyboardButton("🌐 Сайт школы", url="https://shkoladva.ru/")
        btn_diary = types.InlineKeyboardButton("📚 Электронный дневник",
                                               url="https://dnevnik.ru")
        btn_edu_platform = types.InlineKeyboardButton("💡 Образовательная платформа", url="https://uchi.ru")

        markup.add(btn_site)
        markup.add(btn_diary, btn_edu_platform)

        bot.send_message(message.chat.id, "Выберите полезный ресурс:", reply_markup=markup)

    elif message.text == "ℹ️ О школе":
        school_info = ("🏫 **Информация о МОУ СОШ №2:**\n"
                       "📍 **Адрес:** ул. Кирова, д. 13, г. Коряжма\n"
                       "📞 **Телефон:** +7 (81850) 3-49-55 (Директор)\n"
                       "⏰ **Часы работы:** Пн-Пт 8:00 - 16:00")
        bot.send_message(message.chat.id, school_info, parse_mode='Markdown')

    else:
        bot.send_message(message.chat.id, "Извините, я пока не знаю такой команды. 😕\n"
                                          "Пожалуйста, воспользуйтесь кнопками меню внизу экрана.")


if __name__ == "__main__":
    print("Бот 'Школьный помощник' запущен и готов к работе...")
    bot.polling(none_stop=True)


