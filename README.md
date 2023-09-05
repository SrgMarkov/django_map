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

`При запуске локально на ПК [http://127.0.0.1:7006/admin/](http://127.0.0.1:7006/admin/)`

Добавить локацию:
- Название
- Краткое описание
- Полное описание(используется WSWING редактор)
- Координаты
- Фото локации

**Пример файла JSON:**
```
{
    "title": "Горбовская ГЭС",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/151dc8d2833276130c3dff6dd1e43aac.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/5aca226c55eb7dc89d4d7547aea9bc01.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/90825cfcffe6fa578881bac11c7bbc11.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/e66bce160f1ec41593f52e9e744e3514.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0b647ff875464605f6f2ec2b8fe9e709.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4e0615f8bb5c53890354975679ab7c0b.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1ba047f0e1e885f4aff5ee18d54e87bc.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f19617366541e5f2e4dd46e5ada9546a.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/379de8e28e22bec9696a573e29208a10.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/38d794bbfe3db2e10f5ea11fad80bdd6.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4af219237df1691ffe0d4ba41a2f5b41.jpg"
    ],
    "description_short": "В 80 километрах от Москвы стоит Горбовская ГЭС — заброшенная станция, где отлично сохранились механизмы плотины, фильтры и даже загадочный тоннель, о предназначении которого до сих пор ходят легенды. Горбовская ГЭС сегодня — это своеобразный музей раритетных конструкций.",
    "description_long": "<p>Горбовская ГЭС была сооружена в 1953 году. Она была достаточно мощной, на её борту установили два 250-киловатных генератора, а также фильтры, которые и сейчас можно увидеть, посетив это место. ГЭС работала на целлюлозную фабрику до её закрытия в 1990 году. В 2002 и сама ГЭС окончательно прекратила функционировать.</p><p>Сегодня это заброшенная станция, которая привлекает как романтиков, так и специалистов. Здесь есть на что посмотреть и тем, и другим. Романтики могут предаться размышлениям о бренности мира у реки на фоне урбанистического пейзажа, а ещё эта ГЭС — прекрасная декорация для фотосессии. А если термины «крыльчатка», «шибер», «задвижки», «турбина» для вас не пустой звук, то станция станет ещё и наглядным «музеем» раритетных деталей и конструкций.</p><p>Горбовская ГЭС полна тайн и загадок. Возможно, именно вам удастся разгадать тайну находящегося здесь тоннеля. Одни утверждают, что это подрывной тоннель на случай войны, другие — что просто водоотвод, но его истинное назначение неизвестно до сих пор.</p><p>Огромное количество необычных деталей завораживает — помимо открытых конструкций, на ГЭС есть и небольшое помещение, входы туда закрыты, но руку с фотоаппаратом просунуть в незаколоченное отверстие можно. Некоторые любители приключений таким образом запечатлели старое, но вполне сохранное оборудование, воронки для масла, измерительные аппараты и прочие интересные детали, которые приводили в движение некогда величественную ГЭС.</p><p>Вход не ограждён, охраны нет, однако официально у ГЭС есть хозяин — «Сельэлектрострой».</p>",
    "coordinates": {
        "lng": "36.26108899999998",
        "lat": "55.65323799999996"
    }
}
```


## Цели проекта

Код написан в учебных целях — для курса по Django на сайте [Devman](https://dvmn.org),
для урока [Пишем Яндекс.Афишу](https://dvmn.org/modules/django/lesson/yandex-afisha/)

