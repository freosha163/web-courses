
# API-сервис для управления вебинарами и курсами онлайн-школы.

### Стек технологий
- проект написан на Python с использованием Django REST Framework
- базы данны - Postgresql
- система управления версиями - git
- документация drf-yasg




## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

    git clone git@github.com:freosha163/web-courses

Перейти в директорию проекта

    cd courses

Cоздать и активировать виртуальное окружение:

    python -m venv env

Для macOS:

    source env/bin/activate

Для Windows:

    source env/scripts/activate


Установить зависимости из файла requirements.txt:

    pip install -r requirements.txt

Выполнить миграции:

    python manage.py migrate

Запустить проект:

    python manage.py runserver


### Документация по проекту доступна по адресу:

    http://127.0.0.1/redoc/

    http://127.0.0.1/swagger/


### Автор проекта
_[freosha163](https://github.com/freosha163)_, python-developer
