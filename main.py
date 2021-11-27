import random
import telebot
from telebot import types
from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError

import config
from config import ANSWERS, UNCENSORED

owm = OWM(config.OWM_TOKEN, config.PYOWM_CONFIG)
mgr = owm.weather_manager()

bot = telebot.TeleBot(config.TELEBOT_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def info_message(message):
	bot.send_message(message.chat.id, "Привет! Я бот, который рассказывает о погоде в любом городе и даёт совет.")
	bot.send_message(message.chat.id,
	                 "Напиши мне любой город и я скажу шо на улице.\nМожно указать область через запятую, например:\n_'Каменка,_ _Воронеж'_""",
	                 parse_mode="Markdown")


@bot.message_handler(content_types=['text'])
def send_echo(message):
	try:  # Проверяем, можем ли мы получить погоду по сообщению от пользователя.
		observation = mgr.weather_at_place(message.text)
		w = observation.weather
		temp = round(w.temperature('celsius')["temp"])
		city = message.text

		answer = f"В городе *{message.text}* сейчас {w.detailed_status} "
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

		answer += f"\n_Температура_: _{str(temp)}_\t\t_Влажность_: _{str(w.humidity)}%_ \n\n"
		if "дождь" in w.detailed_status and int(*w.rain.values()) < 0.5:
			answer += random.choice(ANSWERS.get('maybe_rain')) + f" Осадки: {str(*w.rain.values())} мм. "
		if "дождь" in w.detailed_status and int(*w.rain.values()) >= 0.5:
			answer += random.choice(ANSWERS.get('rain')) + f" Осадки: {str(*w.rain.values())} мм. "
		elif temp < -10:
			answer += random.choice(ANSWERS.get('extreme_cold'))

		elif temp <= -5:
			answer += random.choice(ANSWERS.get('cold'))

		elif -1 <= temp <= 1:
			answer += random.choice(ANSWERS.get('around_zero'))

		elif temp < 5:
			answer += random.choice(ANSWERS.get('above_zero'))

		elif temp < 10:
			answer += random.choice(ANSWERS.get('autumn_cold'))

		elif temp < 20:
			answer += random.choice(ANSWERS.get('light_cold'))

		elif temp < 28:
			answer += random.choice(ANSWERS.get('warm'))

		else:
			answer += random.choice(ANSWERS.get('hot'))

		markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)  # Кнопка, повторяющая прошлый город.
		markup_btn1 = types.KeyboardButton(city)
		markup.add(markup_btn1)
		bot.send_message(message.chat.id, answer, reply_markup=markup, parse_mode="Markdown")

	except NotFoundError:
		if message.text.lower() in UNCENSORED:  # Фильтр нецензурных выражений
			bot.send_message(message.chat.id, 'Сам ' + message.text)
		else:  # Если город не удалось узнать
			bot.send_message(message.chat.id, random.choice(ANSWERS.get('city_not_found')))


bot.polling(none_stop=True)
