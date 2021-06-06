# Интерактивная карта Москвы

![Website preview](https://sun9-7.userapi.com/impg/hmzBWKmi_m0Vc4g850C4alGEzET5MhdG-NCWcw/eFfED3HVrEw.jpg?size=1920x1080&quality=96&sign=9f893ddaf4bcc5a2413ce448b07b0e8d&type=album)

Карта Москвы с примечательными местами.

- ### [**Ссылка на сайт** (на ресурсе PythonAnywhere)](http://azabirov.pythonanywhere.com/)
- [Админка сайта](http://azabirov.pythonanywhere.com/admin)
___

### Как нанести новое место на карту?
Воспользуйтесь командой `loadplace`:

`python manage.py loadplace <ссылка на GEOJSon метку>`

Сделать это можно и через админку, с помощью дружелюбного интерфейса.
___

### Тестовый логин и пароль от админки:
>login: *admin*
>password: *admin123*
___

### Как запустить проект на локальном сервере?
- Установить Python 
- Создать и активировать виртуальное окружение:

`python -m venv env`
`source env/scripts/activate`
- Создать в папке с проектом файл .env, указав в нем следующие значение:

`SECRET_KEY = '<значение секретного ключа на ваш выбор (чем сложнее - тем лучше)>'`
`DEBUG = <True либо False, зависит от целей>`
- Установить зависимости:

`pip install -r requirements.txt`
- Запустить проект:

`python manage.py runserver`
- Проект запустить по адресу:

http://localhost:8000

