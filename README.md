# Карта достопримечательностей

Интерактивная карта с интересными местами ~~Москвы~~ Вашего города.

Пример сайта можно посмотреть [ на pythonanywhere](https://srgmarkov.pythonanywhere.com/)

## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```bash
pip install -r requirements.txt
```
Создайте базу данных SQLite

```bash
python3 manage.py migrate
```
Создайте учетку администратора
```bash
python3 manage.py createsuperuser
```
Запустите сервер
```bash
python3 manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `DATABASE_FILEPATH` — полный путь к файлу базы данных SQLite, например: `/home/user/map_base.sqlite3`
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## Добавление мест на карте

Зайти в админ панель джанго `{Адрес вашего сайта}/admin`
Добавить локацию:
- Название
- Краткое описание
- Полное описание(используется WSWING редактор)
- Координаты
- Фото локации



## Цели проекта

Код написан в учебных целях — для курса по Django на сайте [Devman](https://dvmn.org),
для урока [Пишем Яндекс.Афишу](https://dvmn.org/modules/django/lesson/yandex-afisha/)

