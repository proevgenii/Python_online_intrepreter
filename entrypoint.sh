#!/usr/bin/env bash

set -e
python manage.py  makemigrations --noinput
python manage.py  migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn djangoProject.wsgi:application -b 0.0.0.0:8080 --reload