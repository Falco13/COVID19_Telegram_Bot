import COVID19Py
import telebot
from telebot import types

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('your_bot_token')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button1 = types.KeyboardButton('🌏 В мире')
    button2 = types.KeyboardButton('Украина')
    button3 = types.KeyboardButton('Россия')
    button4 = types.KeyboardButton('Беларусь')
    button5 = types.KeyboardButton('Италия')
    button6 = types.KeyboardButton('США')
    button7 = types.KeyboardButton('Франция')
    button8 = types.KeyboardButton('Германия')
    button9 = types.KeyboardButton('Япония')
    button10 = types.KeyboardButton('Испания')
    button11 = types.KeyboardButton('Турция')
    button12 = types.KeyboardButton('Польша')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
               button12)

    send_message = f"<b>Привет 👋\nВыбери страну, чтоб узнать ситуацию с COVID-19 🚑</b>"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess_text(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == 'сша':
        location = covid19.getLocationByCountryCode('US')
    elif get_message_bot == 'украина':
        location = covid19.getLocationByCountryCode('UA')
    elif get_message_bot == 'россия':
        location = covid19.getLocationByCountryCode('RU')
    elif get_message_bot == 'беларусь':
        location = covid19.getLocationByCountryCode('BY')
    elif get_message_bot == 'италия':
        location = covid19.getLocationByCountryCode('IT')
    elif get_message_bot == 'франция':
        location = covid19.getLocationByCountryCode('FR')
    elif get_message_bot == 'германия':
        location = covid19.getLocationByCountryCode('DE')
    elif get_message_bot == 'япония':
        location = covid19.getLocationByCountryCode('JP')
    elif get_message_bot == 'испания':
        location = covid19.getLocationByCountryCode('ES')
    elif get_message_bot == 'турция':
        location = covid19.getLocationByCountryCode('TR')
    elif get_message_bot == 'польша':
        location = covid19.getLocationByCountryCode('PL')
    else:
        location = covid19.getLatest()
        final_message = f"🌍 <b>Данные по всему миру:</b>\n\n🚑 <b>Заболевших: </b>{location['confirmed']:,}\n☠ <b>Сметрей: </b>{location['deaths']:,}"

    if final_message == "":
        final_message = f"🚑 <b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n☠ <b>Сметрей: </b>{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
