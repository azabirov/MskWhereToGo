# Интерактивная карта Москвы с примечательными местами

Сайт для отображения GEOJson меток на карте города. Поможет вам найти место поблизости где можно отлично провести время.

![Website preview](https://sun9-34.userapi.com/impg/vyGddoARGE1JC1lEaNjLNsvRCES8HeLb9U8NZQ/Dv6hzO0uGjM.jpg?size=1920x1080&quality=96&sign=35d6698ef13b8d2d8a4379ab08936192&type=album)


[**Ссылка на сайт** (на ресурсе PythonAnywhere)](http://azabirov.pythonanywhere.com/)

[Админка сайта](http://azabirov.pythonanywhere.com/admin)

## Установка. Как запустить проект на локальном сервере?
- Установить Python
- Создать и активировать виртуальное окружение:
```bash
python -m venv env
source env/scripts/activate
```
- Установить зависимости:
```bash
pip install -r requirements.txt
```
- Создать в папке с проектом файл .env, указав в нем следующие значение:
```
SECRET_KEY = <значение секретного ключа на ваш выбор (чем сложнее - тем лучше)>
DEBUG = <True либо False, зависит от целей>
ALLOWED_HOSTS = <имена хостов через пробел, например: localhost 127.0.0.1 azabirov.pythonanywhere.com>
```
- Запустить проект:
```bash
python manage.py runserver
```
- Собрать статику:
```bash
python manage.py collectstatic
```
- Сервер запустится по адресу:

http://localhost:8000

## Как нанести новое место на карту?
Двумя способами:
- Через [админку](http://azabirov.pythonanywhere.com/admin), с помощью дружелюбного интерфейса. Тестовые логин и пароль:
```
login: admin
password: admin123
```
- Воспользовавшись командой `loadplace` на запущенном сервере:
```bash
python manage.py loadplace <ссылка на GEOJSon метку>
```
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

>Данные для сайта взяты с сайта [Kudago](https://kudago.com)
