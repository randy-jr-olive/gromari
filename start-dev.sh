#!/bin/bash

echo "Starting gromari Deployment"
echo "Running migrations:"
python3 manage.py makemigrations
python3 manage.py migrate
echo "Done migrations"
echo "Running collect static:"
python3 manage.py collectstatic --noinput
echo "done collectstatic"
echo "Starting celery"
celery multi start 1 -A gromari -B -n gromari --logfile=/code/log/celery/gromari_worker.log --pidfile=/celery-pidfiles/%n.pid
echo "Starting gromari server"
gunicorn gromari.wsgi -b 0.0.0.0:8000 --timeout 300 >> /code/log/gromari/gromari.log
