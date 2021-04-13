# Weather bot for telegram

<h2>1. <code>pip install pyowm</code></h1>

<h2>2. <code>pip install pyTelegramBotAPI==0.3.0</code></h1>

<p>First of all you need to get tokens for <a href="https://pypi.org/project/pyowm/" rel="nofollow">OWM</a> and <a href="https://core.telegram.org/bots/api" rel="nofollow">telegramm-bot</a>. You can read the detailed instructions in their documentation.</p>
<p>Insert your token from OWM into "<code>owm = OWM('<b>TOKEN</b>', config_dict)</code>" 
and token from telegram-bot into "<code>bot = telebot.TeleBot('<b>TOKEN</b>', parse_mode=None)</code>"</p>

<p>I used <code><b>uncensored.txt</b></code> as censor, you could add unwanted expressions into it.</p>

<p>Last correct responses from your bot are saved and could be used from button in the lower part of application.</p>


<p>Run script - <code><i>python Weather.py</i></code></p>


