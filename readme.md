# Weather bot for telegram

<h2>1. pip install pyowm</h1>

<h2>2. pip install pyTelegramBotAPI==0.3.0</h1>

First of all you need to get tokens for Weather parsing and your telegramm-bot. You can read the detailed instructions in their documentation.
Insert your token from OWM into "<i>owm = OWM('TOKEN', config_dict)</i>" 
and token from telegram-bot into "<i>bot = telebot.TeleBot('TOKEN', parse_mode=None)</i>"

I used <b>uncensored.txt</b> as censor, you could add unwanted expressions into it. 

Last correct responses from your bot are saved and could be used from button in the lower part of application.


Run script - <i>python Weather.py</i>


