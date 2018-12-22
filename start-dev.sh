#!/bin/bash

echo "Starting CanGrow Deployment"
echo "Running migrations:"
python3 manage.py makemigrations
python3 manage.py migrate
echo "Done migrations"
echo "Running collect static:"
python3 manage.py collectstatic --noinput
echo "done collectstatic"
echo "Starting celery"
celery multi start 1 -A cangrow -B -n cangrow --logfile=/code/log/celery/cangrow_worker.log --pidfile=/celery-pidfiles/%n.pid
echo "Starting CanGrow server"
gunicorn cangrow.wsgi -b 0.0.0.0:8000 --timeout 300 >> /code/log/cangrow/cangrow.log
