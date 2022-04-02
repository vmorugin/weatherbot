# Weather bot for telegram

<code>pip install requirements.txt</code>


<p>First of all you need to get tokens for <a href="https://pypi.org/project/pyowm/" rel="nofollow">OWM</a> and <a href="https://pypi.org/project/pyTelegramBotAPI/" rel="nofollow">telegramm-bot</a>. You can read the detailed instructions in their documentation.</p>

```python
# Insert your token from OWM into:
owm = OWM('TOKEN<', config_dict)

# and token from telegram-bot into
bot = telebot.TeleBot('TOKEN', parse_mode=None)
```

<p>I used <code><b>uncensored.txt</b></code> as censor, you could add unwanted expressions into it.</p>

<p>Last correct responses from your bot are saved and could be used from button in the lower part of application.</p>


<p>Run script - <code><i>python main.py</i></code></p>

