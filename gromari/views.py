from django.shortcuts import render
from celery.task.control import inspect
from celery import current_app


def home(request):
    return render(request, 'home.html')
