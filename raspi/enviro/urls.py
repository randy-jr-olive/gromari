from django.urls import path

from . import views

urlpatterns = [
    path('', views.enviro, name='enviro'),
]
