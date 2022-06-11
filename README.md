## Информация о проекте
Цель проекта

Разработка сайта интернет магазина мебели. Учебный проект.

##Используемые технологии:
* Python 3.9
* Django 3.2
* Bootstrap 5
* PostgreSQL 14

##Основные возможности веб-сайта
Просмотр главной страницы и страницы контактов с информационным содержимым

Просмотр всего каталога товаров, товаров, разделенных по категориям, детальной информации о каждом товаре

Возможность зарегистрироваться на сайте

Для зарегистрированных пользователей возможность добавлять товары в корзину и делать заказ на сайте

Для персонала магазина возможность удобно просматривать и обрабатывать заказы, редактировать каталоги 

##Настройка проекта
Перейти в корень проекта

Создать файл с переменными окружения .env в папке ./store_site по шаблону .env.template

Установить зависимости
```
pip install -r requirements.txt
```
Выполнить миграцию базы данных
```
python manage.py makemigrations
python manage.py migrate
```

Для загрузки тестовых данных с содержимым каталога
```
python manage.py fill_db
```
Запуск проекта
```
python manage.py runserver
```