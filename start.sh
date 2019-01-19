#!/bin/bash

echo "Starting gromari Deployment"
echo "Running migrations:"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py makemigrations accounts
python3 manage.py migrate accounts
python3 manage.py makemigrations rooms
python3 manage.py migrate rooms
python3 manage.py makemigrations django_celery_results
python3 manage.py migrate django_celery_results
echo "Done migrations"
echo "Running collect static:"
python3 manage.py collectstatic --noinput --clear
echo "done collectstatic"
echo "Starting supervisor"
service supervisor start
supervisorctl reread
supervisorctl update
echo "Starting gromari server"
gunicorn gromari.wsgi -b 0.0.0.0:8000 --timeout 300 >> /code/log/gromari/gromari.log
