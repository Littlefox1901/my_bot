import telebot
from telebot import types

bot = telebot.TeleBot('5233609274:AAHNNXK_4_Lj_W2-NjnfKyE6SN3Wx1H7U6g')
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user))


# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text
    bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)

first =  ["Год для вас будет наполнен сюрпризами. Все они будут приятными, поэтому опасаться их не стоит", "Вы откроете в себе скрытые резервы, что позволит решиться на самые безумные поступки."]
second = ["Сейчас удачное время для признания в любви. Вам ответят взаимностью", "Счастье уже стоит за дверью."]
second_2 = ["Приготовьтесь, что получаемые вами результаты, успех в делах и яркие отношения с любимыми могут стать предметом зависти","Невозможно отвести глаз от твоей красоты!"]
third = ["Невозможно отвести глаз от твоей красоты!","Больше нет таких умных и проницательных девушек."]
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    def get_text_messages(message):
        if message.text == "Привет":
            bot.send_message(message.from_user.id, "Привет,сегодня я расскажу твой личный гороскоп")
            keyboard = types.InlineKeyboardMarkup()
            btn_oven = types.InlineKeyboardButton(text= "Овен", callback_data="zodiac")
            keyboard.add(btn_oven)



# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()



