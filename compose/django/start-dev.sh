#!/bin/sh
python manage.py migrate
python manage.py runserver 0.0.0.0:8000 & celery -A eshop worker -l info #& celery worker --app=orders.tasks
