from django.shortcuts import render
from celery.task.control import inspect
from django.contrib.auth.decorators import login_required
from celery import current_app


@login_required
def home(request):
    return render(request, 'home.html')
