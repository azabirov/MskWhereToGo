# Интерактивная карта Москвы

![Website preview](https://sun9-34.userapi.com/impg/vyGddoARGE1JC1lEaNjLNsvRCES8HeLb9U8NZQ/Dv6hzO0uGjM.jpg?size=1920x1080&quality=96&sign=35d6698ef13b8d2d8a4379ab08936192&type=album)

### *Примечательные места на карте москвы*

[**Ссылка на сайт** (на ресурсе PythonAnywhere)](http://azabirov.pythonanywhere.com/)
[Админка сайта](http://azabirov.pythonanywhere.com/admin)
___

### Как нанести новое место на карту?
Двумя способами:
- Через админку, с помощью дружелюбного интерфейса.

- Воспользовашись командой `loadplace`:

`python manage.py loadplace <ссылка на GEOJSon метку>`

Пример данных в формате GEOJSon, которые нужно передать по ссылке:
```
{
    "title": "Название",
    "imgs": [
        "http://placehold.it/350x50",
        "http://placehold.it/350x50",
    ],
    "description_short": "Краткое описание",
    "description_long": "<p>Длинное описание в HTML</p>",
    "coordinates": {
        "lng": "37.32478",
        "lat": "55.70731"
    }
}
```

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
- Сервер запустится по адресу:

http://localhost:8000

