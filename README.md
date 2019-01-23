# Watcher of Friends Online

Скрипт предназначен для отображения списка ваших друзей онлайн. 
Для работы скрипту нужен `APP_ID`, который можно получить создав приложение здесь https://vk.com/editapp?act=create

При запуске скрипта вам нужно передать этот id через переменную окружения `VK_APP_ID`:

```angular2
VK_APP_ID=123456 python3 vk_friends_online.py
```

Скрипт запросил ваши логин и пароль, и после этого выведет список ваших друзей онлайн.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
