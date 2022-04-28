# nested_comments

Техническое задание. Реализация вложенных комментариев и вывод с определённой вложенностью.

Использовался следующий стэк

```
- Django
- Django Rest Framework
- django-mptt
- drf-yasg
- psycopg2
- pip-compile-multi
- python-dotenv
```

## Установка и запуск(локально):

1. Скачать проект

   - git clone https://github.com/scad89/nested_comments.git

2. Добавить файл с переменными окружения(.env) в корень проекта

3. Активировать виртуальное окружение:

   - . venv_name/Scripts/activate - Windows
   - source venv_name/bin/activate - Linux

4. Установить зависимости(в виртуальном окружении):

   - pip-compile -U
   - pip install -r requirements.txt

5. Сделать миграции:

   - python manage.py makemigrations
   - python manage.py migrate

6. Создать суперпользователя для администраторского Web UI(если требуется):

   - python manage.py createsuperuser

7. Запустить сервер:

   - python manage.py runserver

## Установка и запуск(docker-compose):

1. Добавить файл с переменными окружения(.env_docker) в корень проекта
2. Запустить командой:
   - sudo docker-compose up -d

Если необходимо пересобрать контейнеры(внесли какие-то изменения) использовать:

- sudo docker-compose up --build

Если Вы запускаете проект на Windows, а docker из-под виртуальной машины(по типу VirtualBox), проект
по адресу 0.0.0.0:8000 может не открыться. Тогда необходимо использовать адрес 192.168.99.100:8000

Для остановки контейнеров используйте команду:

```
docker-compose down -v
```

## Описание методов и документация:

```
http://0.0.0.0:8000/admin - панель администратора
http://0.0.0.0:8000/create_article/ - создание статьи
http://0.0.0.0:8000/articles/ - вывод всех статей
http://0.0.0.0:8000/article/<pk>/ - вывод детальной информации о статье и его комментариев до 3-ого уровня вложенности
http://0.0.0.0:8000/create_comment/ - создание комментария к статье/создание комментария на комментарий
http://0.0.0.0:8000/comment/<pk>/ - вывод комментария и всех его вложенных комментариев
http://0.0.0.0:8000/docs/ - документация
```

## Contacts

- Instagram: [@igor*komkov*](https://www.instagram.com/igor_komkov_/)
- Vk.com: [Igor Komkov](https://vk.com/zzzscadzzz)
- Linkedin: [Igor Komkov](https://www.linkedin.com/in/igor-komkov/)
- email: **scad200@gmail.com**
- Telegram: **@zzzSCADzzz**
