import random
import bs4
import requests
import telebot
from telebot import types

bot = telebot.TeleBot('5233609274:AAHNNXK_4_Lj_W2-NjnfKyE6SN3Wx1H7U6g')
first =  ["Год для вас будет наполнен сюрпризами. Все они будут приятными, поэтому опасаться их не стоит", "Вы откроете в себе скрытые резервы, что позволит решиться на самые безумные поступки."]
second = ["Сейчас удачное время для признания в любви. Вам ответят взаимностью", "Счастье уже стоит за дверью."]
second_2 = ["Приготовьтесь, что получаемые вами результаты, успех в делах и яркие отношения с любимыми могут стать предметом зависти","Невозможно отвести глаз от твоей красоты!"]
third = ["Невозможно отвести глаз от твоей красоты!","Больше нет таких умных и проницательных девушек."]


# ----------------------------------------------------------------------
@bot.message_handler(commands=["start"])
def start(message, res=False):
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
        item1 = types.KeyboardButton('Об авторе')
        item2 = types.KeyboardButton('Гороскоп')
        item3 = types.KeyboardButton('Анекдоты')
        item4 = types.KeyboardButton('Показать китю')
        markup.add(item1,item2,item3,item4)
        bot.send_message(message.chat.id, 'Привет,{0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.chat.type == 'private':
        if message.text == 'Гороскоп':
            bot.send_message(message.from_user.id, "сейчас я расскажу тебе гороскоп на сегодня.")
            keyboard = types.InlineKeyboardMarkup()
            key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
            keyboard.add(key_oven)
            key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
            keyboard.add(key_telec)
            key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
            keyboard.add(key_bliznecy)
            key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
            keyboard.add(key_rak)
            key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
            keyboard.add(key_lev)
            key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
            keyboard.add(key_deva)
            key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
            keyboard.add(key_vesy)
            key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
            keyboard.add(key_scorpion)
            key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
            keyboard.add(key_strelec)
            key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
            keyboard.add(key_kozerog)
            key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
            keyboard.add(key_vodoley)
            key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
            keyboard.add(key_ryby)
            bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)

            @bot.callback_query_handler(func=lambda call: True)
            def callback_worker(call):
                if call.data == "zodiac":
                    msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_2) + ' ' + random.choice(third)
                    bot.send_message(message.chat.id, msg,)

        elif message.text == "Об авторе":
            bot.send_message(message.chat.id, 'Привет,  меня зовут Катя. Мне 19 лет. Я учусь в Питере на специальности "Создание цифрового контента"',)
        elif message.text == "Анекдоты":
            bot.send_message(message.chat.id, text=get_anekdot())
        elif message.text == "Показать китю":
            contents = requests.get('https://aws.random.cat/meow').json()
            urlCAT = contents['file']
            bot.send_photo(message.chat.id, photo=urlCAT, caption="Китя")



# -----------------------------------------------------------------------
def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()



