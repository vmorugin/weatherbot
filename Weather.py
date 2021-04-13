import random
import telebot
from telebot import types
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import NotFoundError

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Portuguese

owm = OWM('TOKEN', config_dict)
mgr = owm.weather_manager()
uncens = set()
with open ("Uncens.txt") as unc:
	for line in unc:
		line = line.strip()
		uncens.add(line)  # Подключили словарь нецензурных слов.

# 1 0 7 6 2 3 4 5 было
# 0 1 2 3 4 5 6 7 стало

# Словарь с выражениями
ph  = ["Возможен дожь, захвати зонтик. ","Возможно будет дождь. "]
ph0 = ["Идёт дождь, не забудь зонтик. ","Синоптики обещают дождь. "]
ph1 = ["На улице холода, лучше одеться теплее", "На улице очень холодно, лучше дома посидеть.", "На улице холодно, лучше надеть подштанники"]
ph2 = ["На улице холодно, лучше надеть перчатки.", "На улице холодно, одевайся теплее.", "На улице холодно, рекомендую надеть подштанники."]
ph3 = ["Погода около нуля, возможен гололёд, будь аккуратней", "На улице возможен гололёд"]
ph4 = ["На улице холодно, одевайся теплее.","На улице холодно, настало время достать легкую куртку.","На улице холодно, не забудь шапку."]
ph5 = ["Ещё пока холодно, лекую куртку лучше надеть", "На улице не очень тепло, но это временно."]
ph6 = ["На улице прохладно, надень легкую куртку или свитер.", "На улице прохладно, лучше надень ветровку.", "На улице прохладно, лучше надеть легкую куртку"]
ph7 = ["На улице тепло, надевай что хочешь.","На улице тепло, самое время прогуляться.", "На улице отличная погода для прогулки."]
ph8 = ["На улице очень жарко.","На улице жара, возьми с собой водички.","На улице жарко, лучше прикрыть голову."]

non = ["А я что-то не знаю такого города...", "Хм, или лыжи не едут или я не знаю такого города...", "Непонятна, попробуй другой город или проверь на ошибки..."]

bot = telebot.TeleBot('TOKEN', parse_mode=None) 

@bot.message_handler(content_types=['text'])
def send_echo(message):
	if "start" in message.text or "help" in message.text:  # Ответ на help или start от пользователя.
		bot.send_message(message.chat.id,"Привет! Я бот, который рассказывает о погоде в любом городе и даёт совет.")
		bot.send_message(message.chat.id,"Напиши мне любой город и я скажу шо на улице.\nМожно указать область через запятую, например:\n_'Каменка,_ _Воронеж'_", parse_mode="Markdown")
		return
	try:  # Проверяем, можем ли мы получить погоду по сообщению от пользователя.
		observation = mgr.weather_at_place(message.text)
		w = observation.weather
		temp = round(w.temperature('celsius')["temp"])
		city = message.text

		answer =  "В городе " + "*" + message.text + "*" + " сейчас " + w.detailed_status  # Показываем какая на улице погода, ставим соответствующий смайл.
		if "ясно" in w.detailed_status:
			answer += " \u2600\ufe0f"
		elif "пасмурно" in w.detailed_status or "облачность" in w.detailed_status:
			answer += " \u2601\ufe0f"
		elif "с прояснениями" in w.detailed_status:
			answer += " \u26c5\ufe0f"
		elif "снег" in w.detailed_status:
			answer += " \u2744\ufe0f"
		elif "дождь" in w.detailed_status:
			answer += " \u2614\ufe0f"
		elif "мгла" in w.detailed_status:
			answer += " \u2601\ufe0f \u2601\ufe0f"

		answer += "\n_Температура_: _" + str(temp) + "_\t\t_Влажность_: _" + str(w.humidity) +"%_" + " \n\n"  # Выводим фразу в зависимости от температуры и погоды.
		if "дождь" in w.detailed_status and int(*w.rain.values()) < 0.5:
			answer += random.choice(ph) + " Осадки: " + str(*w.rain.values()) + " мм. "
		if "дождь" in w.detailed_status and int(*w.rain.values()) >= 0.5:
			answer += random.choice(ph0) + " Осадки: " + str(*w.rain.values()) + " мм. "
		elif temp < -10:
			answer += random.choice(ph1) 

		elif temp <= -5:
			answer += random.choice(ph2)

		elif -1 <= temp <= 1:
			answer += random.choice(ph3)

		elif temp < 5:
			answer += random.choice(ph4)

		elif temp < 10:
			answer += random.choice(ph5)

		elif temp < 20:
			answer += random.choice(ph6)

		elif temp < 28:
			answer += random.choice(ph7)

		else:
			answer += random.choice(ph8)	

		markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)  # Кнопка, повторяющая прошлый город.
		markup_btn1 = types.KeyboardButton(city)
		markup.add(markup_btn1)
		bot.send_message(message.chat.id,answer, reply_markup = markup, parse_mode="Markdown")

	except NotFoundError:  # Исключение
		if message.text.lower() in uncens:  # Фильтр нецензурных выражений
			bot.send_message(message.chat.id, 'Сам ' + message.text)  
		else:  								# Если город не удалось узнать
			bot.send_message(message.chat.id,random.choice(non))

bot.polling( none_stop = True)
