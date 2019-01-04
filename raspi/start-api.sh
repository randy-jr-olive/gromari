#!/bin/bash

echo "Starting gromari api"
echo "Running migrations:"
python3 manage.py makemigrations
python3 manage.py migrate
echo "Done migrations"
echo "Running collect static:"
python3 manage.py collectstatic --noinput
echo "done collectstatic"
echo "Starting gromari api"
gunicorn raspi.wsgi -b 0.0.0.0:8000 --timeout 300 >> /code/log/api/api.log
