#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn djangoProject.wsgi:application --bind 0.0.0.0:8080