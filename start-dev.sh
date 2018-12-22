#!/bin/bash

echo "Starting CanGrow Deployment"
# python3 manage.py migrate
celery multi start 1 -A cangrow -B -n cangrow --logfile=/code/log/celery/cangrow_worker.log --pidfile=/celery-pidfiles/%n.pid
gunicorn cangrow.wsgi -b 0.0.0.0:8000 --timeout 300 >> /code/log/cangrow/cangrow.log
