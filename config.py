import os
import pathlib
from pyowm.utils import config

BASE_DIR = pathlib.Path(__file__).parent.resolve()

PYOWM_CONFIG = config.get_default_config()

# Here is your Telebot Api token. Add them to your envelopment or type manually
TELEBOT_TOKEN = os.getenv('TELEBOT_TOKEN', None)
OWM_TOKEN = os.getenv('OWM_TOKEN', None)

# your language here, eg. Portuguese
PYOWM_CONFIG['language'] = 'ru'

ANSWERS = {
	'maybe_rain': [
		"Возможен дожь, захвати зонтик. ",
		"Возможно будет дождь. "
	],
	'rain': [
		"Идёт дождь, не забудь зонтик. ",
		"Синоптики обещают дождь. "
	],
	'extreme_cold': [
		"На улице холода, лучше одеться теплее",
		"На улице очень холодно, лучше дома посидеть.",
		"На улице холодно, лучше надеть подштанники"
	],
	'cold': [
		"На улице холодно, лучше надеть перчатки.",
		"На улице холодно, одевайся теплее.",
		"На улице холодно, рекомендую надеть подштанники."
	],
	'around_zero': [
		"Погода около нуля, возможен гололёд, будь аккуратней",
		"На улице возможен гололёд"
	],
	'above_zero': [
		"На улице холодно, одевайся теплее.",
		"На улице холодно, настало время достать легкую куртку.",
		"На улице холодно, не забудь шапку."
	],
	'autumn_cold':  [
		"Ещё пока холодно, лекую куртку лучше надеть",
		"На улице не очень тепло, но это временно."
	],
	'light_cold': [
		"На улице прохладно, надень легкую куртку или свитер.",
		"На улице прохладно, лучше надень ветровку.",
		"На улице прохладно, лучше надеть легкую куртку"
	],
	'warm': [
		"На улице тепло, надевай что хочешь.",
		"На улице тепло, самое время прогуляться.",
		"На улице отличная погода для прогулки."
	],
	'hot': [
		"На улице очень жарко.",
		"На улице жара, возьми с собой водички.",
		"На улице жарко, лучше прикрыть голову."
	],
	'city_not_found': [
		"А я что-то не знаю такого города...",
		"Хм, или лыжи не едут или я не знаю такого города...",
		"Непонятна, попробуй другой город или проверь на ошибки..."
	]
}

UNCENSORED = set()

UNCENSORED_PATH = BASE_DIR / 'uncensored.txt'

# Подключили словарь нецензурных слов.
if UNCENSORED_PATH.exists():
	with open(UNCENSORED_PATH, 'rb') as unc:  # You can remove this point if you want.
		for line in unc:
			line = line.strip().decode('utf-8-sig')
			UNCENSORED.add(line)
