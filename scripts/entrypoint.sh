#!/bin/sh

set -e

python manage.py collectstatic --no-input

#gunicorn djangoProject.wsgi:application --bind 0.0.0.0:8080

uwsgi --socket :8000 --master --enable-threads --module djangoProject.wsgi